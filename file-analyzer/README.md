# File Analyzer

This is a simple Python program that reads a text file and displays basic information about it.

The program asks the user for a filename, reads the file, and displays the total number of lines, words, and characters. It also handles common file-related errors using exception handling.

## Features

- Read a text file
- Count the number of lines
- Count the number of words
- Count the number of characters
- Handle file not found errors
- Handle permission denied errors
- Detect an empty file
- Use `try-except` for exception handling

## Concepts Used

- File Handling
- `with open()`
- `try-except`
- Custom Error Handling
- String Methods
- Conditional Statements

## How to Run

```bash
python file_analyzer.py
```

## Example

```
Enter a file name: notes.txt

Lines: 8
Words: 54
Characters: 312
```

### Empty File

```
Enter a file name: empty.txt

File is empty.
```

## Author

**Muhammad Annas**