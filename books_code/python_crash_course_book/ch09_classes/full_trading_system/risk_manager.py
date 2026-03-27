""""Risk manager class for full trading system example"""

class RiskManager:
    """Manages position sizing and drawdown limits."""

    def __init__(self, max_position_size: int = 1000, 
                       max_drawdown_pct: float = 5.0) -> None:
        """Initialize risk management parameters."""
        self.max_position_size: int = max_position_size
        self.max_drawdown_pct: float = max_drawdown_pct

    def describe_risk_params(self) -> None:
        """Print risk management parameters."""
        print(f"Max position: {self.max_position_size} | "
              f"Max drawdown: {self.max_drawdown_pct}%")
        
    def is_within_limits(self, position_size: int) -> bool:
        return position_size <= self.max_position_size
    
    def get_max_loss(self, capital: float) -> float:
        return capital * (self.max_drawdown_pct / 100)