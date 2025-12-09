import random

# This whhere the user will give his response
answer = input("Can't decide? Type 'yes' to flip a coin: ")

if answer.lower() == "yes":
    num = random.randint(0, 1)  # 0 or 1
    if num == 0:
        print("Heads")
    else:
        print("Tails")
else:
    print("Okay, no coin flip.")








