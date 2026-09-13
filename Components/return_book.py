def return_book(library_data):

    print("\n====== RETURN BOOK ======")

    book_id = input("Enter Book ID: ").strip()

    if book_id not in library_data:
        print("Book not found!")
        return

    if not library_data[book_id]["issued"]:
        print("Book is already available!")
        return

    library_data[book_id]["issued"] = False

    print("Book returned successfully!")