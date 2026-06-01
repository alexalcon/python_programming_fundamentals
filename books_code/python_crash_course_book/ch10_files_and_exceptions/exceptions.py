""" 
File: exceptions.py
Author: Alex Alcón
GitHub: https://github.com/alexalcon
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Description: 
    
    3. Exceptions
        3.1 Handling the ZeroDivisionError Exception
        3.2 Using try-except Blocks
        3.3 Using Exceptions to Prevent Crashes
        3.4 The else Block
        3.5 Handling the FileNotFoundError Exception
        3.6 Analyzing Text
        3.7 Working with Multiple Files
        3.8 Failing Silently
        3.9 Deciding Which Errors to Report
Created on: 27-05-2026
"""

from pathlib import Path

def load_price_file(path):
    """Load prices from a text file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # print(f"  Warning: {path} not found, skipping.")
        pass  # silently skip missing files
    else:
        lines = contents.splitlines()
        print(f"  Loaded {len(lines)} records from {path}")


# ───────────────────────────────────────
# 3.3 Using Exceptions to Prevent Crashes
# ───────────────────────────────────────
print("\n───────────────────────────────────────")
print("3.3 Using Exceptions to Prevent Crashes")
print("───────────────────────────────────────")

prices = [175.50, 180.00, 0, 300.00, 310.00]
returns = []

for i in range(1, len(prices)):
    try:
        daily_return = (prices[i] - prices[i - 1]) / prices[i - 1]
    except ZeroDivisionError:
        print(f"Skipping index {i}: division by zero")
        daily_return = 0.0
    returns.append(round(daily_return, 4))

print(f"Daily returns: {returns}")

# ──────────────────
# 3.4 The else Block
# ──────────────────
print("\n──────────────────")
print("3.4 The else Block")
print("──────────────────")

print("Portfolio return calculator")
print("Enter 'q' to quit.\n")

while True:
    pnl = input("PnL ($): ")
    if pnl == 'q':
        break
    capital = input("Capital ($): ")
    if capital == 'q':
        break
    try:
        result = float(pnl) / float(capital)
    except ZeroDivisionError:
        print("  Error: capital cannot be zero.")
    except ValueError:
        print("  Error: please enter numeric values.")
    else:
        print(f"  Return: {result:.2%}\n")

# ────────────────────────────────────────────
# 3.5 Handling the FileNotFoundError Exception
# ────────────────────────────────────────────
"""
Using the str splitlines() method to analyze a file's
contents as lines from the file.
"""
print("\n────────────────────────────────────────────")
print("3.5 Handling the FileNotFoundError Exception")
print("────────────────────────────────────────────")

path = Path('daily_prices.txt')

try:
    contents = path.read_text(encoding='utf-8') 
except FileNotFoundError:
    print(f"Error: the file {path} does not exist.")
else:
    lines = contents.splitlines()
    print(f"Loaded {len(lines)} lines from {path}")

# ──────────────────
# 3.6 Analyzing Text
# ──────────────────
"""
Using the str split() method to analyze a file's
contents as words from the file.
"""
print("\n──────────────────")
print("3.6 Analyzing Text")
print("──────────────────")

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Error: the file {path} does not exist.")
else:
    words = contents.split()
    print(f"{path} contains about {len(words)} words.")

# ───────────────────────────────
# 3.7 Working with Multiple Files
# ───────────────────────────────
print("\n───────────────────────────────")
print("3.7 Working with Multiple Files")
print("───────────────────────────────")

filenames = ['daily_prices.txt', 'closing_prices.txt',
             'missing_data.txt', 'trade_log.txt']

for filename in filenames:
    path = Path(filename)
    load_price_file(path)