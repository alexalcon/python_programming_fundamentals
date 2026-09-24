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

    # methods for generating signals and executing orders
    # ──────────────────────────────────────────────────────────────────
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
    # ──────────────────────────────────────────────────────────────────


class RiskManager:
    """"A risk management component for trading strategies."""

    def __init__(self, max_position_size: int = 1000, 
                 max_drawdown_pct: float = 5.0) -> None:
        """Initialize risk parameters."""
        self.max_position_size: int = max_position_size
        self.max_drawdown_pct: float = max_drawdown_pct
    
    def describe_risk_params(self) -> None:
        """Print risk management parameters."""
        print(f"Max position size: {self.max_position_size} units")
        print(f"Max drawdown: {self.max_drawdown_pct}%")
    
    def check_risk(self, position_size: int) -> bool:
        if position_size <= self.max_position_size:
            print("Position size within risk limits.")
            return True
        else:
            print("ALERT: Position size exceeds max limit!")
            return False
        
    def get_max_loss(self, current_capital: float) -> float:
        """Calculate maximum acceptable loss."""
        max_loss: float = current_capital * (self.max_drawdown_pct / 100)
        print(f"Max acceptable loss: ${max_loss:.2f}")
        return max_loss


class MeanReversionStrategy(TradingStrategy):
    """A mean reversion strategy — specialized TradingStrategy."""

    def __init__(self, symbol: str, timeframe: str, capital: float) -> None:
        """Initialize parent attributes, then child-specific ones."""
        super().__init__(symbol, timeframe, capital)
        
        # subclass-specific default attributes  
        self.lookback_period: int = 20
        self.z_score_threshold: float = 2.0 

        # composition: include a RiskManager instance as an attribute
        self.risk_manager: RiskManager = RiskManager()

    def describe_parameters(self) -> None:
        """Print the strategy's specific parameters."""
        print(f"Lookback Period: {self.lookback_period} periods")
        print(f"Z-Score Threshold: {self.z_score_threshold}")

    # overriding the parent method with mean reversion logic
    def generate_signal(self) -> None:
        """Override the parent method with mean reversion logic."""
        print(f"Calculating z-score for {self.symbol} "
              f"over {self.lookback_period} periods...")
        print(f"Signal: LONG if z < -{self.z_score_threshold}, "
              f"SHORT if z > {self.z_score_threshold}")


mr_strategy_btcusd: MeanReversionStrategy = MeanReversionStrategy('BTCUSD', '1H', 100)

# dashed lines for better readability of output
thick_dash = "━" * 70 
thin_dash = "─" * 70 

print(thick_dash)
print(mr_strategy_btcusd.get_description())
print(thin_dash)
mr_strategy_btcusd.describe_parameters()
print(thin_dash)
mr_strategy_btcusd.risk_manager.describe_risk_params()
print(thin_dash)
mr_strategy_btcusd.risk_manager.check_risk(500)
mr_strategy_btcusd.risk_manager.check_risk(1500)
print(thin_dash)
mr_strategy_btcusd.risk_manager.get_max_loss(mr_strategy_btcusd.capital)
print(thick_dash)