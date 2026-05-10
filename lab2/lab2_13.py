a = 0
b = int(input("Enter the end: "))
for i in range(3, b):
    if i % 3 == 0:
        a += 1
    else:
        pass
print("There's quantity of numbers that are multiples of 3, from 3 to", b)
print(a)