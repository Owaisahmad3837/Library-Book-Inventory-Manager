def show_report(library_data):

    print("\n====== LIBRARY REPORT ======")

    total_books = len(library_data)

    issued_books = 0

    for book in library_data.values():

        if book["issued"]:
            issued_books += 1

    available_books = total_books - issued_books

    print("Total books:", total_books)
    print("Issued books:", issued_books)
    print("Available books:", available_books)