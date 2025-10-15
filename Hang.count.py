#
# Hang.count, 2025/10/15
# File: Hang.count.py
# Short description of the task
#

# 1. Input
order_values = [120,450,80,300,650]
total_revenue = 0 
order_count = 0
# 2. Process
for order in order_values:
    order_count += 1
    total_revenue += order
    print(f'processing order: ${order}')
    
print(f"\nTotal revenue: ${total_revenue}") 
print(f"Total number of orders: {order_count}")
# 3. Output