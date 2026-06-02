"""
trading_files_demo.py
Demonstrates all Chapter 10 concepts applied to algo trading.
"""

from pathlib import Path
import json
from random import uniform, choice

# ============================================================
# 1. WRITING DATA — Create sample price files
# ============================================================

def create_sample_data() -> None:
    """Write sample price files for demonstration."""
    symbols = ['aapl', 'msft', 'goog']
    for symbol in symbols:
        prices = [round(150 + uniform(-10, 10), 2) for _ in range(20)]
        content = "\n".join(str(p) for p in prices)
        path = Path(f"{symbol}_prices.txt")
        path.write_text(content)
    print("Sample price files created.\n")

create_sample_data()


# ============================================================
# 2. READING DATA — Load and parse price files
# ============================================================

def read_price_data(path: Path) -> list[float] | None:
    """Load prices for a given symbol. Returns a list of floats or None."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return None
    else:
        lines = contents.splitlines()
        prices = []
        for line in lines:
            try:
                prices.append(float(line.strip()))
            except ValueError:
                pass  # skip lines that cannot be parsed
        return prices
    

# ============================================================
# 3. ANALYSIS — Calculate returns with error handling
# ============================================================

def calculate_returns(prices: list[float]) -> list[float]:
    """Calculate daily returns from a list of prices."""
    returns = []
    for i in range(1, len(prices)):
        try:
            daily_return = (prices[i] - prices[i-1]) / prices[i-1]
        except ZeroDivisionError:
            daily_return = 0.0
        returns.append(round(daily_return, 6))
    return returns


def analyze_symbol(symbol: str) -> dict[str, float] | None:
    """Full analysis pipeline for a given symbol."""
    path = Path(f"{symbol}_prices.txt")
    prices = read_price_data(path)

    if prices is None:
        print(f"  {symbol.upper()}: Price data not found.")
        return None
    
    returns = calculate_returns(prices)
    total_return = (prices[-1] - prices[0]) / prices[0]

    result = {
        'symbol': symbol.upper(),
        'days': len(prices),
        'latest_price': prices[-1],
        'min_price': min(prices),
        'max_price': max(prices),
        'total_return': round(total_return, 4),
        'avg_daily_return': round(sum(returns) / len(returns), 6),
    }

    return result


# ============================================================
# 4. BATCH PROCESSING — Multiple files, some missing
# ============================================================

print("=== Price Analysis ===\n")
symbols_to_analyze = ['aapl', 'msft', 'missing_ticker', 'goog']
results = []

for symbol in symbols_to_analyze:
    analysis = analyze_symbol(symbol)
    if analysis:
        results.append(analysis)
        print(f"  {analysis['symbol']}: {analysis['days']} days | "
              f"Return: {analysis['total_return']:.2%} | "
              f"Latest: ${analysis['latest_price']:.2f}")


# ============================================================
# 5. STORING RESULTS — Save and reload with JSON
# ============================================================

print("\n=== Storing Results ===\n")
state_path = Path('analysis_results.json')
contents = json.dumps(results, indent=4)
state_path.write_text(contents)
print(f"Results saved to {state_path}")


# ============================================================
# 6. LOADING STATE — Check existence, load, and display
# ============================================================

print("\n=== Loading Saved Results ===\n")
if state_path.exists():
    loaded = json.loads(state_path.read_text())
    for r in loaded:
        print(f"  {r['symbol']}: {r['total_return']:.2%}")
    print(f"\n  Total symbols analyzed: {len(loaded)}")
else:
    print("  No saved results found.")


# ============================================================
# 7. TRADE LOG — Writing multiple lines to a file
# ============================================================

print("\n=== Trade Log ===\n")
log_content = ""
for r in results:
    side = choice(['BUY', 'SELL'])
    qty = 100
    log_content += (f"2025-06-15 {side} {r['symbol']} "
                    f"{qty} @ ${r['latest_price']:.2f}\n")      
    
log_path = Path('trade_log.txt')
log_path.write_text(log_content)
print(f"Trade log written to {log_path}")
print(log_path.read_text().rstrip())