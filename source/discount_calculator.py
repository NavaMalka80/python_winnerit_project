
def calculate_discount(price,discount_percent):

    if price < 0 or discount_percent < 0:
        raise ValueError("Price and discount must be non-negative")
    final_price = price * (1- discount_percent/100)
    return final_price