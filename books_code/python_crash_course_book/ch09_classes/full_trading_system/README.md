# Full Trading System

This folder contains a small educational trading-system example that combines several object-oriented Python concepts into one runnable program. The code is intentionally simple and is meant to demonstrate structure and relationships between classes rather than provide a production-ready trading engine.

## Learning goals

This example brings together the chapter topics in one place:

- defining classes with `__init__()`
- creating and using instances
- storing state with attributes
- writing instance methods
- working with default values
- updating attributes over time
- using inheritance with `super()`
- overriding base-class behavior
- using composition to connect objects
- splitting code across multiple modules and importing them
- using the standard library `random` module to simulate signals and PnL

## File overview

- `general_trading_strategy.py`: defines the base `TradingStrategy` class with shared attributes such as `symbol`, `timeframe`, `capital`, `total_trades`, and `realized_pnl`
- `mean_reversion_trading_strategy.py`: defines `MeanReversionStrategy`, which inherits from `TradingStrategy`, overrides signal generation, and owns a `RiskManager`
- `risk_manager.py`: defines `RiskManager`, which handles max position size and max drawdown settings
- `main.py`: creates a strategy instance, prints its configuration, runs a 50-step simulation, and shows final summary values

## How the example works

`main.py` creates a `MeanReversionStrategy` for `BTCUSD` on the `1H` timeframe with `$10000.0` in starting capital.

The simulation then runs through 50 backtest steps:

1. `generate_signal()` creates a fake z-score using `randint()`.
2. If the z-score is below `-2.0`, the strategy returns `BUY`.
3. If the z-score is above `2.0`, the strategy returns `SELL`.
4. Otherwise, it returns `HOLD`.
5. When the signal is not `HOLD`, the strategy checks whether the position size is allowed by `RiskManager`.
6. If the trade is allowed, the order is executed, the trade counter is incremented, and a random PnL value is generated.

## OOP relationships in this folder

### Inheritance

`MeanReversionStrategy` inherits from `TradingStrategy` and reuses the shared strategy fields initialized by the parent class.

### Method overriding

The base class defines a general `generate_signal()` method, while `MeanReversionStrategy` overrides it with mean-reversion-specific logic.

### Composition

`MeanReversionStrategy` contains a `RiskManager` instance through its `risk_manager` attribute. This is a clear example of one class using another class as part of its behavior.

## Running the example

Run the program from inside this folder so the local imports resolve correctly:

```bash
cd ./books_code/python_crash_course_book/ch9_classes/full_trading_system
python main.py
```

Because the example uses random numbers, each run will produce different z-scores, trade signals, and PnL values.

## What to notice in the output

When you run the script, you will see:

- the strategy description
- the risk limits from `RiskManager`
- each simulated step
- whether a trade was executed
- the per-step PnL returned by the backtest step
- the final realized PnL
- the total number of trades
- the maximum acceptable loss based on drawdown percentage

## Important limitations

This example is useful for learning class design, but it is still a toy model:

- prices are not loaded from real market data
- signals are randomly simulated
- orders are always sized at `100` units when a trade happens
- the result of a step can be `None` when the signal is `HOLD`
- the realized PnL accumulation is simplified and not financially accurate