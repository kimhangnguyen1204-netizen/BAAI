#
# Hang, 2025/10/08
# File: Hang_excel.py
# Caculate sum of column in Excel file
#
#
import pandas as pd

# 1. Input
df = pd.read_excel('Financial_Sample.xlsx')
# 2. Process
sum = df.select_dtypes(include='number').sum()
df_with_total = pd.concat([df,pd.DataFrame([sum])],ignore_index=True)
df_with_total.to_excel("Financial_Sample.xlsx", index=False)
# 3. Output
print(f'sum{sum}')
print(df_with_total)