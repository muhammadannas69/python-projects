# Library Management System

This is a simple Python-based Library Management System.

The program allows the user to add books, borrow books, and return books. Book information such as book ID, title, author, and quantity is stored in a dictionary.

## Features

- Add a new book
- Borrow books
- Return books
- Check book availability
- Prevent duplicate book IDs
- Handle invalid book IDs
- Validate book quantity
- Handle invalid user input
- Use exception handling for errors

## Concepts Used

- Dictionaries
- Lists
- While Loop
- `if-else`
- `try-except`
- `raise`
- Input Validation
- Dictionary indexing

## How to Run

```bash
python library_management_system.py
```

## Example

```text
Library Management System

1. Add book
2. Borrow Book
3. Return Book
4. Exit

Enter option: 1

Enter book ID: 101
Enter book title: Python Basics
Enter author name: John
Enter quantity: 5
```

After adding the book, users can borrow or return copies using the book ID.

## Data Structure

Book information is stored in a dictionary:

```python
library = {
    101: ["Python Basics", "John", 5]
}
```

Here:

- `101` → Book ID
- `"Python Basics"` → Book Title
- `"John"` → Author
- `5` → Quantity
