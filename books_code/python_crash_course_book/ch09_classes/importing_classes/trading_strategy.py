"""Base trading strategy class."""

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