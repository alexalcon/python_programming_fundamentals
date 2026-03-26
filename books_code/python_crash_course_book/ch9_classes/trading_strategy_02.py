""" 
File: trading_strategy_02.py
Author: Alex Alcón
GitHub: https://github.com/alexalcon
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Description: 
    
    2. Working with Classes and Instances
        2.1 Setting a Default Value for an Attribute
        2.2 Modifying Attribute Values
            2.2.1 Modifying an Attribute's Value Directly
            2.2.2 Modifying an Attribute's Value Through a Method
            2.2.3 Incrementing an Attribute's Value Through a Method
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Created on: 25-03-2026
"""

class TradingStrategy:
    """A simple model of a trading strategy with tracking."""

    def __init__(self, symbol: str, timeframe: str, capital: float) -> None:
        """Initialize strategy attributes."""
        self.symbol: str = symbol
        self.timeframe: str = timeframe
        self.capital: float = capital
        self.total_trades: int = 0    # default attribute
        self.realized_pnl: float = 0.0  # default attribute
    
    def get_description(self) -> str:
        """Return a formatted strategy description."""
        description: str = f"{self.symbol} | {self.timeframe} | ${self.capital}"
        return description
    
    def read_pnl(self) -> None:
        """Print the current realized PnL."""    
        print(f"Realized PnL: ${self.realized_pnl}")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2.1 Setting a Default Value for an Attribute
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("2.1 Setting a Default Value for an Attribute")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

# instance of the TradingStrategy class
strategy_btcusd: TradingStrategy = TradingStrategy('BTCUSD', '1H', 100)

# dashed lines for better readability of output
thick_dash: str = "━" * 30 
thin_dash: str = "─" * 30

# printting description 
# printing default PnL and total trades of the strategy
print(thick_dash)
print(strategy_btcusd.get_description())
print(thin_dash)
print(f"Total trades: {strategy_btcusd.total_trades}")
strategy_btcusd.read_pnl()
print(thick_dash)
print("")