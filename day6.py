import pandas as pd

raw_sales_data = {
    'Product': ['Laptop', 'Smartphone', 'Tablet', 'Headphones'],
    'Unit_Sold': [150, 300, 200, 400],
    'Unit_Price': [1000, 500, 300, 100],
    'Total_Revenue': [150000, 150000, 60000, 40000]
}

df_inventory = pd.DataFrame(raw_sales_data)
print("--- Inventory DataFrame (DataFrame created from raw_sales_data) ---")
print(df_inventory)
df_inventory['Total_Revenue'] = df_inventory['Unit_Sold'] * df_inventory['Unit_Price']