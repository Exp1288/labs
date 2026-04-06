def joinus(x, y, z):
    v = map(str, [x,y,z])
    print("".join(v))

a = int(input("Enter a three-digit number: "))
a = str(a)
a = list(a)
if len(a) > 3 or len(a) < 3:
    print("ENTER A THREE-DIGIT NUMBER!")
    quit()
print("All possible combinations:")
joinus(a[0], a[1], a[2])
joinus(a[1], a[0], a[2])
joinus(a[0], a[2], a[1])
joinus(a[2], a[0], a[1])
joinus(a[2], a[1], a[0])
joinus(a[1], a[2], a[0])

