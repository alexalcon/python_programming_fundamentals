"""Mean reversion strategy classes."""

from trading_strategy import TradingStrategy

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
        
        # subclass-specific attributes  
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