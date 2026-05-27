""" 
File: reading_from_a_file.py
Author: Alex Alcón
GitHub: https://github.com/alexalcon
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Description: 
    
    1. Reading from a File
        1.1 Reading the Contents of a File
        1.2 Relative and Absolute File Paths
        1.3 Accessing a File's Lines
        1.4 Working with a File's Contents
        1.5 Large Files
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Created on: 26-05-2026
"""

from pathlib import Path

# ──────────────────────────────────
# 1.1 Reading the Contents of a File
# ──────────────────────────────────
"""
Using pathlib to read a file's contents:

    - The `read_text()` method reads the entire file as a string.
    - The `rstrip()` method is used to remove any trailing whitespace, 
      including the newline character.
    - Applying rstrip() immediately after read_text() is called method 
      chaining. 

"""
path_daily_prices = Path("./daily_prices.txt")
daily_prices = path_daily_prices.read_text().rstrip()
print(daily_prices)

# ────────────────────────────
# 1.3 Accessing a File's Lines
# ────────────────────────────
path_closing_prices = Path("./closing_prices.txt")
closing_prices = path_closing_prices.read_text()
lines_closing_prices = closing_prices.splitlines()
for line in range(len(lines_closing_prices)):
    print(lines_closing_prices[line])