from general_trading_strategy import TradingStrategy
from risk_manager import RiskManager
from random import randint

class MeanReversionStrategy(TradingStrategy):
    """Mean reversion strategy with risk management."""

    def __init__(self, symbol: str, 
                       timeframe: str, 
                       capital: float) -> None:
        # call the superclass's __init__ method to initialize core attributes
        super().__init__(symbol, timeframe, capital)

        # default attributes for mean reversion logic
        self.lookback_period: int = 20
        self.z_score_threshold: float = 2.0

        # composition - include a RiskManager instance as an attribute 
        self.risk_manager = RiskManager()

    def generate_signal(self) -> str:
        """Override: mean reversion signal generation."""
        # simulate a z-score
        fake_z_score: float = randint(-300, 300) / 100  

        print(f"[MR] {self.symbol} z-score: {fake_z_score:.2f}")

        # main logic for mean reversion signals 
        # based on z-score thresholds
        if fake_z_score < -self.z_score_threshold:
            return "BUY"
        elif fake_z_score > self.z_score_threshold:
            return "SELL"
        else:
            return "HOLD"
        
    def run_backtest_step(self) -> float:
        """Simulate a one step of a backtest."""
        signal: str = self.generate_signal()
        if signal != "HOLD":
            quantity: int = 100
            if self.risk_manager.is_within_limits(quantity):
                self.execute_order(signal, quantity)
                pnl: float = randint(-200, 300) / 100
                self.add_pnl(self.realized_pnl + pnl)
                return pnl