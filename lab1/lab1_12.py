a = int(input("Enter the price of the purchase: "))
if a >= 200:
    a = a - (a * 0.03)
    print("with 3% discount")
else:
    a = a
print("Your final price is", a)