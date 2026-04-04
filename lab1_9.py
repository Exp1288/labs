print("The program determines is triangle equalateral or not")
a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second of the triangle: "))
c = float(input("Enter the third of the triangle: "))
if a+b>c and a+c>b and b+c>a:
    print("The triangle exist")
else:
    print("The triangle doesn't exist")