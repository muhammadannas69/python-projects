# Password Validator

This is a simple Python program that checks whether a password is strong based on common security rules.

The program validates the password step by step. If any rule is not satisfied, it raises a custom exception and displays a clear error message.

## Features

- Minimum 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character
- Uses custom exceptions
- Handles errors with `try-except`

## Concepts Used

- Custom Exceptions
- `raise`
- `try-except`
- Loops
- Conditional Statements
- String Methods

## How to Run

```bash
python task_03_password_validator.py
```

## Example

```
Enter Password: Hello123

Password must contain at least one special character.
```

```
Enter Password: Hello@123

Password is valid.
```

## Author

**Muhammad Annas**