""" 
File: trading_strategy_01.py
Author: Alex Alcón
GitHub: https://github.com/alexalcon
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Description: 
    
    1. Creating and Using a Class
        1.1 The Anatomy of a Class
        1.2 The __init__() Method
        1.3 Making an Instance from a Class 
        1.4 Accessing Attributes
        1.5 Calling Methods
        1.6 Creating Multiple Instances
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Created on: 23-03-2026
"""

class TradingStrategy:
    """A simple model of a trading strategy."""

    def __init__(self, symbol, timeframe, capital):
        """Initialize core strategy attributes."""
        self.symbol = symbol
        self.timeframe = timeframe
        self.capital = capital
    
    def generate_signal(self):
        """
        Generate a trading signal for the asset based on 
        the strategy's logic.
        """
        print(f"Generating signal for {self.symbol} on {self.timeframe}" +
              f" timeframe with capital ${self.capital}.")
    
    def execute_order(self):
        """Execute a trade based on the generated signal."""
        print(f"Executing order for {self.symbol} on {self.timeframe}" +
              f" timeframe with capital ${self.capital}.")
        
        
# instances of the same TradingStrategy class
strategy_btcusd = TradingStrategy('BTCUSD', '1H', 100) 
strategy_ethusd = TradingStrategy('ETHUSD', '30M', 100) 
strategy_solusd = TradingStrategy('SOLUSD', '15M', 500) 

# dashed lines for better readability of output
thick_dash = "━" * 70 
thin_dash = "─" * 70 

# display strategy information
# ─────────────────────────────────────────────────────────
print(thick_dash)
print(f"Strategy symbol: {strategy_btcusd.symbol}")
print(f"Strategy timeframe: {strategy_btcusd.timeframe}")
print(f"Strategy capital: ${strategy_btcusd.capital}")
print(thin_dash)
print(f"Strategy symbol: {strategy_ethusd.symbol}")
print(f"Strategy timeframe: {strategy_ethusd.timeframe}")
print(f"Strategy capital: ${strategy_ethusd.capital}")
print(thin_dash)
print(f"Strategy symbol: {strategy_solusd.symbol}")
print(f"Strategy timeframe: {strategy_solusd.timeframe}")
print(f"Strategy capital: ${strategy_solusd.capital}")
# ─────────────────────────────────────────────────────────

# simulate generating a trading signal and executing an order
# ─────────────────────────────────────────────────────────────
print(thick_dash)
strategy_btcusd.generate_signal()
strategy_btcusd.execute_order()
print(thin_dash)
strategy_ethusd.generate_signal()
strategy_ethusd.execute_order()
print(thin_dash)
strategy_solusd.generate_signal()
strategy_solusd.execute_order()
print(thick_dash)
# ─────────────────────────────────────────────────────────────