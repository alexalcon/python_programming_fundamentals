""" 
File: trading_strategy_inheritance.py
Author: Alex Alcón
GitHub: https://github.com/alexalcon
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Description: 

    3. Inheritance
        3.1 The __init__() Method for a Child Class
        3.2 Defining Attributes and Methods for the Child Class
        3.3 Overriding Methods from the Parent Class
        3.4 Instances as Attributes (Composition)
        3.5 Modeling Real-World Objects
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Created on: 26-03-2026
"""

class TradingStrategy:
    """"A general trading strategy."""

    def __init__(self, symbol: str, timeframe: str, capital: float) -> None:
        """Initialize general strategy attributes."""
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
    # ──────────────────────────────────────────────────────────────────
    
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 3.1 The __init__() Method for a Child Class
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
class MeanReversionStrategy(TradingStrategy):
    """A mean reversion strategy — specialized TradingStrategy."""

    def __init__(self, symbol: str, timeframe: str, capital: float) -> None:
        """Initialize parent attributes, then child-specific ones."""
        super().__init__(symbol, timeframe, capital)
        
        # subclass-specific attributes  
        self.lookback_period: int = 20
        self.z_score_threshold: float = 2.0 

    def describe_parameters(self) -> None:
        """Print the strategy's specific parameters."""
        print(f"Lookback Period: {self.lookback_period} periods")
        print(f"Z-Score Threshold: {self.z_score_threshold}")


mr_strategy_btcusd: MeanReversionStrategy = MeanReversionStrategy('BTCUSD', '1H', 100)

# dashed lines for better readability of output
thick_dash = "━" * 70 
thin_dash = "─" * 70 

print(thick_dash)
print(mr_strategy_btcusd.get_description())
print(thin_dash)
mr_strategy_btcusd.describe_parameters()
print(thick_dash)