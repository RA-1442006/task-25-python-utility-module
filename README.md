# Python Utility Module

A reusable, modular Python utility library created as an internship project. The module provides commonly needed helper functions for data validation, string and currency formatting, numerical calculations, and file operations.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Objective](#objective)
- [Approach](#approach)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
- [Function Documentation](#function-documentation)
  - [1. Validation Utilities](#1-validation-utilities)
  - [2. Formatting Utilities](#2-formatting-utilities)
  - [3. Calculation Utilities](#3-calculation-utilities)
  - [4. File Utilities](#4-file-utilities)
- [Sample Execution Output](#sample-execution-output)
- [Outcome and Key Learnings](#outcome-and-key-learnings)

---

## Project Overview

In software development, applications frequently need repetitive operations such as validating user inputs, formatting display text or currency, performing arithmetic calculations, and interacting with the local filesystem. 

Rather than rewriting this logic across multiple scripts, this project encapsulates these functions into a single, clean module named `utils.py`. The companion script `main.py` demonstrates and tests each utility function.

---

## Objective

- **Learn Modular Programming**: Break down complex programming problems into independent, reusable functional units.
- **Practice Code Reuse**: Import functions into different scripts without copying and pasting logic.
- **Implement Defensive Programming**: Add basic error handling for empty inputs, missing files, and incorrect data types.
- **Maintain Clean Code Standards**: Write clear docstrings, single-responsibility functions, and readable, human-friendly code.

---

## Approach

1. **Separation of Concerns**: Each function has exactly one clear responsibility with self-descriptive naming.
2. **Defensive Error Handling**: Functions handle `None`, empty strings, wrong data types, and missing files gracefully instead of crashing.
3. **Beginner-Friendly and Natural Style**:
   - Clean, standard variable names (`result`, `count`, `total`, `text`).
   - Plain English, casual comments explaining logic.
   - Avoids unnecessary decorators, overly complex OOP patterns, or rigid type annotations to keep the code lightweight and approachable.
4. **Platform Compatibility**: Includes standard UTF-8 console output support for special characters such as the Indian Rupee symbol (`₹`).

---

## Project Structure

```text
python_utility_module/
│
├── utils.py             # The core reusable utility module containing 17 helper functions
├── main.py              # Demonstration script importing and executing all functions
├── sample_data.txt      # Input text file used to test file-handling functions
├── sample_output.txt    # Actual terminal output produced by running main.py
├── .gitignore           # Git ignore configuration for bytecode and temporary files
└── README.md            # Comprehensive project documentation
```

---

## How to Run

### Prerequisites
- Python 3.7 or higher installed on your system.

### Steps

1. **Open a Terminal / Command Prompt** (or use the built-in terminal in VS Code).
2. **Navigate to the project directory**:
   ```bash
   cd C:\Users\<your-username>\Desktop\python_utility_module
   ```
3. **Run the demonstration script**:
   ```bash
   python main.py
   ```
4. **View Output**:
   The demonstration script will display formatted section headers and outputs for validation, formatting, calculation, and file utility tests.

---

## Function Documentation

### 1. Validation Utilities

#### `is_valid_email(email)`
- **Purpose**: Checks whether an email address matches a standard email format using regular expressions.
- **Parameters**: `email` (*str*) - The email address string to validate.
- **Return Value**: `bool` - `True` if valid, `False` otherwise.
- **Example**:
  ```python
  is_valid_email("student@example.com")  # Returns True
  is_valid_email("invalid_email")        # Returns False
  ```

#### `is_valid_phone(phone)`
- **Purpose**: Validates whether a phone number is a 10-digit Indian mobile number (starts with 6, 7, 8, or 9). Cleans up optional `+91` or leading `0` prefixes.
- **Parameters**: `phone` (*str or int*) - The phone number to test.
- **Return Value**: `bool` - `True` if valid 10-digit Indian number, `False` otherwise.
- **Example**:
  ```python
  is_valid_phone("9876543210")       # Returns True
  is_valid_phone("+91 9876543210")   # Returns True
  is_valid_phone("1234567890")       # Returns False
  ```

#### `is_strong_password(password)`
- **Purpose**: Verifies that a password meets strength requirements: minimum 8 characters, at least one uppercase letter, one lowercase letter, one digit, and one special character.
- **Parameters**: `password` (*str*) - The password string to evaluate.
- **Return Value**: `bool` - `True` if strong, `False` otherwise.
- **Example**:
  ```python
  is_strong_password("SecurePass#2026")  # Returns True
  is_strong_password("weak")             # Returns False
  ```

#### `is_valid_age(age)`
- **Purpose**: Checks whether the given age is a realistic human age between 0 and 120 (inclusive).
- **Parameters**: `age` (*int or str*) - The age to validate.
- **Return Value**: `bool` - `True` if within 0–120, `False` otherwise.
- **Example**:
  ```python
  is_valid_age(21)      # Returns True
  is_valid_age("35")    # Returns True
  is_valid_age(-4)      # Returns False
  ```

---

### 2. Formatting Utilities

#### `format_name(name)`
- **Purpose**: Trims leading, trailing, and excessive internal whitespace, and converts the name into Title Case.
- **Parameters**: `name` (*str*) - Raw name string.
- **Return Value**: `str` - Cleaned, capitalized name.
- **Example**:
  ```python
  format_name("   rahul   kumar  ")  # Returns "Rahul Kumar"
  ```

#### `format_currency(amount)`
- **Purpose**: Formats a number as Indian Rupees (`₹`) using standard Indian comma grouping (lakhs and crores, e.g., `₹1,50,000.00`).
- **Parameters**: `amount` (*int or float*) - The monetary amount.
- **Return Value**: `str` - Formatted currency string with `₹` symbol.
- **Example**:
  ```python
  format_currency(150000)     # Returns "₹1,50,000.00"
  format_currency(2500.5)     # Returns "₹2,500.50"
  ```

#### `format_date(date_input)`
- **Purpose**: Converts date strings (in `YYYY-MM-DD`, `YYYY/MM/DD`, etc.) or Python `date`/`datetime` objects into standard `DD-MM-YYYY` format.
- **Parameters**: `date_input` (*str, date, or datetime*) - Date to format.
- **Return Value**: `str` - Date string formatted as `DD-MM-YYYY`, or empty string if invalid.
- **Example**:
  ```python
  format_date("2026-10-25")  # Returns "25-10-2026"
  ```

#### `truncate_text(text, max_len=30)`
- **Purpose**: Shortens a text string if it exceeds `max_len` and appends an ellipsis (`...`).
- **Parameters**: 
  - `text` (*str*) - Original text.
  - `max_len` (*int*, default 30) - Maximum allowed length including the ellipsis.
- **Return Value**: `str` - Truncated string or original text if already within limit.
- **Example**:
  ```python
  truncate_text("Python is a powerful language", 15)  # Returns "Python is a..."
  ```

---

### 3. Calculation Utilities

#### `calculate_average(numbers)`
- **Purpose**: Computes the arithmetic average (mean) of a list or tuple of numbers.
- **Parameters**: `numbers` (*list or tuple*) - Numerical elements.
- **Return Value**: `float` - Mean rounded to 2 decimal places (or `0.0` if empty/invalid).
- **Example**:
  ```python
  calculate_average([10, 20, 30, 40])  # Returns 25.0
  ```

#### `calculate_percentage(obtained, total)`
- **Purpose**: Computes percentage based on obtained marks and total marks.
- **Parameters**:
  - `obtained` (*int or float*) - Score obtained.
  - `total` (*int or float*) - Maximum score possible.
- **Return Value**: `float` - Percentage rounded to 2 decimal places.
- **Example**:
  ```python
  calculate_percentage(450, 500)  # Returns 90.0
  ```

#### `calculate_simple_interest(principal, rate, time)`
- **Purpose**: Calculates simple interest using the standard formula $SI = \frac{P \times R \times T}{100}$.
- **Parameters**:
  - `principal` (*int or float*) - Principal amount.
  - `rate` (*int or float*) - Annual interest rate (%).
  - `time` (*int or float*) - Time period in years.
- **Return Value**: `float` - Calculated interest rounded to 2 decimal places.
- **Example**:
  ```python
  calculate_simple_interest(10000, 7.5, 2)  # Returns 1500.0
  ```

#### `find_max_min(numbers)`
- **Purpose**: Finds the maximum and minimum values in a sequence of numbers.
- **Parameters**: `numbers` (*list or tuple*) - Collection of numbers.
- **Return Value**: `tuple` - `(max_value, min_value)` or `(None, None)` if empty.
- **Example**:
  ```python
  find_max_min([15, 3, 99, 42, -5])  # Returns (99, -5)
  ```

---

### 4. File Utilities

#### `read_file(filepath)`
- **Purpose**: Reads and returns the entire content of a UTF-8 text file.
- **Parameters**: `filepath` (*str*) - Path to the target file.
- **Return Value**: `str` - Content of file, or empty string if file does not exist or cannot be read.
- **Example**:
  ```python
  read_file("sample_data.txt")  # Returns text contents
  ```

#### `write_file(filepath, content)`
- **Purpose**: Creates or overwrites a text file with the provided content.
- **Parameters**:
  - `filepath` (*str*) - Target file path.
  - `content` (*str*) - Text to write.
- **Return Value**: `bool` - `True` if writing succeeded, `False` otherwise.
- **Example**:
  ```python
  write_file("notes.txt", "First note.")  # Returns True
  ```

#### `append_to_file(filepath, content)`
- **Purpose**: Appends new text to the end of an existing file.
- **Parameters**:
  - `filepath` (*str*) - Target file path.
  - `content` (*str*) - Text to append.
- **Return Value**: `bool` - `True` if append succeeded, `False` otherwise.
- **Example**:
  ```python
  append_to_file("notes.txt", "\nSecond note.")  # Returns True
  ```

#### `count_words_in_file(filepath)`
- **Purpose**: Counts the total word count in a text file based on whitespace separation.
- **Parameters**: `filepath` (*str*) - Path to the file.
- **Return Value**: `int` - Total words, or `0` if empty or missing.
- **Example**:
  ```python
  count_words_in_file("sample_data.txt")  # Returns 45
  ```

#### `file_exists(filepath)`
- **Purpose**: Checks whether a file exists at the given path and is a regular file.
- **Parameters**: `filepath` (*str*) - Path to verify.
- **Return Value**: `bool` - `True` if file exists, `False` otherwise.
- **Example**:
  ```python
  file_exists("sample_data.txt")  # Returns True
  ```

---

## Sample Execution Output

The complete output from executing `python main.py` is captured in [`sample_output.txt`](./sample_output.txt). Below is a summary excerpt:

```text
############################################################
     PYTHON UTILITY MODULE - DEMONSTRATION RUN
############################################################

============================================================
--- 1. Validation Utilities Demo ---
============================================================
[is_valid_email]
  Input: student.intern@example.com     -> Valid: True
  Input: invalid_email_at_domain        -> Valid: False

[is_valid_phone] (10-digit Indian Mobile Numbers)
  Input: 9876543210                -> Valid: True
  Input: +91 8123456789            -> Valid: True

...

============================================================
--- 2. Formatting Utilities Demo ---
============================================================
[format_name]
  Input: '  aarav   sharma  '
  Output: 'Aarav Sharma'

[format_currency]
  Input: 150000           -> Formatted: ₹1,50,000.00
  Input: 1250000         -> Formatted: ₹12,50,000.00

...
############################################################
     ALL UTILITY DEMONSTRATIONS COMPLETED SUCCESSFULLY
############################################################
```

---

## Outcome and Key Learnings

1. **Modular Architecture**: Demonstrated how dividing functionality into self-contained modules improves maintainability, unit testability, and code organization.
2. **Reusability**: `utils.py` functions can be imported into any future Python project with `from utils import ...`.
3. **Robust Input Handling**: Handled edge cases such as missing parameters, negative numbers, divide-by-zero scenarios, and missing filesystem paths.
4. **Documentation Skills**: Practiced writing structured docstrings and README documentation that allow any teammate to immediately understand and use the module.
