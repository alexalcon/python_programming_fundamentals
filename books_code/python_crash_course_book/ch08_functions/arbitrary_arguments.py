""" 
File: passing_a_list.py
Author: Alex Alcón
GitHub: https://github.com/alexalcon
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Description: 
    
    5. Passing an Arbitrary Number of Arguments
        5.1 Using *args (Arbitrary Positional Arguments)
        5.2 Mixing Positional and Arbitrary Arguments
        5.3 Using kwargs (Arbitrary Keyword Arguments)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Created on: 04-04-2026
""" 

# 5.1 Using *args (Arbitrary Positional Arguments)
# 5.2 Mixing Positional and Arbitrary Arguments
def add_to_watchlist(portfolio_name: str, *symbols: str):
    """Add symbols to a named portfolio watchlist."""
    print(f"Adding to '{portfolio_name}' watchlist:")
    for symbol in symbols:
        print(f"- {symbol.upper()}")


# 5.3 Using kwargs (Arbitrary Keyword Arguments)
def build_strategy(name: str, strategy_type: str, **parameters):
    """Build a dictionary containing everything about a strategy."""
    parameters['name'] = name
    parameters['strategy_type'] = strategy_type
    return parameters


thin_dash = "─" * 70

# 5.1 Using *args (Arbitrary Positional Arguments)
# 5.2 Mixing Positional and Arbitrary Arguments
print(thin_dash)
add_to_watchlist('aggressive', 'aapl')
print(thin_dash)
add_to_watchlist('conservative', 'msft', 'goog')

# 5.3 Using kwargs (Arbitrary Keyword Arguments)
print(thin_dash)
strategy = build_strategy('mean_rev_01', 'mean_reversion',
                            lookback=20,
                            z_threshold=2.0,
                            capital=10000)
print(strategy)