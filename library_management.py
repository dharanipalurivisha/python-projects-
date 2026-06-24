def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    book_id = input("Enter book ID: ")

    with open("library.txt", "a") as f:
        f.write(f"{book_id},{title},{author},Available\n")

    print("Book added successfully!")


def view_books():
    try:
        print("\n--- All Books ---")
        with open("library.txt", "r") as f:
            for line in f:
                book_id, title, author, status = line.strip().split(",")
                print(f"ID: {book_id}, Title: {title}, Author: {author}, Status: {status}")
    except FileNotFoundError:
        print("No books found!")


def issue_book():
    book_id = input("Enter book ID to issue: ")

    try:
        with open("library.txt", "r") as f:
            lines = f.readlines()

        with open("library.txt", "w") as f:
            for line in lines:
                data = line.strip().split(",")
                if data[0] == book_id:
                    data[3] = "Issued"
                    print(f"Book '{data[1]}' issued!")
                f.write(",".join(data) + "\n")

    except FileNotFoundError:
        print("No books found!")


def return_book():
    book_id = input("Enter book ID to return: ")

    try:
        with open("library.txt", "r") as f:
            lines = f.readlines()

        with open("library.txt", "w") as f:
            for line in lines:
                data = line.strip().split(",")
                if data[0] == book_id:
                    data[3] = "Available"
                    print(f"Book '{data[1]}' returned!")
                f.write(",".join(data) + "\n")

    except FileNotFoundError:
        print("No books found!")


def delete_book():
    book_id = input("Enter book ID to delete: ")

    try:
        with open("library.txt", "r") as f:
            lines = f.readlines()

        with open("library.txt", "w") as f:
            for line in lines:
                if line.split(",")[0] != book_id:
                    f.write(line)

        print("Book deleted successfully!")

    except FileNotFoundError:
        print("No books found!")


while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Delete Book")
    print("6. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        add_book()
    elif ch == "2":
        view_books()
    elif ch == "3":
        issue_book()
    elif ch == "4":
        return_book()
    elif ch == "5":
        delete_book()
    elif ch == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")