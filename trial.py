# === PRODUCT DISCOUNT CALCULATOR ===

# Data Provided (from the slide)
products = [
    {"name": "Laptop", "price": 1200, "category": "Electronics"},
    {"name": "Shirt", "price": 45, "category": "Clothing"},
    {"name": "Phone", "price": 800, "category": "Electronics"},
    {"name": "Shoes", "price": 120, "category": "Clothing"},
    {"name": "Tablet", "price": 350, "category": "Electronics"},
    {"name": "Jacket", "price": 95, "category": "Clothing"},
    {"name": "Book", "price": 25, "category": "Books"},
    {"name": "Headphones", "price": 150, "category": "Electronics"}
]

# --- Tracking variables (no len() used) ---
total_original = 0.0
total_discount_amount = 0.0
total_final = 0.0
total_products = 0  # we’ll count manually in the loop

# Bonus tracking (optional)
highest_disc_amt = -1.0
highest_disc_name = ""
sum_discount_pct = 0.0  # to compute average discount % (simple mean over products)
category_counts = {}
most_expensive_name, most_expensive_final = "", -1.0
cheapest_name, cheapest_final = "", 10**18  # large sentinel

print("=== PRODUCT DISCOUNT CALCULATOR ===\n")

# --- Main processing loop ---
for p in products:
    name = p["name"]
    price = float(p["price"])
    category = p["category"]

    # Determine discount rate by rules
    if category == "Electronics":
        if price >= 1000:
            rate = 0.20
        elif price >= 500:
            rate = 0.15
        else:
            rate = 0.10
    elif category == "Clothing":
        if price >= 100:
            rate = 0.25
        else:
            rate = 0.15
    elif category == "Books":
        rate = 0.10
    else:
        rate = 0.0  # fallback if an unknown category appears

    # Calculations
    disc_amt = price * rate
    final_price = price - disc_amt

    # Print product block
    print(f"Product: {name}")
    print(f"Category: {category}")
    print(f"Original Price: ${price:.2f}")
    print(f"Discount: {int(rate*100)}%")
    print(f"Final Price: ${final_price:.2f}")
    if rate >= 0.20:
        print("(Clearance)")
    print()

    # Update totals
    total_original += price
    total_discount_amount += disc_amt
    total_final += final_price
    total_products += 1

    # Bonus tracking
    if disc_amt > highest_disc_amt:
        highest_disc_amt = disc_amt
        highest_disc_name = name

    sum_discount_pct += (rate * 100.0)

    # Count categories (no len needed)
    if category in category_counts:
        category_counts[category] += 1
    else:
        category_counts[category] = 1

    # Track most expensive / cheapest after discount
    if final_price > most_expensive_final:
        most_expensive_final = final_price
        most_expensive_name = name
    if final_price < cheapest_final:
        cheapest_final = final_price
        cheapest_name = name

# --- Summary ---
print("=== SUMMARY ===")
print(f"Total Products : {total_products}")
print(f"Total Original Price: ${total_original:.2f}")
print(f"Total Discount : ${total_discount_amount:.2f}")
print(f"Total Final Price: ${total_final:.2f}")

# --- Bonus outputs (optional) ---
if total_products > 0:
    avg_discount_pct = sum_discount_pct / total_products
    print("\n--- Bonus ---")
    print(f"Highest Discount: {highest_disc_name} (${highest_disc_amt:.2f})")
    print(f"Average Discount (%): {avg_discount_pct:.2f}%")
    print("Count by Category:")
    for cat in category_counts:
        print(f"  - {cat}: {category_counts[cat]}")
    print(f"Most Expensive (after discount): {most_expensive_name} (${most_expensive_final:.2f})")
    print(f"Cheapest (after discount): {cheapest_name} (${cheapest_final:.2f})")
    print(f"Total Savings (customer): ${total_discount_amount:.2f}")
