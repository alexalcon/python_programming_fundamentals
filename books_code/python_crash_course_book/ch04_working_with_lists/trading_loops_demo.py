"""
trading_loops_demo.py
Demonstrated all Chapter 4 concepts applied to algo trading.
"""

from random import randint

# --- 1. for loop: scan watchlist ---
watchlist = ['appl', 'msft', 'goog', 'tsla', 'nvda']
print("=== Market Scanner ===\n")

signals = []
for symbol in watchlist:
    strength = randint(1, 100)
    print(f"  {symbol.upper()} signal strength: {strength}")
    if strength > 50:
        signals.append(symbol.upper())

# after the loop — summary
print(f"\nSignals found: {len(signals)}")
print(f"Actionable: {signals}\n")

# --- 2. range() and list(): generate lookback periods ---
lookback_periods = list(range(5, 55, 5))
print(f"Lookback sweep values: {lookback_periods}")

# --- 3. numerical list with statistics ---
# ──────────────────────────────────────────────────────────────────────
# _ is a common convention for unused loop variables the `_` is just a 
# variable name, which by convention, it means 
#   
#   "I don't care about this value." 
# 
# it's a throwaway variable used when you need to repeat an action a 
# certain number of times, but you don't need to keep track of the 
# loop index, i.e., you just want to repeat `randint(-500, 1000)` 
# exactly 10 times 
# ──────────────────────────────────────────────────────────────────────
daily_pnl = [randint(-100, 1000) for _ in range(10)] # $ PnL for 10 days
print(f"\n10-day PnL: {daily_pnl}")
print(f"  Best day:  ${max(daily_pnl)}")
print(f"  Worst day: ${min(daily_pnl)}")
print(f"  Total PnL: ${sum(daily_pnl)}")

# --- 4. list comprehension: filter positive days ---
winning_days = [pnl for pnl in daily_pnl if pnl > 0]
print(f"  Winning days: {len(winning_days)} / {len(daily_pnl)}")

# --- 5. slicing: rolling window and top positions ---
prices = [round(150 + randint(-5, 5) + (i * 0.5), 2) for i in range(20)]
print(f"\n20-day price series: {prices}")

last_5 = prices[-5:]
print(f"  Last 5 days: {last_5}")
print(f"  5-day avg: ${round(sum(last_5) / len(last_5), 2)}")

# --- 6. copying a list: independent strategy universes ---
base_universe = ['aapl', 'msft', 'goog']
momentum_universe = base_universe[:]
mean_rev_universe = base_universe[:]

momentum_universe.append('tsla')
mean_rev_universe.append('bnd')

print(f"\nMomentum universe:       {momentum_universe}")
print(f"Mean reversion universe: {mean_rev_universe}")      
print(f"Base universe unchanged: {base_universe}")

# --- 7. tuples: fixed risk parameters ---
risk_params = (0.02, 1000, 5)
print(f"\nSession risk limits:")
print(f"  Max drawdown:       {risk_params[0] * 100}%")
print(f"  Max position size: ${risk_params[1]}")
print(f"  Max positions:      {risk_params[2]}")

# writing over a tuple between sessions
risk_params = (0.01, 500, 3)
print(f"\nTightened risk limits for next session:")
for param in risk_params:
    print(f"  {param}") 