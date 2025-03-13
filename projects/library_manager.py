# purpose of storing and loading data in json format(library.txt)
import json


# creating empty list for the purpose of storing new and old  books data.
library = []


# Load existing library data

def load_library(): # ye function sirf library.txt ka  data load karwaii ga
    global library
    try:
        with open("library.txt", "r", encoding="utf-8") as file:
            content = file.read()
            library = json.loads(content) if content.strip() else []
        print("\n Data loaded successfully!\n")
    except (FileNotFoundError, json.JSONDecodeError):
        library = []


# Save data in library.txt:

def save_library():
    with open("library.txt", "w", encoding="utf-8") as file:
        json.dump(library, file, indent=4, ensure_ascii=False)
    print("\n Library saved successfully!\n")



# Add book
def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    year = input("Enter publication year: ").strip()
    genre = input("Enter book genre: ").strip()
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

    book = {"title": title, "author": author, "year": year, "genre": genre, "read": read_status}
    library.append(book)

# Save after adding a book
    save_library()  

    print(f"\n '{title}' added successfully!\n")

# Remove book
def remove_book():
    title = input("Enter book title to remove: ").strip().lower()
    for book in library:
        if book["title"].lower() == title:
            library.remove(book)
            save_library()  # Save after removing a book
            print(f"\n '{title.title()}' removed from library!\n")
            return
    print(f"\n '{title.title()}' not found in library!\n")

# Search book
def search_book():
    query = input("Enter book title or author to search: ").strip().lower()
    found_books = [book for book in library if query in book['title'].lower() or query in book['author'].lower()]
    
    if found_books:
        print("\n Matching Books:")
        for book in found_books:
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {' Read' if book['read'] else ' Unread'}")
    else:
        print("\n No books found!\n")

# Display books
def display_books():
    if library:
        print("\n Your Library:\n")
        for i, book in enumerate(library, start=1):
            status = " Read" if book["read"] else " Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("\n Your library is empty!\n")

# Show statistics
def display_statistics():
    total_books = len(library)
    read_books = sum(1 for book in library if book['read'])
    read_percentage = (read_books / total_books) * 100 if total_books > 0 else 0

    print(f"\n Library Statistics:\nTotal Books: {total_books}\nPercentage Read: {read_percentage:.2f}%\n")

# Mark book as read
def mark_as_read():
    title = input("Enter book title to mark as read: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            book["read"] = True
            save_library()  # Save after marking a book as read
            print(f"\n '{title}' marked as read!\n")
            return
    print(f"\n '{title}' not found!\n")

# Load library before running menu
load_library()

# While loop
while True:
    print("\n Library Management System")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Display All Books")
    print("5. Show Statistics")
    print("6. Mark Book as Read")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        remove_book()
    elif choice == "3":
        search_book()
    elif choice == "4":
        display_books()
    elif choice == "5":
        display_statistics()
    elif choice == "6":
        mark_as_read()
    elif choice == "7":
        save_library()
        print(" Library saved. Exiting...")
        break
    else:
        print("\n Oops! It's wrong select again.")
