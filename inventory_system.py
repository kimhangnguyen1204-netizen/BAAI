#
# inventory, 2025/10/21
# File: inventory_system.py
# Make inventory reorder report
#

# 1. Input
import pandas as pd
df = pd.read_excel("inventory.xlsx", header=1)
total_reorder_cost = 0

print("\nINVENTORY REORDER REPORT")
print("========================")
print("Products Needing Reorder:\n")

# 2. Process
for x in range(len(df)):
    name = df.loc[x, "Product_Name"]
    min_stock = df.loc[x, "Minimum_Stock"]
    stock = df.loc[x, "Current_Stock"]
    price = df.loc[x,"Unit_Price"]
    if stock < min_stock:
        reorder = min_stock - stock + 10
        reorder_cost = reorder * price
        total_reorder_cost += reorder_cost
        print(f"{name} : Reorder {reorder} units | Cost: ${reorder_cost:,.0f}")
print(f"\nTotal Reorder Cost: ${total_reorder_cost:,.0f}")

for x in range(len(df)):
    name = df.loc[x, "Product_Name"]
    min_stock = df.loc[x, "Minimum_Stock"]
    stock = df.loc[x, "Current_Stock"]
    price = df.loc[x,"Unit_Price"]        
    if stock > min_stock:
        print(f"Products in Good Stock: {name}\n")


# 3. Output
