def place_order(symbol: str , side: str, quantity: float):
    print(f"Placing {side.upper()} order:" +   
          f" {quantity} units of {symbol.upper()}")


def cancel_order(order_id: int):
    print(f"Cancelling order #{order_id}")