"""
main.py - Demonstration script for the python utility module.
Tests and displays results for every function defined in utils.py.
"""

import os
import sys

# ensure utf-8 console output for special symbols like ₹ on Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from utils import (
    is_valid_email,
    is_valid_phone,
    is_strong_password,
    is_valid_age,
    format_name,
    format_currency,
    format_date,
    truncate_text,
    calculate_average,
    calculate_percentage,
    calculate_simple_interest,
    find_max_min,
    read_file,
    write_file,
    append_to_file,
    count_words_in_file,
    file_exists
)


def run_validation_demo():
    print("=" * 60)
    print("--- 1. Validation Utilities Demo ---")
    print("=" * 60)

    # 1. Email validation
    test_emails = [
        "student.intern@example.com",
        "invalid_email_at_domain",
        "user@sub.domain.co.in"
    ]
    print("\n[is_valid_email]")
    for email in test_emails:
        result = is_valid_email(email)
        print(f"  Input: {email:<30} -> Valid: {result}")

    # 2. Indian Phone number validation
    test_phones = [
        "9876543210",
        "+91 8123456789",
        "5432109876",  # invalid: starts with 5
        "98765"         # invalid: too short
    ]
    print("\n[is_valid_phone] (10-digit Indian Mobile Numbers)")
    for phone in test_phones:
        result = is_valid_phone(phone)
        print(f"  Input: {phone:<25} -> Valid: {result}")

    # 3. Strong password check
    test_passwords = [
        "Weak123",
        "StrongPass@2026",
        "alllowercase#1",
        "N0SpecialCharHere"
    ]
    print("\n[is_strong_password]")
    for pwd in test_passwords:
        result = is_strong_password(pwd)
        print(f"  Input: {pwd:<25} -> Strong: {result}")

    # 4. Age validation
    test_ages = [21, "35", -4, 150, "twenty"]
    print("\n[is_valid_age] (0 to 120)")
    for age in test_ages:
        result = is_valid_age(age)
        print(f"  Input: {str(age):<15} -> Valid: {result}")


def run_formatting_demo():
    print("\n" + "=" * 60)
    print("--- 2. Formatting Utilities Demo ---")
    print("=" * 60)

    # 1. Name formatting
    test_names = [
        "  aarav   sharma  ",
        "priya NAIR",
        "vikramaditya"
    ]
    print("\n[format_name]")
    for name in test_names:
        result = format_name(name)
        print(f"  Input: '{name}'\n  Output: '{result}'\n")

    # 2. Currency formatting (Indian Rupees)
    test_amounts = [500, 15000, 1250000, 8765432.75, -2500]
    print("[format_currency]")
    for amt in test_amounts:
        result = format_currency(amt)
        print(f"  Input: {str(amt):<15} -> Formatted: {result}")

    # 3. Date formatting
    test_dates = [
        "2026-10-25",
        "2026/12/31",
        "15/08/2024"
    ]
    print("\n[format_date] (Output format: DD-MM-YYYY)")
    for d in test_dates:
        result = format_date(d)
        print(f"  Input: {d:<15} -> Formatted: {result}")

    # 4. Text truncation
    test_texts = [
        ("Learning modular Python programming is fun and useful.", 30),
        ("Short note", 20),
        ("A very long sentence that needs to be shortened for a preview card.", 35)
    ]
    print("\n[truncate_text]")
    for text, max_len in test_texts:
        result = truncate_text(text, max_len)
        print(f"  Max length: {max_len}")
        print(f"  Original : '{text}'")
        print(f"  Truncated: '{result}'\n")


def run_calculation_demo():
    print("=" * 60)
    print("--- 3. Calculation Utilities Demo ---")
    print("=" * 60)

    # 1. Average
    sample_scores = [85, 92, 78, 90, 88]
    avg_result = calculate_average(sample_scores)
    print(f"\n[calculate_average]")
    print(f"  Scores: {sample_scores}")
    print(f"  Average Score: {avg_result}")

    # 2. Percentage
    marks_obtained = 465
    total_marks = 500
    pct = calculate_percentage(marks_obtained, total_marks)
    print(f"\n[calculate_percentage]")
    print(f"  Obtained: {marks_obtained} / Total: {total_marks}")
    print(f"  Percentage: {pct}%")

    # 3. Simple interest
    principal = 50000
    rate = 7.5
    time_years = 3
    si = calculate_simple_interest(principal, rate, time_years)
    print(f"\n[calculate_simple_interest]")
    print(f"  Principal: ₹{principal}, Rate: {rate}%, Time: {time_years} years")
    print(f"  Calculated Interest: ₹{si}")

    # 4. Max and min
    number_list = [42, 17, 89, 3, 56, -10, 72]
    max_val, min_val = find_max_min(number_list)
    print(f"\n[find_max_min]")
    print(f"  Numbers: {number_list}")
    print(f"  Maximum: {max_val}, Minimum: {min_val}")


def run_file_demo():
    print("\n" + "=" * 60)
    print("--- 4. File Utilities Demo ---")
    print("=" * 60)

    # Base path for files
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sample_file = os.path.join(current_dir, "sample_data.txt")
    output_file = os.path.join(current_dir, "demo_output.txt")

    # 1. Check if sample file exists
    print(f"\n[file_exists]")
    exists = file_exists(sample_file)
    print(f"  Checking '{os.path.basename(sample_file)}': {exists}")

    # 2. Read sample file
    print(f"\n[read_file]")
    content = read_file(sample_file)
    print("  File content preview:")
    for line in content.strip().split("\n"):
        print(f"    | {line}")

    # 3. Word count
    print(f"\n[count_words_in_file]")
    words = count_words_in_file(sample_file)
    print(f"  Total word count in '{os.path.basename(sample_file)}': {words} words")

    # 4. Write to a new demo file
    print(f"\n[write_file]")
    initial_note = "Internship Task: Python Utility Module\nStatus: Started testing file utilities.\n"
    written = write_file(output_file, initial_note)
    print(f"  Writing to '{os.path.basename(output_file)}': {'Success' if written else 'Failed'}")

    # 5. Append to the demo file
    print(f"\n[append_to_file]")
    append_note = "Status Update: All utilities executed and verified successfully!\n"
    appended = append_to_file(output_file, append_note)
    print(f"  Appending to '{os.path.basename(output_file)}': {'Success' if appended else 'Failed'}")

    # 6. Verify written output
    print(f"\n[Verification of Created File]")
    final_output = read_file(output_file)
    final_word_count = count_words_in_file(output_file)
    print(f"  Content in '{os.path.basename(output_file)}':")
    for line in final_output.strip().split("\n"):
        print(f"    | {line}")
    print(f"  Word count in new file: {final_word_count} words")


if __name__ == "__main__":
    print("\n" + "#" * 60)
    print("     PYTHON UTILITY MODULE - DEMONSTRATION RUN")
    print("#" * 60 + "\n")

    run_validation_demo()
    run_formatting_demo()
    run_calculation_demo()
    run_file_demo()

    print("\n" + "#" * 60)
    print("     ALL UTILITY DEMONSTRATIONS COMPLETED SUCCESSFULLY")
    print("#" * 60 + "\n")
