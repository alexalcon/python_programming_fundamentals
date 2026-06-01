""" 
File: storing_data.py
Author: Alex Alcón
GitHub: https://github.com/alexalcon
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Description: 
    
    4. Storing Data
        4.1 Using json.dumps() and json.loads()
        4.2 Saving and Reading User-Generated Data
        4.3 Refactoring
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Created on: 01-06-2026
"""

from pathlib import Path
import json

def get_stored_portfolio(path):
    """Load stored portfolio if available."""
    if path.exists():
        contents = path.read_text()
        return json.loads(contents)
    else:
        return None

def initialize_portfolio(path):
    """Create a new default portfolio and save it."""
    portfolio = {
        'cash': 100000,
        'positions': {},
        'session': 1,
    }
    contents = json.dumps(portfolio)
    path.write_text(contents)
    return portfolio

def start_session():
    """Start a trading session, loading or creating a portfolio."""
    path = Path('portfolio_state.json')
    portfolio = get_stored_portfolio(path)
    if portfolio is None:
        portfolio = initialize_portfolio(path)
    print(f"Current portfolio: {portfolio}")


# ───────────────────────────────────────
# 4.1 Using json.dumps() and json.loads()
# ───────────────────────────────────────
print("\n───────────────────────────────────────")
print("4.1 Using json.dumps() and json.loads()")
print("───────────────────────────────────────")

# save strategy parameters
params = {
    'strategy': 'momentum',
    'lookback': 20,
    'threshold': 1.5,
    'symbols': ['aapl', 'msft', 'goog'],
}

path = Path('strategy_config.json')
contents = json.dumps(params) # takes a python object and 
                              # returns a JSON-formatted string
path.write_text(contents)

# load strategy parameters
contents = path.read_text()
params = json.loads(contents) # takes a JSON-formatted string 
                              # and returns a python object 
                              # (like a list or dict)          
print(params)

# ──────────────────────────────────────────
# 4.2 Saving and Reading User-Generated Data
# ──────────────────────────────────────────
print("\n─────────────────────────────────────────")
print("4.2 Saving and Reading User-Generated Data")
print("─────────────────────────────────────────")

path = Path('portfolio_state.json')

"""
You can combine saving and loading into a single program using 
path.exists(). The exists() method returns True if a file or 
folder exists and False if it does not.
"""
if path.exists():
    contents = path.read_text()
    portfolio = json.loads(contents)
    print(f"Restored portfolio: {portfolio}")
else:
    portfolio = {
        'cash': 10000,
        'positions': {},
        'session': 1,
    }
    contents = json.dumps(portfolio)
    path.write_text(contents)
    print(f"Initialized new portfolio: {portfolio}")

# ───────────────
# 4.3 Refactoring
# ───────────────
print("\n───────────────")
print("4.3 Refactoring")
print("───────────────")

"""
Refactoring is the process of improving code by breaking it up into a 
series of functions that have specific jobs. This makes your code 
cleaner, easier to understand, and easier to extend. Each function 
should have a single, clear purpose stated in its docstring. A 
function should either return the value you are expecting, or it 
should return None.
"""
start_session()