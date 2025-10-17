# Hang, 2025/10/15
# File: Hang_miniproject.py
# Short description of the task

# 1. Input
products = [{"name": "Laptop", "price": 1200, "category": "Electronics"},
{"name": "Shirt", "price": 45, "category": "Clothing"},
{"name": "Phone", "price": 800, "category": "Electronics"},
{"name": "Shoes", "price": 120, "category": "Clothing"},
{"name": "Tablet", "price": 350, "category": "Electronics"},
{"name": "Jacket", "price": 95, "category": "Clothing"},
{"name": "Book", "price": 25, "category": "Books"},
{"name": "Headphones", "price": 150, "category": "Electronics"}]
# Variables
total_original = 0
total_discount_amount = 0
total_final = 0
total_products = 0
# Level 1
highest_discount_amount = 0
highest_product = " "
total_discount_percent = 0
# Level 2
category_count = {}
most_expensive_name = None
most_expensive_final = None
cheapest_name = None
cheapest_final = None


print("=== PRODUCT DISCOUNT CALCULATOR ===\n") 

# 2. Process
#Level 0 - Use for loop to process each product
for p in products: 
    name = p["name"]
    price = p["price"]
    category = p["category"]
   # Determine discount rate 
    if category == "Electronics":
        if price >= 1000:
            discount_rate = 0.20
        elif price >= 500:
            discount_rate = 0.15
        else:
            discount_rate = 0.10

    elif category == "Clothing":
        if price >= 100:
            discount_rate = 0.25
        else:
            discount_rate = 0.15

    elif category == "Books":
        discount_rate = 0.10
        
    # Calculate price
    discount_amount = price * discount_rate
    final_price = price - discount_amount

    total_original += price
    total_discount_amount += discount_amount
    total_final += final_price
    total_products += 1 

    # Level 1 - product with highest discount amount & average discount percentage
    if highest_discount_amount < discount_amount:
        highest_discount_amount = discount_amount
        highest_discount_name = name
    total_discount_percent += discount_rate * 100
    average_discount_percent = total_discount_percent / total_products

    # Level 2 - category counts & cheapest and most expensive products
    if category in category_count:
        category_count[category] += 1
    else:
        category_count[category] = 1
    if most_expensive_final is None or final_price > most_expensive_final:
        most_expensive_final = final_price
        most_expensive_name = name
    if cheapest_final is None or final_price < cheapest_final:
        cheapest_final = final_price
        cheapest_name = name

    # Level 3 - clearance tag
    if discount_rate >= 0.20:
        print("(Clearance)")
    print()

    # Level 0 - Output for each product 
    print("Product:", name)
    print("Category:", category)
    print(f"Original Price: ${price:.2f}")
    print(f"Discount: {discount_rate*100:.0f}%")
    print(f"Final Price: ${final_price:.2f}\n")

# 3. Output

# Level 0 output 
print(" === SUMMARY ===")
print(f"Total Products : {total_products}")
print(f"Total Original Price: ${total_original:.2f}")
print(f"Total Discount : ${total_discount_amount:.2f}")
print(f"Total Final Price: ${total_final:.2f}\n")

# Level 1 output
print("=== LEVEL 1 OUTPUT ===")
print(f"Product with Highest Discount Amount: {highest_discount_name}, Amount: ${highest_discount_amount:.2f}")
print(f"Average Discount Percentage: {average_discount_percent:.2f}%")

# Level 2 output   
print("\n=== LEVEL 2 OUTPUT ===")
print("Category Counts:")
for count in category_count:
    print(f"{count}: {category_count[count]}")
print(f"Most Expensive Product: {most_expensive_name}, Price: ${most_expensive_final:.2f}")
print(f"Cheapest Product: {cheapest_name}, Price: ${cheapest_final:.2f}")

# Level 3 output 
print("\n=== LEVEL 3 OUTPUT ===")
print(f"Total Saving For Customer: ${total_discount_amount:.2f}")
