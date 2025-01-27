# The Konditorei coffee shop sells coffee at $15.50 a pound plus the cost of shipping. 
# Each order ships for $0.99 per pound + $4.50 fixed cost for overhead. 
# Write a program that calculates the cost of an order.

def calculate_order_total(pounds_of_coffee):
    coffee_price_per_pound = 15.50
    shipping_fee_per_pound = 0.99
    overhead_cost = 4.50

    total = pounds_of_coffee * (coffee_price_per_pound + shipping_fee_per_pound)
    total += overhead_cost
    
    return total

def main():
    print("[Konditorei Coffee Shop]")
    try:
        pounds = float(input("How many pounds of coffee would you like to order? "))
        total_cost = calculate_order_total(pounds)

        print(f"Your order total is ${total_cost:.2f}.")
    except:
        print("Invalid pounds amount.")

if __name__ == "__main__":
    main()


