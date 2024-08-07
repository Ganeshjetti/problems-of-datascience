# Define a Student class to represent a student
class Student:
    def __init__(self, student_id, name, books_borrowed):
        # Initialize student attributes: student ID, name, and number of books borrowed
        self.student_id = student_id
        self.name = name
        self.books_borrowed = 0
    def __str__(self):
        # Return a string representation of the student
        return (f"student id:{self.student_id},name:{self.name},booksborrowed:{self.books_borrowed}")
# Define a Book class to represent a book
class Book:
    def __init__(self, book_id, title, author, year_published, copies_left):
        # Initialize book attributes: book ID, title, author, year published, and number of copies left
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year_published = year_published
        self.copies_left = copies_left
    def __str__(self):
        # Return a string representation of the book
        return (f"book id : {self.book_id},title : {self.title},author : {self.author},year published : {self.year_published}, copies left : {self.copies_left}")
# Define a Library class to manage students and books
class Library:
    def __init__(self):
        # Initialize library attributes: dictionaries to store books and students
        self.books = {}  # dictionary to store book titles as keys and quantities as values
        self.students = {}  # dictionary to store student IDs as keys and borrowed books as values
    def add_book(self, title, quantity):
        # Add a book to the library or update its quantity if it already exists
        if title in self.books:
            self.books[title] += quantity
        else:
            self.books[title] = quantity
    def add_student(self, student_id):
        # Add a student to the library
        self.students[student_id] = []
    def borrow_book(self, student_id, book_title):
        # Allow a student to borrow a book if it's available and they haven't already borrowed 3 books
        if book_title in self.books and self.books[book_title] > 0:
            if student_id in self.students and len(self.students[student_id]) < 3:
                self.books[book_title] -= 1
                self.students[student_id].append(book_title)
                print(f"Book '{book_title}' borrowed by student {student_id}")
            else:
                print("Student has already borrowed 3 books or is not registered")
        else:
            print("Book is not available or out of stock")
    def return_book(self, student_id, book_title):
        # Allow a student to return a book they've borrowed
        if student_id in self.students and book_title in self.students[student_id]:
            self.students[student_id].remove(book_title)
            self.books[book_title] += 1
            print(f"Book '{book_title}' returned by student {student_id}")
        else:
            print("Student has not borrowed this book or is not registered")
    def display_library(self):
        # Display the current state of the library
        print("Books in the library:")
        for title, quantity in self.books.items():
            print(f"{title}: {quantity}")
        print("Students and their borrowed books:")
        for student_id, books in self.students.items():
            print(f"Student {student_id}: {', '.join(books)}")