def issue_book(library_data):

    print("\n====== ISSUE BOOK ======")

    book_id = input("Enter Book ID: ").strip()

    if book_id not in library_data:
        print("Book not found!")
        return

    if library_data[book_id]["issued"]:
        print("Book is already issued!")
        return

    library_data[book_id]["issued"] = True

    print("Book issued successfully!")