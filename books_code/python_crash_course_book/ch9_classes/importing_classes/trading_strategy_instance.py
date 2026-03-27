""" 
File: trading_strategy.py
Author: Alex Alcón
GitHub: https://github.com/alexalcon
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Description: 
    
    4. Importing Classes
        4.1 Importing a Single Class
        4.2 Storing Multiple Classes in a Module
        4.3 Importing Multiple Classes from a Module
        4.4 Importing an Entire Module
        4.5 Importing All Classes from a Module (Not Recommended)
        4.6 Importing a Module into a Module
        4.7 Using Aliases
        4.8 Finding Your Own Workflow
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Created on: 26-03-2026
"""

from trading_strategy import TradingStrategy 
from mean_reversion_strategy import MeanReversionStrategy as MRS

btcusd_strategy: TradingStrategy = TradingStrategy('BTCUSD', '1H', 1000)
print(btcusd_strategy.get_description())

eth_strategy: MRS = MRS('ETHUSD', '1H', 1000)
print(eth_strategy.get_description())