#
# customer, 2025/10/21
# File: customer_segmetation.py
# MAKE CUSTOMER SEGMENTATION REPORT
#
# 1. Input
import pandas as pd
df = pd.read_excel("customers.xlsx", header = 1)
print(df)
total_vip_revenue = 0
print("\nCUSTOMER SEGMENTATION REPORT")
print("\n=============================\n")

# 2. Process
# VIP CUSTOMERS
print("VIP Customers:")
for x in range(len(df)):
    customer = df.loc[x,"Customer_Name"]
    order = df.loc[x,"Number_of_Orders"]
    purchase = df.loc[x,"Total_Purchases"]
    avg_order = purchase/order 
    if purchase > 10000:
        print(f"- {customer} | Total: ${purchase:,.0f} | Orders: {order} | Avg Order: ${avg_order:,.2f}")
        total_vip_revenue += purchase

# REGULAR CUSTOMERS
print("\nRegular Customers:")
for x in range(len(df)):
    customer = df.loc[x,"Customer_Name"]
    order = df.loc[x,"Number_of_Orders"]
    purchase = df.loc[x,"Total_Purchases"]
    avg_order = purchase/order 
    if purchase >= 5000 and purchase <= 10000:
        print(f"- {customer} | Total: ${purchase:,.0f} | Orders: {order} | Avg Order: ${avg_order:,.2f}\n")

# NEW CUSTOMERS 
print("New Customers:")
for x in range(len(df)):
    customer = df.loc[x,"Customer_Name"]
    order = df.loc[x,"Number_of_Orders"]
    purchase = df.loc[x,"Total_Purchases"]
    avg_order = purchase/order 
    if purchase < 5000:
        print(f"- {customer} | Total: ${purchase:,.0f} | Orders: {order} | Avg Order: ${avg_order:,.2f}")
        
# 3. Output
print(f"\nTotal VIP Revenue: ${total_vip_revenue:,.0f}\n")
