# Full Trading System

This folder contains a small educational trading-system example that combines several Chapter 8 function concepts into one runnable program. The code is intentionally simple and is meant to demonstrate how functions can organize trading-related tasks rather than provide a production-ready trading engine.

## Learning goals

This example brings together the chapter topics in one place:

- defining functions with docstrings
- calling functions with positional arguments
- calling functions with keyword arguments
- using default parameter values
- returning values from functions
- passing and modifying lists
- passing copies of lists to preserve original data
- using arbitrary positional arguments with `*args`
- using arbitrary keyword arguments with `**kwargs`
- splitting functions across modules and importing them
- using the standard library `random` module to simulate trade PnL

## File overview

- `trading_functions_utils.py`: defines the reusable helper functions for market status, order placement, ticker formatting, order execution, execution reporting, watchlists, and strategy configuration
- `trading_functions_demo.py`: imports the utility module, calls each function in sequence, and prints the results so you can see how each Chapter 8 concept behaves in one script

## How the example works

`trading_functions_demo.py` walks through a mini trading workflow step by step:

1. `check_market_status()` prints a simple market-open message.
2. `place_order()` is called three times to show default arguments, positional arguments, and keyword arguments.
3. Each order call returns a dictionary containing `symbol`, `side`, and `quantity`.
4. `format_ticker()` is used once without the optional `asset_class` argument and once with it.
5. The returned order dictionaries are placed into a `pending_orders` list.
6. A copy of that list is stored in `original_orders` so the original order data can still be reviewed later.
7. `execute_pending_orders()` removes orders from the pending list one at a time, assigns a random PnL value, and appends the updated order to `executed_orders`.
8. `show_execution_report()` prints every executed order and the total combined PnL.
9. `add_to_watchlist()` is called with different numbers of symbols to demonstrate `*args`.
10. `build_strategy()` is called with named configuration settings to demonstrate `**kwargs`.

## Function concepts in this folder

### Return values

Several functions return useful values instead of only printing output. For example, `place_order()` returns a dictionary representing an order, and `format_ticker()` returns a formatted ticker string.

### List mutation

`execute_pending_orders()` shows that when a list is passed to a function, the function can modify that list directly. After execution, `pending_orders` becomes empty while `executed_orders` contains the processed trades.

### Preserving original data

The demo creates `original_orders = pending_orders[:]` before processing. This shows how passing or storing a copy can preserve the original records for audit or comparison.

### Arbitrary arguments

`add_to_watchlist()` accepts any number of ticker symbols through `*symbols`, while `build_strategy()` accepts any number of named settings through `**parameters`.

## Running the example

Run the program from inside this folder so the local import resolves correctly:

```bash
cd ./books_code/python_crash_course_book/ch08_functions/full_trading_system
python trading_functions_demo.py
```

Because the example uses random numbers, each run will produce different PnL values during order execution.

## What to notice in the output

When you run the script, you will see:

- the market status message
- three example orders created with different argument styles
- two formatted ticker strings
- each pending order being executed with a random PnL
- a final execution report with total PnL
- confirmation that the copied `original_orders` list was preserved
- the empty pending queue after all orders are processed
- two watchlists created with different numbers of symbols
- the final strategy configuration dictionary

## Important limitations

This example is useful for learning function design, but it is still a toy model:

- prices are not loaded from real market data
- order execution is simulated immediately
- PnL values are randomly generated
- no validation is performed on symbols, sides, or quantities
- no risk controls, fees, slippage, or portfolio accounting are included
- the strategy configuration is only stored as a dictionary and is not executed