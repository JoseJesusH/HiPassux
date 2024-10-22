def process_order(order):
    total_price = 0
    discount = 0

    for item in order.items:
        if item.category == "Electronics":
            if item.price > 1000:
                discount += item.price * 0.1
            elif item.price > 500:
                discount += item.price * 0.05
        else:
            if item.price > 100:
                discount += item.price * 0.02

    try:
        total_price = sum([item.price for item in order.items]) - discount
        if total_price < 0:
            raise ValueError("Total price cannot be negative")
    except ValueError as e:
        print(f"Error processing order: {e}")
    
    return total_price
