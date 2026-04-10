"""
trading_functions_utils.py
Demonstrates all Chapter 8 function concepts applied to algo trading.
"""

from random import randint


# --- 1. basic function with docstring ---
def check_market_status():
    """Display the current market status."""
    print("Market is open. Ready to trade.\n")


# --- 2. positional & keyword arguments, default values, 
#        returning value (a dict) ---
def place_order(symbol: str, side: str='buy', quantity: int=100) -> dict:
    """Place a trade order with a default side and quantity."""
    print(f"ORDER: {side.upper()} {quantity} units of {symbol.upper()}")
    return {'symbol': symbol.upper(), 
            'side': side.upper(), 
            'quantity': quantity}


# --- 3. return value, optional argument ---
def format_ticker(exchange: str, symbol: str, asset_class: str=''):
    """Return a formatted ticker string, optionally with asset class."""
    if asset_class:
        ticker = f"{exchange.upper()}:{symbol.upper()} ({asset_class.upper()})"
    else:
        ticker = f"{exchange.upper()}:{symbol.upper()}"
    return ticker.upper()


# --- 4. passing and modifying a list ---
def execute_pending_orders(pending: list[dict], executed: list[dict]):
    """
    Process pending orders and move them to executed list.

    List of dicts arguments:
    pending: list of dicts with keys 'symbol', 'side', 'quantity'
    executed: list to append executed orders with added 'pnl' key
    """
    while pending:
        order: dict = pending.pop() # catching a pending order to execute
        pnl = randint(-200, 1000)
        order['pnl'] = pnl
        print(f"  Executed: {order['side'].upper()} {order['quantity']} "
              f"{order['symbol']} -> PnL: ${pnl}")
        executed.append(order)


def show_execution_report(executed: list[dict]):
    """Display a summary of all executed orders."""
    print("\n--- Execution Report ---")
    total_pnl = 0
    for order in executed:
        print(f"  {order['side'].upper()} {order['quantity']} "
              f"{order['symbol'].upper()}: ${order['pnl']}")
        total_pnl += order['pnl']
    print(f"  Total PnL: ${total_pnl}")


# --- 5. arbitrary positional arguments (*args) ---
def add_to_watchlist(portfolio_name: str, *symbols:str):
    """Add any number of symbols to a named watchlist."""
    print(f"\nWatchlist '{portfolio_name}' portfolio:")
    for symbol in symbols:
        print(f"  + {symbol.upper()}")


# --- 6. arbitrary keyword arguments (**kwargs) ---
def build_strategy(name: str, strategy_type: str, **parameters):
    """Build a strategy config dict with arbitrary parameters."""
    parameters['name'] = name
    parameters['type'] = strategy_type
    return parameters