"""
File: trading_strategy_03.py
Author: Alex Alcón
GitHub: https://github.com/alexalcon
------------------------------------------------------------------------
Description:

    3A. Working with Class Methods
        3A.1 Reading Class-Level Strategy Configuration
        3A.2 Creating Strategies with a Class Method
------------------------------------------------------------------------
Created on: 24-09-2026
"""


class TradingStrategy:
    """Model a strategy and create instances from shared risk profiles."""

    RISK_PROFILES: dict[str, float] = {
        "conservative": 500.0,
        "balanced": 1000.0,
        "aggressive": 2000.0,
    }

    def __init__(self, symbol: str, timeframe: str, capital: float) -> None:
        """Initialize a strategy with its market and allocated capital.

        Parameters
        ----------
        symbol : str
            Market symbol, such as ``BTCUSD``.
        timeframe : str
            Candle timeframe used by the strategy.
        capital : float
            Example capital allocation for the strategy.
        """
        self.symbol = symbol
        self.timeframe = timeframe
        self.capital = capital

    @classmethod
    def available_risk_profiles(cls) -> list[str]:
        """Return the profile names configured for this strategy class.

        ``cls`` refers to the class, so this method can read shared class
        data without an already-created strategy instance.

        Returns
        -------
        list[str]
            Names of the configured risk profiles.
        """
        return list(cls.RISK_PROFILES)

    @classmethod
    def from_risk_profile(
        cls,
        symbol: str,
        timeframe: str,
        risk_profile: str,
    ) -> "TradingStrategy":
        """Build a strategy using capital assigned to a named profile.

        ``cls`` is used both to look up class-level configuration and to
        construct the result. No strategy instance is needed to call this.

        Parameters
        ----------
        symbol : str
            Market symbol, such as ``BTCUSD``.
        timeframe : str
            Candle timeframe used by the strategy.
        risk_profile : str
            Configured capital profile: conservative, balanced, or aggressive.

        Returns
        -------
        TradingStrategy
            A new strategy with capital from the selected profile.

        Raises
        ------
        ValueError
            If the requested risk profile is not configured.
        """
        profile_name = risk_profile.lower()
        try:
            capital = cls.RISK_PROFILES[profile_name]
        except KeyError as error:
            available_profiles = ", ".join(cls.available_risk_profiles())
            raise ValueError(
                f"Unknown risk profile '{risk_profile}'. "
                f"Choose from: {available_profiles}."
            ) from error

        return cls(symbol, timeframe, capital)

    def get_description(self) -> str:
        """Return a concise description of this strategy."""
        return (
            f"{self.symbol} | {self.timeframe} | "
            f"{self.capital:.2f} USD"
        )


print("=" * 60)
print("3A. Working with Class Methods")
print("=" * 60)

# The class method reads shared profile data before any instance exists.
print("Available risk profiles:", TradingStrategy.available_risk_profiles())

# Call the factory on the class; it uses cls to create each instance.
strategy_btcusd = TradingStrategy.from_risk_profile(
    "BTCUSD", "1H", "balanced"
)
strategy_ethusd = TradingStrategy.from_risk_profile(
    "ETHUSD", "30M", "conservative"
)

print("-" * 60)
print(strategy_btcusd.get_description())
print(strategy_ethusd.get_description())
print("=" * 60)