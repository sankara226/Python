import pandas as pd

raw_sales_data = {
    'Product': ['Laptop', 'Smartphone', 'Tablet', 'Headphones'],
    'Category': ['Hardware', 'Hardware', 'Hardware', 'Accessory'],
    'Unit_Sold': [150, 300, 200, 400],
    'Unit_Price': [1000, 500, 300, 100]
}

df_inventory = pd.DataFrame(raw_sales_data)
print("--- Inventory DataFrame (DataFrame created from raw_sales_data) ---")
print(df_inventory)
df_inventory['Total_Revenue'] = df_inventory['Unit_Sold'] * df_inventory['Unit_Price']

is_high_price = df_inventory['Unit_Price'] > 400
print ("--- Boolean series (True/False check) ---")
print (is_high_price)

df_high_value = df_inventory[is_high_price]
print("\n--- Filtered Dataframe (Price > $400 )")
print(df_high_value)

df_sorted_revenue = df_inventory.sort_values(by='Total_Revenue', ascending=False)
print("\n--- Sorted DataFrame (Highest Revenue First) ---")
print(df_sorted_revenue)

df_inventory_sorted = df_inventory.sort_values(by='Total_Revenue', ascending=False)

is_low_price = df_inventory_sorted['Unit_Price'] < 400
print ("--- Boolean series (True/False check for low price) ---")
print (is_low_price)

df_low_value_sorted = df_inventory_sorted[is_low_price]
print("\n--- Filtered DataFrame (Low Price from Sorted Inventory) ---")
print(df_low_value_sorted)

df_sorted_revenue = df_inventory.sort_values(by='Total_Revenue', ascending=True)
print("\n--- Sorted DataFrame (Lowest Revenue First) ---")
print(df_sorted_revenue)
category_summary = df_inventory.groupby('Category').sum(numeric_only=True)

print("\n--- Summary by Category) ---")
print(category_summary)

