""" 
File: writing_to_a_file.py
Author: Alex Alcón
GitHub: https://github.com/alexalcon
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Description: 
    
    2. Writing to a File
        2.1 Writing a Single Line
        2.2 Writing Multiple Lines
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Created on: 27-05-2026
"""

from pathlib import Path

path = Path('./trade_log.txt')
path.write_text("BUY AAPL 100 @ 175.50\n")

contents = "SELL AAPL 100 @ 180.00\n"
contents += "BUY MSFT 50 @ 300.00\n"
contents += "SELL MSFT 50 @ 310.00\n"
path.write_text(contents)