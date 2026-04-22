import math as m
print("ax^2 + bx + c = 0")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
D = b**2 - 4*a*c 
if D<0:
    print("No roots")
elif D == 0:
    x = -b / (2*a)
    print(f"One root x: {x}")
elif D>0:
    x1 = (-b + m.sqrt(D)) / (2*a)
    x2 = (-b - m.sqrt(D)) / (2*a)
    print(f"Two roots x1:{x1}, x2: {x2}")