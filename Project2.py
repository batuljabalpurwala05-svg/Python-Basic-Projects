from datetime import datetime, timedelta

library = {}

def check_due_date(issue_date):
    return issue_date + timedelta(days=7)

def add_book():
    isbn = int(input("Enter ISBN Number :"))

    if isbn in library:
        print("ISBN already exists!!")
        return
    
    title =input("Enter title :")
    author = input("Enter author name :")

    library[isbn]={
        "title": title,
        "author" : author,
        "available":True,
        "borrower":None,
        "issue_date":None   
    }
    print("Book Record added!")

def issue_book():
    isbn = input("Enter ISBN: ").strip()   # remove extra spaces

    if isbn in library:
        if library[isbn]["available"]:
            borrower_id = input("Enter Borrower ID: ").strip()
            name = input("Enter Your Name: ").strip()

            issue_date = datetime.now()
            due_date = check_due_date(issue_date)

            library[isbn]["available"] = False
            library[isbn]["borrower"] = f"{name} ({borrower_id})"
            library[isbn]["issue_date"] = issue_date

            print("Book Issued Successfully!")
            print("Title   :", library[isbn]["title"])
            print("Due Date:", due_date.strftime("%d-%B-%Y"))

        else:
            print("Book already issued!")
    else:
        print("Book not found!")

def return_book():
    isbn = int(input("Enter ISBN number of book to be searched :"))

    if isbn in library:
        if not library[isbn]["available"]:
            library[isbn]["available"] = True
            library[isbn]["borrower"] = None
            library[isbn]["issue_date"] = None

            print("Book Returned Successfully!")
        else:
            print("Book was not issued!")
    else:
        print("Book not found!")

def search_book():
    keyword = input("Enter author or title name to search :").lower
    found = False
    for isbn, data in library.items():
        if keyword in data["title"].lower() or keyword in data["author"].lower():
            print("Book Found:")
            print("ISBN   :", isbn)
            print("Title  :", data["title"])
            print("Author :", data["author"])
            print("Status :", "Available" if data["available"] else "Issued")
            found = True

    if not found:
        print("No such book found!")

def view_catalog():
    if not library:
        print("No such book available")
        return
    print("===== LIBRARY CATALOG =====")
    for isbn, data in library.items():
        status = "Available" if data["available"] else "Issued"
        print("ISBN:",isbn,"| Title:",data['title'],"| Author:",data['author'],"| Status:",status)

def show_menu():
    print("\n====== LIBRARY MANAGEMENT SYSTEM ======")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. View Catalog")
    print("6. Exit")

while True:
    show_menu()
    choice = int(input("Enter your choice (1 to 6):"))

    if choice == 1:
        add_book()
    elif choice == 2:
        issue_book()
    elif choice == 3:
        return_book()
    elif choice == 4:
        search_book()
    elif choice == 5:
        view_catalog()
    elif choice == 6:
        print("Exiting Program....")
        break
    else:
        print("INVALID CHOICE!!") 

