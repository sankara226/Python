def calculate_bonus(sales_amount, bonus_rate):
    bonus_rate = sales_amount * bonus_rate
    return bonus_rate

sales_rep_a = "Alice"
sales_rep_a_sales = 15000
bonus_a = calculate_bonus(sales_rep_a_sales, 0.10)
print(f"{sales_rep_a} earned a bonus of ${bonus_a:.2f}")

sales_rep_b = "Bob"
sales_rep_b_sales = 20000
bonus_b = calculate_bonus(sales_rep_b_sales, 0.08)
print(f"{sales_rep_b} earned a bonus of ${bonus_b:.2f}")

if sales_rep_a_sales > sales_rep_b_sales:
    print(f"{sales_rep_a} had higher sales than {sales_rep_b}.")
elif sales_rep_b_sales > sales_rep_a_sales:
    print(f"{sales_rep_b} had higher sales than {sales_rep_a}.")
