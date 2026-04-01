""" 
File: passing_arguments.py
Author: Alex Alcón
GitHub: https://github.com/alexalcon
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Description: 
    
    2. Passing Arguments
        2.1 Positional Arguments
            2.1.1 Multiple Function Calls
            2.1.2 Order Matters in Positional Arguments
        2.2 Keyword Arguments
        2.3 Default Values
        2.4 Equivalent Function Calls
        2.5 Avoiding Argument Errors
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Created on: 01-04-2026
""" 

# positional arguments and default values
def place_order(symbol: str, side: str = "BUY"):
    """Place a trade order for a given symbol and side."""
    print(f"Placing order: {side.upper()} order for {symbol.upper()}")
    print(f"Order for {symbol.upper()} ({side.upper()}) submitted.")
    print("-----------------------------------------------------------")


place_order("aapl", "buy")
place_order("nvidia")
place_order("BTCUSD", "sell")

# keyword arguments
place_order(side="buy", symbol="ethusd")
place_order(symbol="solusd", side="sell")
