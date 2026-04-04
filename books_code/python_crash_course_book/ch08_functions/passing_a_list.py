""" 
File: passing_a_list.py
Author: Alex Alcón
GitHub: https://github.com/alexalcon
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Description: 
    
    4. Passing a List
        4.1 Modifying a List in a Function
        4.2 Preventing a Function from Modifying a List
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Created on: 04-04-2026
""" 

def monitor_assets(symbols: list):
    """Print a monitoring status for each asset in the list."""
    for symbol in symbols:
        msg = f"Monitoring {symbol.upper()}..."
        print(msg)


def execute_pending_orders(pending_orders: list, executed_orders: list):
    """
    Simulate executing each pending order.
    Move each order to the executed list after processing.
    """
    while pending_orders:
        current_order: str = pending_orders.pop()
        print(f"Executing order: {current_order}")
        executed_orders.append(current_order)


def show_executed_orders(executed_orders: list):
    """Show all orders that were executed."""
    print("\nThe following orders have been executed:")
    for order in executed_orders:
        print(order)


thick_dash = "━" * 40 
thin_dash = "─" * 40

# 4. Passing a List
watch_list : list = ["BTC", "ETH", "XRP"]
monitor_assets(watch_list)

# 4.1 Modifying a List in a Function
print(thin_dash)
pending_orders : list = ['BUY AAPL 100', 'SELL MSFT 50', 'BUY GOOG 75']
executed_orders : list = []
execute_pending_orders(pending_orders, executed_orders)
show_executed_orders(executed_orders)
print("Original pending orders (empty):", pending_orders) 

# 4.2 Preventing a Function from Modifying a List
print(thin_dash)
pending_orders : list = ['BUY AAPL 100', 'SELL MSFT 50', 'BUY GOOG 75']
executed_orders : list = []
execute_pending_orders(pending_orders[:], executed_orders)
show_executed_orders(executed_orders)
print("Original pending orders (unchanged):", pending_orders)