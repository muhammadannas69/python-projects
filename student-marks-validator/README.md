# Student Marks Validator

This is a simple Python program that validates marks for five subjects using custom exceptions.

The program asks the user to enter marks for each subject. If a mark is less than 0 or greater than 100, it raises a custom exception and asks the user to enter that mark again. After all valid marks are entered, it calculates the total, average, and final grade.

## Features

- Enter marks for 5 subjects
- Validate marks between 0 and 100
- Custom exception for invalid marks
- Re-enter only the invalid mark
- Calculate total and average
- Display the final grade
- Handle invalid input using `try-except`

## Concepts Used

- Dictionaries
- Loops
- Custom Exceptions
- `raise`
- `try-except`
- Input Validation
- Conditional Statements

## How to Run

```bash
python task_02_student_marks_validator.py
```

## Example

```
Enter English marks: 85
Enter Math marks: 90
Enter Science marks: 120
Invalid marks! Please enter marks between 0 and 100.
Enter Science marks again: 95
Enter Biology marks: 80
Enter Physics marks: 75

Total: 425
Average: 85.0
Grade: B
```

## Author

**Muhammad Annas**