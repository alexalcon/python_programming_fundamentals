"""
trading_lists_demo.py
Demonstrates all Chapter 3 list concepts applied to algo trading.
"""

# dashed lines for better readability of output
thick_dash = "━" * 73 
thin_dash = "─" * 73

# ─── 1. define a list (a watchlist of stock symbols) ───
print(thick_dash)
print(f"1. define a list (a watchlist of stock symbols)")
print(thick_dash)
watchlist = ['msft', 'aapl', 'tsla', 'goog']
print(f"Initial watchlist: {watchlist}")
print(thin_dash)

# ─── 2. access elements by index and negative index ───
print()
print(thick_dash)
print("2. access elements by index and negative index")
print(thick_dash)
print(f"First symbol: {watchlist[0].upper()}")
print(f"Last symbol: {watchlist[-1].upper()}")
print(thin_dash)

# ─── 3. use individual values from the list ───
print()
print(thick_dash)
print("3. use individual values from the list")
print(thick_dash)
top_pick = watchlist[0].upper()
message = f"Today's top pick is {top_pick}"
print(f"Updated watchlist: {message}")
print(thin_dash)

# ─── 4. modify an element (rebalance) ───
print()
print(thick_dash)
print("4. modify an element (rebalance)")
print(thick_dash)
print(f"Replacing {watchlist[2].upper()} with NVDA...")
watchlist[2] = 'nvda'
print(f"Updated watchlist: {watchlist}")
print(thin_dash)

# ─── 5. append a new symbol ───
print()
print(thick_dash)
print("5. append a new symbol")
print(thick_dash)
watchlist.append('amzn')
print(f"Appended AMZN: {watchlist}")
print(thin_dash)

# ─── 6. insert at a specific position ───
print()
print(thick_dash)
print("6. insert at a specific position")
print(thick_dash)
watchlist.insert(0, 'meta')
print(f"Inserted META at front: {watchlist}")
print(thin_dash)

# ─── 7. remove by index with the 'del' statement ───
print()
print(thick_dash)
print("7. remove by index with the 'del' statement")
print(thick_dash)
del watchlist[3]
print(f"Deleted index 3: {watchlist}")
print(thin_dash)

# ─── 8. pop the last item ───
print()
print(thick_dash)
print("8. pop the last item")
print(thick_dash)
last_removed = watchlist.pop()
print(f"Popped last: {last_removed.upper()}")
print(f"Watchlist now: {watchlist}")
print(thin_dash)

# ─── 9. pop from a specific position ───
print()
print(thick_dash)
print("9. pop from a specific position")
print(thick_dash)
first_removed = watchlist.pop(0)
print(f"Popped first: {first_removed.upper()}")
print(f"Watchlist now: {watchlist}")
print(thin_dash)

# ─── 10. remove by value ───
print()
print(thick_dash)
print("10. remove by value")
print(thick_dash)
watchlist.append('goog')
print(f"Before remove: {watchlist}")
watchlist.remove('goog')
print(f"Removed GOOG by value: {watchlist}")
print(thin_dash)

# ─── 11. sort temporarily with the sorted() function ───
print()
print(thick_dash)
print("11. sort temporarily with the sorted() function")
print(thick_dash)
print(f"Sorted view: {sorted(watchlist)}")
print(f"Original order preserved: {watchlist}")
print(thin_dash)

# ─── 12. sort permanently with the sort() method ───
print()
print(thick_dash)
print("12. sort permanently with the sort() method")
print(thick_dash)
watchlist.sort()
print(f"Permanently sorted: {watchlist}")
print(thin_dash)

# ─── 13. reverse the list ───
print()
print(thick_dash)
print("13. reverse the list")
print(thick_dash)
watchlist.reverse()
print(f"Reversed order: {watchlist}")
print(thin_dash)

# ─── 14. find the length() function ───
print()
print(thick_dash)
print("14. find the length() function")
print(thick_dash)
print(f"Number of symbols in watchlist: {len(watchlist)}")
print(thin_dash)