#
# Hang, 2025/10/22
# File: Hang_Correlation_Analysis.py
# Apply correlation analysis to business problems
# 
# 
# 1. Input
import pandas as pd 
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Correlataion_Analysis_Data.csv")

df.info()
correlation_matrix = df.iloc[:,1:6].corr()

print(correlation_matrix.round(3))
# correlation, pvalue =stats.pearsonr(df['Marketing_Spend'],df['Sales_Revenue'])

# 2. Process

# df[].corr()
# print(df.isnull().sum())
# print(df.isnull().sum().sum())

# 3. Output
# print("Data loated succesfully")
# print(f"Dataset shape:{df.shape}")

# print(f'Correlation: {correlation:.2f}')
# print(f'P value: {pvalue:.4e}')
sns.heatmap(correlation_matrix)
plt.tight_layout()
plt.title("Hang is the most intelligent person in the world")
plt.show()
