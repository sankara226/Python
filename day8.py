import pandas as pd

messy_data = {
    'Region': ['East', 'West', 'Central', 'East', 'West'],
    'Sales_Rep': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Bonus_Rate': [0.10, 0.15, None, 0.12, 0.10], 
    'Total_Sales': [15000, 22000, 10000, None, 18000]
}

# --- 1. Cleaned Data (Starting Point) ---
# FIX: Use 'messy_data' variable name and [] for dropna check
df_analysis = pd.DataFrame(messy_data).dropna() 
print("--- 1. Cleaned Data (Starting Point) ---")
print(df_analysis)

# --- 2. Calculated Expected Bonus ---
# FIX: Use square brackets [] for column assignment and access
df_analysis['Expected_Bonus'] = df_analysis['Total_Sales'] * df_analysis['Bonus_Rate']
print("\n--- 2. Calculated Expected Bonus ---")
print(df_analysis)

# --- 3. Regional Sales Summary (Groupby) ---
# FIX: Use square brackets [] for column access after groupby
regional_summary = df_analysis.groupby('Region')['Total_Sales'].sum().reset_index()
regional_summary = regional_summary.sort_values(by='Total_Sales', ascending=False)
print("\n--- 3. Regional Sales Summary (Groupby) ---")
print(regional_summary)

# --- 4. Top Performing Region ---
# FIX: Use square brackets [] for column access
top_sales = regional_summary['Total_Sales'].iloc[0] 
df_top_region = regional_summary[regional_summary['Total_Sales'] == top_sales]
print("\n--- 4. Top Performing Region ---")
print(df_top_region)

# --- 5. Exporting the Final Report ---
df_analysis.to_excel("Sales_Report.xlsx", index=False)
print("\n--- 5. Analysis Complete ---")
print("Final report saved to 'Sales_Report.xlsx' (File will be generated in your project folder).")