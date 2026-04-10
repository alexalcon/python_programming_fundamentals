# ========== MAIN PROGRAM ==========

import trading_functions_utils as tfu

# 1. basic function call
tfu.check_market_status()

# 2. positional & keyword arguments, default values, 
#    returning value (a dict)
trade1: dict = tfu.place_order('aapl')              # defaults
trade2: dict = tfu.place_order('msft', 'sell', 50)  # positional
trade3: dict = tfu.place_order(symbol='goog', side='buy', quantity=150)  # keyword
print()

# 3. return value with optional arguments
ticker1: str = tfu.format_ticker('binance', 'btcusdt')
ticker2: str = tfu.format_ticker('binance', 'ethusdt', 'crypto')
print(f"Ticker 1: {ticker1}")
print(f"Ticker 2: {ticker2}\n")

# 4. passing and modifying a list
pending_orders: list[dict] = [trade1, trade2, trade3]
executed_orders: list[dict] = []
# pass a copy to preserve original for audit
original_orders: list[dict] = pending_orders[:]

print("Processing orders:")
tfu.execute_pending_orders(pending_orders, executed_orders)
tfu.show_execution_report(executed_orders)

print(f"\nOriginal pending orders (for audit): {original_orders}")
print(f"Pending queue after execution: {pending_orders}")

# 5. arbitrary positional arguments (*args)
tfu.add_to_watchlist('tech', 'aapl', 'msft', 'goog', 'nvda')
tfu.add_to_watchlist('crypto', 'btcusd', 'ethusd')

# 6. arbitrary keyword arguments (**kwargs)
strategy: dict = tfu.build_strategy(
    'momentum_01', 'momentum',
    lookback_period=20,
    entry_threshold=1.5,
    capital_allocation=250000,
    max_positions=5
)
print(f"\nStrategy config: {strategy}")