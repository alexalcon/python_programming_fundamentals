"""General trading strategy class for full trading system example"""

class TradingStrategy:
    """Base class for all trading strategies."""

    def __init__(self, symbol: str, timeframe: str, capital: float) -> None:
        # core strategy attributes
        self.symbol: str = symbol
        self.timeframe: str = timeframe
        self.capital: float = capital

        # default attributes for tracking performance
        self.total_trades: int = 0
        self.realized_pnl: float = 0.0
    
    # methods for strategy information and performance tracking
    # ──────────────────────────────────────────────────────────────────────
    def get_description(self) -> str:
        """Return a formatted strategy description."""
        description: str = f"{self.symbol} | " + \
                           f"{self.timeframe} | " + \
                           f"${self.capital}"
        return description
    
    def read_pnl(self) -> None:
        """Print the current realized PnL."""    
        print(f"Realized PnL for {self.symbol}: ${self.realized_pnl:.2f}")
    # ──────────────────────────────────────────────────────────────────────

    # method for modifying performance tracking attributes
    def add_pnl(self, amount: float) -> None:
        """
        Add the given amount to the realized PnL.
        """
        self.realized_pnl += amount

    # methods for generating signals and executing orders
    # ─────────────────────────────────────────────────────────────────────────
    def generate_signal(self) -> None:
        """
        Generate a trading signal for the asset
        based on the strategy's logic.
        """
        print(f"Generating signal for {self.symbol} on {self.timeframe} " + \
              f"timeframe with capital ${self.capital}.")

    def execute_order(self, side: str, quantity: int) -> None:
        """Execute a trade based on the generated signal."""
        print(f"Executing {side} order: {quantity} units of {self.symbol}")
        self.total_trades += 1
    # ─────────────────────────────────────────────────────────────────────────