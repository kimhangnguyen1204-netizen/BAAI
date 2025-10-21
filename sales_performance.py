#
# sales, 2025/10/21
# File: sales_performance.py
# Make sales performance report
#
 
# 1. Input
import pandas as pd
df = pd.read_excel('sales_data.xlsx', header=1)
total_bonus_to_pay = 0

print("\nSALES PERFORMANCE REPORT\n")
print("========================\n")

# 2. Process
for x in range(len(df)):
    name = df.loc[x, "Employee_Name"]
    sales = df.loc[x, "Monthly_Sales"]
    target = df.loc[x, "Sales_Target"]
    if sales >= target:
        bonus = sales * 0.1
        kpi = "Target MET"
    else:
        bonus = sales * 0.05
        kpi = "Target NOT MET"
    total_bonus_to_pay += bonus

    # 3. Output
    print(f"{name} : {kpi} | Sales: ${sales:,.0f} | Bonus: ${bonus:,.0f}\n")
print(f"Total Bonuses to Pay: ${total_bonus_to_pay:,.0f}\n")
