from Configs.json import read_data, save_data

from Components.Add_books import add_data
from Components.Serach_book import search_book
from Components.issure_book import issue_book
from Components.return_book import return_book
from Components.Report_book import show_report


# Get the saved books when the program starts
library_data = read_data()


while True:

    print("\n")
    print("========== LIBRARY MANAGEMENT SYSTEM ==========")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Reports")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":

        add_data(library_data)

        # Save the new book
        save_data(library_data)

    elif choice == "2":

        search_book(library_data)

    elif choice == "3":

        issue_book(library_data)

        # Save the updated book status
        save_data(library_data)

    elif choice == "4":

        return_book(library_data)

        # Save the updated book status
        save_data(library_data)

    elif choice == "5":

        show_report(library_data)

    elif choice == "6":

        print("Thank you for using Library Management System!")
        break

    else:

        print("Invalid choice!")