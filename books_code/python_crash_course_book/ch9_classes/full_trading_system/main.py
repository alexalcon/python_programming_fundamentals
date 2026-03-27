from mean_reversion_trading_strategy import MeanReversionStrategy

btcusd_strategy= MeanReversionStrategy("BTCUSD", "1H", 10000.0)
print(btcusd_strategy.get_description())
btcusd_strategy.risk_manager.describe_risk_params()
print()

for i in range(50):
    print(f"--- Step {i+1} ---")
    print("pnl:", btcusd_strategy.run_backtest_step())

print()
btcusd_strategy.read_pnl()
print(f"Total trades: {btcusd_strategy.total_trades}")
max_loss : float = btcusd_strategy.risk_manager.get_max_loss(btcusd_strategy.capital)
print(f"Max acceptable loss: ${max_loss:.2f}")