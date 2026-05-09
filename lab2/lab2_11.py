a = str(input("Enter a few numbers: "))
b = 0
c = 0
d = 0

for i in range(0, len(a.split(" "))):
    if int(a.split()[i]) > 0:
        b += 1
    elif int(a.split()[i]) == 0:
        c += 1
    elif int(a.split()[i]) < 0:
        d += 1
    else: 
        print("Enter numbers!")
print("Positive: ", b)
print("Zeros: ", c)
print("Negative: ", d)
