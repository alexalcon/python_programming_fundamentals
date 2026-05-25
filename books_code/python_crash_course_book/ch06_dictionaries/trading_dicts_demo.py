"""
trading_dicts_demo.py
Demonstrates all Chapter 6 dictionary concepts applied to algo trading.
"""

from random import choice, randint

# --- 1. define a dictionary (a trade object) ---
trade = {'symbol': 'aapl', 'side': 'buy', 'quantity': 100}
print("=== Trade Object ===")
print(f"Symbol: {trade['symbol'].upper()}")
print(f"Side:   {trade['side'].upper()}")
print(f"Qty:    {trade['quantity']}")

# --- 2. add new key-value pairs ---
trade['price'] = 175.50
trade['timestamp'] = '2025-06-15 09:30:01'
print(f"\nAfter fill: {trade}")

# --- 3. start from an empty dictionary ---
position = {}
position['symbol'] = trade['symbol']
position['shares'] = trade['quantity']
position['avg_cost'] = trade['price']
print(f"\nPosition built: {position}")

# --- 4. modify values ---
position['avg_cost'] = 174.80  # const basis updated
print(f"Updated avg cost: ${position['avg_cost']}")

# --- 5. delete a key-value pair ---
trade['notes'] = 'test run'
print(f"\nBefore deleting notes: {trade}")
del trade['notes']
print(f"After deleting notes: {trade}")

# --- 6. use get() for safe access --- 
stop_loss = trade.get('stop_loss', 'Not set')
print(f"Stop loss: {stop_loss}")

# --- 7. dictionary of similar objects (portfolio weights) ---
portfolio = {
    'aapl': 0.30,
    'msft': 0.25,
    'goog': 0.20,
    'tsla': 0.15,
    'nvda': 0.10,
}

# loop through all key-value pairs
print("\n=== Portfolio Weights ===")
for symbol, weight in portfolio.items():
    print(f"  {symbol.upper()}: {weight:.0%}")

# loop through sorted keys
print("\n=== Portfolio Weights (Sorted) ===")
for symbol in sorted(portfolio.keys()):
    print(f"  {symbol.upper()}: {portfolio[symbol]:.0%}")

# total allocation (sum of values)
print(f"\nTotal allocation: {sum(portfolio.values()):.0%}")

# --- 8. check membership with keys() ---
print("\n=== Portfolio Membership ===")
check_symbols = ['aapl', 'amzn', 'goog']
for symbol in check_symbols:
    if symbol in portfolio.keys():
        print(f"  {symbol.upper()} in portfolio")
    else:
        print(f"  {symbol.upper()} not in portfolio")

# --- 9. nesting: list of dictionaries (order blotter) ---
print("\n=== Order Blotter ===")
blotter = []
symbols = ['aapl', 'msft', 'goog', 'tsla', 'nvda']
for i in range(5):
    order = {
        'id': i + 1,
        'symbol': symbols[i],
        'side': choice(['buy', 'sell']),
        'quantity' : randint(10, 200),
        'status': choice(['filled', 'pending', 'cancelled']),
    }
    blotter.append(order)

for order in blotter[:3]:
    print(f"  #{order['id']} {order['side'].upper()} "
          f"{order['quantity']} shares of {order['symbol'].upper()} "
          f"({order['status']})")
print(f"  ... ({len(blotter)} total orders)")

# --- 10. nesting: list in a dictionary (strategy config) ---
print("\n=== Strategy Config ===")
strategy = {
    'name': 'multi_ma',
    'lookbacks': [10, 20, 50, 200],
    'universe': ['aapl', 'msft', 'goog'],
}
print(f"Strategy: {strategy['name']}")
for period in strategy['lookbacks']:
    print(f"  {period}-day MA")

# --- 11. nesting: dictionary in a dictionary (account config) ---
print("\n=== Account Config ===")
accounts = {
    'alpha': {'capital': 50000, 'risk': 0.05, 'strategy': 'momentum'},
    'beta': {'capital': 100000, 'risk': 0.01, 'strategy': 'value'}
}
for name, config in accounts.items():
    print(f"  {name.upper()}: Capital: ${config['capital']:,} | "
          f"Risk: {config['risk']:.0%} | Strategy: {config['strategy'].title()}")

# --- 12. unique signal types with set() ---
print(f"\n=== Unique Signal Types ===")
signals = {s: choice(['buy', 'sell', 'hold']) for s in symbols}
print(f"  Signals: {signals}")
print(f"  Unique signal types: {set(signals.values())}")