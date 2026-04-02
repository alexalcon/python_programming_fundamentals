""" 
File: return_values.py
Author: Alex Alcón
GitHub: https://github.com/alexalcon
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Description: 
    
    3. Return Values
        3.1 Returning a Simple Value
        3.2 Making an Argument Optional
        3.3 Returning a Dictionary
        3.4 Using a Function with a while Loop
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Created on: 02-04-2026
""" 

def format_ticker(exchange: str, symbol: str, asset_class: str = "") -> str:
    """
    Return a formatted ticker string, optionally including asset class.
    """
    if asset_class:
        ticker = f"{exchange}:{symbol} ({asset_class})"
    else:
        ticker = f"{exchange}:{symbol}"

    return ticker.upper()


def build_trade(symbol: str, side: str, quantity: float = None) -> dict:
    """Return a dictionary representing a trade."""
    trade = {"symbol": symbol, "side": side}
    if quantity:
        trade["quantity"] = quantity
    return trade


thick_dash = "━" * 70 
thin_dash = "─" * 70

print(thin_dash)
print(format_ticker("binance", "BTCUSD"))
print(format_ticker("binance", "ETHUSD", "spot"))
print(thin_dash)
my_trade = build_trade("AAPL", "buy")
print(my_trade)
print(thin_dash)
my_trade_with_quantity = build_trade("AAPL", "buy", 100)
print(my_trade_with_quantity)
print(thin_dash)

while True:
    print("Enter trade details:")
    print("(enter 'q' at any time to quit)")

    symbol = input("Symbol: ")
    if symbol == 'q':
        break

    side = input("Side (buy/sell): ")
    if side == 'q':
        break

    trade = build_trade(symbol, side)
    print(f"\nTrade created: {trade}")
    print(thin_dash)