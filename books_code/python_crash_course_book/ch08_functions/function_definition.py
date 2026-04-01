""" 
File: function_definition.py
Author: Alex Alcón
GitHub: https://github.com/alexalcon
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Description: 
    
    1. Defining a Function
        1.1 Passing Information to a Function
        1.2 Arguments and Parameters
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Created on: 01-04-2026
"""

def check_market_stats(symbol: str):
    """Display market status for a given symbol."""
    print(f"Checking market status for {symbol.upper()}...")


check_market_stats("aapl")
check_market_stats("BTCUSD")