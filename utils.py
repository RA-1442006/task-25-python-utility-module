"""
utils.py - A reusable Python utility module for common tasks.
Contains validation, formatting, calculation, and file utilities.
"""

import os
import re
from datetime import datetime, date


# ==========================================
# 1. VALIDATION UTILITIES
# ==========================================

def is_valid_email(email):
    """
    Checks whether the given email address has a valid format.

    Parameters:
        email (str): The email string to validate.

    Returns:
        bool: True if the email format is valid, False otherwise.

    Example:
        is_valid_email("student@example.com") -> True
        is_valid_email("invalid-email") -> False
    """
    # check for empty or non-string input
    if not isinstance(email, str) or not email.strip():
        return False

    email = email.strip()
    # simple regex pattern for general email validation
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))


def is_valid_phone(phone):
    """
    Checks if a phone number is a valid 10-digit Indian mobile number.
    Accepts numbers starting with 6, 7, 8, or 9. Also cleans up '+91' or leading '0'.

    Parameters:
        phone (str or int): The phone number to validate.

    Returns:
        bool: True if it is a valid 10-digit Indian number, False otherwise.

    Example:
        is_valid_phone("9876543210") -> True
        is_valid_phone("+91 9876543210") -> True
        is_valid_phone("1234567890") -> False
    """
    # handle None or empty input
    if phone is None:
        return False

    # convert to string and remove spaces and hyphens
    text = str(phone).strip().replace(" ", "").replace("-", "")

    # strip international prefix or leading trunk zero if present
    if text.startswith("+91"):
        text = text[3:]
    elif text.startswith("91") and len(text) == 12:
        text = text[2:]
    elif text.startswith("0") and len(text) == 11:
        text = text[1:]

    # indian mobile numbers have exactly 10 digits and start with 6, 7, 8, or 9
    if len(text) == 10 and text.isdigit() and text[0] in "6789":
        return True

    return False


def is_strong_password(password):
    """
    Validates if a password meets basic security standards:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    - Contains at least one special character

    Parameters:
        password (str): The password string to check.

    Returns:
        bool: True if strong password, False otherwise.

    Example:
        is_strong_password("Admin@1234") -> True
        is_strong_password("weakpass") -> False
    """
    if not isinstance(password, str):
        return False

    # check minimum length
    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    # inspect each character
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    return has_upper and has_lower and has_digit and has_special


def is_valid_age(age):
    """
    Validates whether the provided age is a realistic human age (0 to 120).

    Parameters:
        age (int or str): Age value to validate.

    Returns:
        bool: True if age is valid, False otherwise.

    Example:
        is_valid_age(21) -> True
        is_valid_age("25") -> True
        is_valid_age(-5) -> False
    """
    try:
        # convert string or float to integer
        num = int(age)
        return 0 <= num <= 120
    except (ValueError, TypeError):
        return False


# ==========================================
# 2. FORMATTING UTILITIES
# ==========================================

def format_name(name):
    """
    Trims extra spaces and converts a name to proper Title Case.

    Parameters:
        name (str): Raw name string.

    Returns:
        str: Cleaned and title-cased name.

    Example:
        format_name("   rahul   kumar  ") -> "Rahul Kumar"
    """
    if not isinstance(name, str):
        return ""

    # remove excess whitespace between words and format to title case
    words = name.strip().split()
    return " ".join(words).title()


def format_currency(amount):
    """
    Formats a numeric amount as Indian Rupees (₹) with proper comma grouping.
    Follows the Indian numbering system (e.g., 1,50,000.00).

    Parameters:
        amount (int or float): The amount to format.

    Returns:
        str: Formatted currency string with ₹ symbol.

    Example:
        format_currency(150000) -> "₹1,50,000.00"
        format_currency(2500.5) -> "₹2,500.50"
    """
    try:
        num = float(amount)
    except (ValueError, TypeError):
        return "₹0.00"

    is_negative = num < 0
    num = abs(num)

    # split into integer and decimal parts
    parts = f"{num:.2f}".split(".")
    int_part = parts[0]
    dec_part = parts[1]

    # indian format groups last 3 digits, then pairs of 2
    if len(int_part) <= 3:
        formatted_int = int_part
    else:
        last_three = int_part[-3:]
        remaining = int_part[:-3]
        groups = []
        while len(remaining) > 2:
            groups.append(remaining[-2:])
            remaining = remaining[:-2]
        if remaining:
            groups.append(remaining)
        groups.reverse()
        formatted_int = ",".join(groups) + "," + last_three

    sign = "-" if is_negative else ""
    return f"{sign}₹{formatted_int}.{dec_part}"


def format_date(date_input):
    """
    Converts a date string or date object into standard DD-MM-YYYY format.
    Accepts YYYY-MM-DD, YYYY/MM/DD, DD/MM/YYYY, or date/datetime objects.

    Parameters:
        date_input (str, date, or datetime): Input date to format.

    Returns:
        str: Formatted date string in DD-MM-YYYY format, or empty string if invalid.

    Example:
        format_date("2026-10-25") -> "25-10-2026"
    """
    if not date_input:
        return ""

    # if already a datetime/date object
    if isinstance(date_input, (date, datetime)):
        return date_input.strftime("%d-%m-%Y")

    date_str = str(date_input).strip()
    supported_formats = ["%Y-%m-%d", "%Y/%m/%d", "%d/%m/%Y", "%d-%m-%Y"]

    for fmt in supported_formats:
        try:
            parsed = datetime.strptime(date_str, fmt)
            return parsed.strftime("%d-%m-%Y")
        except ValueError:
            continue

    # return empty string if no format matched
    return ""


def truncate_text(text, max_len=30):
    """
    Truncates a string to max_len characters and appends '...' if truncated.

    Parameters:
        text (str): The original text.
        max_len (int): Maximum length of the returned string including '...'.

    Returns:
        str: Truncated string with ellipsis if needed, or original string.

    Example:
        truncate_text("Python is a powerful language", 15) -> "Python is a..."
    """
    if not isinstance(text, str):
        return ""

    if max_len <= 3:
        return text[:max_len]

    if len(text) > max_len:
        return text[:max_len - 3] + "..."

    return text


# ==========================================
# 3. CALCULATION UTILITIES
# ==========================================

def calculate_average(numbers):
    """
    Computes the arithmetic average of a list or tuple of numbers.

    Parameters:
        numbers (list or tuple): Collection of numeric values.

    Returns:
        float: Calculated average rounded to 2 decimal places, or 0.0 if empty.

    Example:
        calculate_average([10, 20, 30, 40]) -> 25.0
    """
    if not numbers or not isinstance(numbers, (list, tuple)):
        return 0.0

    try:
        total = sum(numbers)
        avg = total / len(numbers)
        return round(avg, 2)
    except TypeError:
        # non-numeric element found in list
        return 0.0


def calculate_percentage(obtained, total):
    """
    Calculates the percentage from obtained marks and total marks.

    Parameters:
        obtained (int or float): Obtained score or value.
        total (int or float): Total possible score or value.

    Returns:
        float: Percentage rounded to 2 decimal places.

    Example:
        calculate_percentage(450, 500) -> 90.0
    """
    try:
        obtained = float(obtained)
        total = float(total)
        if total <= 0:
            return 0.0
        pct = (obtained / total) * 100
        return round(pct, 2)
    except (ValueError, TypeError, ZeroDivisionError):
        return 0.0


def calculate_simple_interest(principal, rate, time):
    """
    Calculates simple interest based on the formula: SI = (P * R * T) / 100.

    Parameters:
        principal (int or float): Principal amount borrowed or invested.
        rate (int or float): Annual interest rate as a percentage.
        time (int or float): Time period in years.

    Returns:
        float: Simple interest amount rounded to 2 decimal places.

    Example:
        calculate_simple_interest(10000, 7.5, 2) -> 1500.0
    """
    try:
        p = float(principal)
        r = float(rate)
        t = float(time)
        if p < 0 or r < 0 or t < 0:
            return 0.0
        interest = (p * r * t) / 100
        return round(interest, 2)
    except (ValueError, TypeError):
        return 0.0


def find_max_min(numbers):
    """
    Finds the maximum and minimum numbers from a list or tuple.

    Parameters:
        numbers (list or tuple): Collection of numeric values.

    Returns:
        tuple: (max_value, min_value) or (None, None) if list is invalid or empty.

    Example:
        find_max_min([15, 3, 99, 42, -5]) -> (99, -5)
    """
    if not numbers or not isinstance(numbers, (list, tuple)):
        return (None, None)

    try:
        return (max(numbers), min(numbers))
    except (ValueError, TypeError):
        return (None, None)


# ==========================================
# 4. FILE UTILITIES
# ==========================================

def read_file(filepath):
    """
    Reads and returns the contents of a text file safely.

    Parameters:
        filepath (str): Path to the file to read.

    Returns:
        str: File contents as string, or empty string if file cannot be read.

    Example:
        read_file("data.txt") -> "Hello World"
    """
    if not filepath or not isinstance(filepath, str):
        return ""

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except (FileNotFoundError, PermissionError, OSError):
        return ""


def write_file(filepath, content):
    """
    Writes text content to a file, replacing any existing content.

    Parameters:
        filepath (str): Path to the destination file.
        content (str): Text content to write.

    Returns:
        bool: True if writing succeeded, False otherwise.

    Example:
        write_file("output.txt", "Some text") -> True
    """
    if not filepath or not isinstance(filepath, str):
        return False

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(str(content))
        return True
    except (PermissionError, OSError):
        return False


def append_to_file(filepath, content):
    """
    Appends text content to the end of an existing file.

    Parameters:
        filepath (str): Path to the file.
        content (str): Text content to append.

    Returns:
        bool: True if append succeeded, False otherwise.

    Example:
        append_to_file("log.txt", "New entry\n") -> True
    """
    if not filepath or not isinstance(filepath, str):
        return False

    try:
        with open(filepath, "a", encoding="utf-8") as f:
            f.write(str(content))
        return True
    except (PermissionError, OSError):
        return False


def count_words_in_file(filepath):
    """
    Counts the total number of words in a text file.

    Parameters:
        filepath (str): Path to the text file.

    Returns:
        int: Number of words in the file, or 0 if file is missing or empty.

    Example:
        count_words_in_file("notes.txt") -> 120
    """
    text = read_file(filepath)
    if not text:
        return 0

    words = text.split()
    return len(words)


def file_exists(filepath):
    """
    Checks if a file exists at the specified path.

    Parameters:
        filepath (str): Path to check.

    Returns:
        bool: True if the file exists and is a regular file, False otherwise.

    Example:
        file_exists("data.txt") -> True
    """
    if not filepath or not isinstance(filepath, str):
        return False

    return os.path.isfile(filepath)
