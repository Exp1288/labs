print("The program determines is triangle equalateral or not")
a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second of the triangle: "))
c = float(input("Enter the third of the triangle: "))
if a == b or b == c or c == a:
    print("The triangle is equalateral")
elif a == b and c != b or a:
    print("The triangle is isosceles")
else: 
    print("The triangle is scalene")