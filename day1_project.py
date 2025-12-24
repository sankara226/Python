prev_reading = int("1250")
curr_reading = int("1765")
price_per_unit = 0.15
units_consumed = curr_reading - prev_reading
base_cost = units_consumed * price_per_unit
is_premium_user = True

if units_consumed > 500 and is_premium_user:
    base_cost *= 1.10
    print("Applied 10% surcharge for premium user with high consumption. your new bill is:", base_cost)
else:
    final_bill = base_cost
    print("Applied standard rate for non-premium user with high consumption. your final bill is:", final_bill)
    

print("Your final electricity bill is:", float(base_cost))
    