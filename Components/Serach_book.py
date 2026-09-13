def search_book(library_data):

    print("\n====== SEARCH BOOK ======")
    print("1. Search by ID")
    print("2. Search by Name")
    print("3. Search by Author")
    print("4. Exit")

    condition = input("Enter condition: ").strip()

    if condition == "1":
        search_by_id(library_data)

    elif condition == "2":
        search_by_name(library_data)

    elif condition == "3":
        search_by_author(library_data)

    elif condition == "4":
        print("Exiting search...")

    else:
        print("Invalid condition!")


def search_by_id(library_data):

    print("\n=== Search by ID ===")

    book_id = input("Enter ID: ").strip()

    if book_id in library_data:
        print("\nBook Found:")
        print(library_data[book_id])
    else:
        print("Book not found!")


def search_by_name(library_data):

    print("\n=== Search by Name ===")

    name = input("Enter name: ").strip().lower()

    found = False

    for book_id, book in library_data.items():

        if book["name"].lower() == name:
            print("\nBook Found:")
            print("ID:", book_id)
            print("Name:", book["name"])
            print("Author:", book["author"])
            print("Issued:", book["issued"])

            found = True

    if not found:
        print("Book not found!")


def search_by_author(library_data):

    print("\n=== Search by Author ===")

    author = input("Enter author: ").strip().lower()

    found = False

    for book_id, book in library_data.items():

        if book["author"].lower() == author:
            print("\nBook Found:")
            print("ID:", book_id)
            print("Name:", book["name"])
            print("Author:", book["author"])
            print("Issued:", book["issued"])

            found = True

    if not found:
        print("Book not found!")