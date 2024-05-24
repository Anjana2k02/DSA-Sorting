class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrowed = False

    def __repr__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


class LinkedListNode:
    def __init__(self, book):
        self.book = book
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, book):
        new_node = LinkedListNode(book)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def remove(self, isbn):
        current = self.head
        prev = None
        while current:
            if current.book.isbn == isbn:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return current.book
            prev = current
            current = current.next
        return None

    def find(self, isbn):
        current = self.head
        while current:
            if current.book.isbn == isbn:
                return current.book
            current = current.next
        return None

    def __iter__(self):
        current = self.head
        while current:
            yield current.book
            current = current.next


class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def remove(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return v
        return None

    def find(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None


class Library:
    def __init__(self):
        self.books = LinkedList()
        self.book_index = HashTable()
        self.borrowed_books = LinkedList()

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        self.book_index.insert(title.lower(), book)

    def remove_book(self, title):
        book = self.book_index.find(title.lower())
        if book and not book.borrowed:
            self.book_index.remove(title.lower())
            self.books.remove(book.isbn)
            return book
        return None

    def search_book(self, title):
        return self.book_index.find(title.lower())

    def borrow_book(self, title):
        book = self.search_book(title)
        if book and not book.borrowed:
            book.borrowed = True
            self.borrowed_books.append(book)
            return book
        return None

    def return_book(self, title):
        book = self.search_book(title)
        if book and book.borrowed:
            book.borrowed = False
            self.borrowed_books.remove(book.isbn)
            return book
        return None

    def list_books(self):
        return list(self.books)

    def list_borrowed_books(self):
        return list(self.borrowed_books)


def main():
    library = Library()

    # Adding books
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
    library.add_book("To Kill a Mockingbird", "Harper Lee", "1234567891")
    library.add_book("1984", "George Orwell", "1234567892")

    # Listing all books
    print("All Books in Library:")
    for book in library.list_books():
        print(book)

    # Borrow a book
    print("\nBorrowing '1984':")
    borrowed_book = library.borrow_book("1984")
    if borrowed_book:
        print(f"Borrowed: {borrowed_book}")
    else:
        print("Book not available for borrowing.")

    # Listing all books
    print("\nAll Books in Library after borrowing '1984':")
    for book in library.list_books():
        print(book)

    # Listing borrowed books
    print("\nBorrowed Books:")
    for book in library.list_borrowed_books():
        print(book)

    # Returning a book
    print("\nReturning '1984':")
    returned_book = library.return_book("1984")
    if returned_book:
        print(f"Returned: {returned_book}")
    else:
        print("Book not found or not borrowed.")

    # Listing all books
    print("\nAll Books in Library after returning '1984':")
    for book in library.list_books():
        print(book)

    # Removing a book
    print("\nRemoving 'To Kill a Mockingbird':")
    removed_book = library.remove_book("To Kill a Mockingbird")
    if removed_book:
        print(f"Removed: {removed_book}")
    else:
        print("Book not found or currently borrowed.")

    # Listing all books
    print("\nAll Books in Library after removing 'To Kill a Mockingbird':")
    for book in library.list_books():
        print(book)


if __name__ == "__main__":
    main()
