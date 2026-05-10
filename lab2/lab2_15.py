b = input("enter 10 numbers:")
a = []
d = 0
d1 = 0
c = 0
c1 = 0
for i in range(0, 10):
    if int(b.split(" ")[i]) > 0:
        d += 1
        d1 += int(b.split(" ")[i])
    elif int(b.split(" ")[i]) < 0:
        c += 1
        c1 += int(b.split(" ")[i])
    elif int(b.split(" ")[i]) == 0:
        print("Zero")
    else:
        print("Error")
print("Positive quantity:", d)
print("Positive sum: ", d1)
print("Negative quantity: ", c)
print("Negative sum: ", c1)
