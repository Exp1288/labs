a = 3
c = 0
while a < 200:
    a += 1
    if a % 3 == 0:
        c += 1
    else:
        pass
print("There's quantity of numbers that are multiples of 3 and aren't bigger than 200: ")
print(c)