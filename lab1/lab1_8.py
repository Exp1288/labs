print("The program determines is triangle equalateral or not")
a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second of the triangle: "))
c = float(input("Enter the third of the triangle: "))
#does the triangle exist?
if a+b>c and a+c>b and b+c>a:
    if a == b and b == c and c == a:
        print("The triangle is equalateral")
    elif a == b and c != b and c != a:
        print("The triangle is isosceles")
    elif a != b and c != b and a != c: 
        print("The triangle is scalene")
    else:
        print("Something gone wrong")
else:
    print("That triangle doesn't exist")