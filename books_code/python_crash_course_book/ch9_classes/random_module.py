""" 
File: random_module.py
Author: Alex Alcón
GitHub: https://github.com/alexalcon
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Description: 
    5. The Python Standard Library
        5.1 The random Module    
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Created on: 26-03-2026
"""

from random import randint
from random import choice

# simulate a random price movement in ticks (-5 to +5)
price_change: int = randint(-5, 5)
print(f"Random price change: {price_change} ticks")

assests: list[str] = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'TSLA']
selected_asset: str = choice(assests)
print(f"Randomly selected asset: {selected_asset}")