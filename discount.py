def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Example usage:
original_price = 100
discount_percentage = 25
final_price = calculate_discount(original_price, discount_percentage)
print("Final price after discount:", final_price)


def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompting the user to enter the original price and discount percentage
original_price = float(input("Enter the original price of the item: $"))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculating the final price after applying the discount
final_price = calculate_discount(original_price, discount_percentage)

# Printing the final price after applying the discount or the original price
if final_price != original_price:
    print("Final price after discount: $", final_price)
else:
    print("No discount applied. Final price: $", final_price)
