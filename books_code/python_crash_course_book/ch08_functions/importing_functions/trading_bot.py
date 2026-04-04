""" 
File: trading_bot.py
Author: Alex Alcón
GitHub: https://github.com/alexalcon
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Description: 
    
    6. Storing Functions in Modules
        6.1 Importing an Entire Module
        6.2 Importing Specific Functions
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Created on: 04-04-2026
""" 

import order_utils

order_utils.place_order("BTC", "BUY", 100)
order_utils.place_order("ETH", "SELL", 100)
order_utils.cancel_order(12345)