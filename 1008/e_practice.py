import math

is_good = True
price = 1000000

print("Price of a house is $1M.")
if is_good:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")