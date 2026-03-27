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
        # core strategy attributes
        self.symbol: str = symbol
        self.timeframe: str = timeframe
        self.capital: float = capital

        # default attributes for tracking performance
        self.total_trades: int = 0
        self.realized_pnl: float = 0.0

    # methods for strategy information and performance tracking
    # ─────────────────────────────────────────────────────────
    def get_description(self) -> str:
        """Return a formatted strategy description."""
        description: str = f"{self.symbol} | " + \
                           f"{self.timeframe} | " + \
                           f"${self.capital}"
        return description
    
    def read_pnl(self) -> None:
        """Print the current realized PnL."""    
        print(f"Realized PnL: ${self.realized_pnl}")
    # ─────────────────────────────────────────────────────────

    # methods for modifying performance tracking attributes
    # ──────────────────────────────────────────────────────────────────
    def update_pnl(self, pnl: float) -> None:
        """
        Set the realized PnL to the given value.
        Add validation to prevent suspicious resets.
        """
        if pnl >= self.realized_pnl:
            self.realized_pnl = pnl
        else:
            print("Warning: PnL rollback detected. Review trade log.")
    
    def add_pnl(self, amount: float) -> None:
        """Add the given PnL amount to the realized PnL."""
        self.realized_pnl += amount

    def increment_trades(self, count: int) -> None:
        """Add the given number to the total trade count."""
        self.total_trades += count
    # ──────────────────────────────────────────────────────────────────
    

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

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2.2 Modifying Attribute Values
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("2.2 Modifying Attribute Values")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(thick_dash)
print("2.2.1 Modifying an Attribute's Value Directly")
print("─────────────────────────────────────────────")
strategy_btcusd.realized_pnl = 25.0
strategy_btcusd.read_pnl()
print("─────────────────────────────────────────────")
print("2.2.2 Modifying an Attribute's Value Through a Method")
print("─────────────────────────────────────────────────────")
strategy_btcusd.update_pnl(50.0)
strategy_btcusd.read_pnl()
print("─────────────────────────────────────────────────────")
print("2.2.3 Incrementing an Attribute's Value Through a Method")
print("────────────────────────────────────────────────────────")
strategy_btcusd.add_pnl(250.0)
strategy_btcusd.read_pnl()
strategy_btcusd.increment_trades(3)
print(f"Total trades executed: {strategy_btcusd.total_trades}")
print(thick_dash)