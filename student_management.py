def add_student():
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    with open("students.txt", "a") as f:
        f.write(f"{roll},{name},{marks}\n")

    print("Student added successfully!")


def display_students():
    try:
        with open("students.txt", "r") as f:
            print("\n--- All Students ---")
            for line in f:
                roll, name, marks = line.strip().split(",")
                print(f"Roll: {roll}, Name: {name}, Marks: {marks}")
    except FileNotFoundError:
        print("No student records found!")


def search_student():
    roll = input("Enter roll to search: ")

    try:
        with open("students.txt", "r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[0] == roll:
                    print(f"Found → Name: {data[1]}, Marks: {data[2]}")
                    return

        print("Student not found!")
    except FileNotFoundError:
        print("No student records found!")


def delete_student():
    roll = input("Enter roll to delete: ")

    try:
        with open("students.txt", "r") as f:
            lines = f.readlines()

        with open("students.txt", "w") as f:
            for line in lines:
                if line.split(",")[0] != roll:
                    f.write(line)

        print("Student deleted successfully!")

    except FileNotFoundError:
        print("No student records found!")


while True:
    print("\n===== Student Record Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")