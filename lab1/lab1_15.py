def check(x,y):
    for i in range(0, 4):
        if x == list[0][i] and b % 2 == 0:
            square = "white"
        elif x == list[0][i] and b % 2 != 0:
            square = "black"
        if x == list[1][i] and b % 2 == 0:
            square = "black"
        elif x == list[1][i] and b % 2 != 0:
            square = "white"
    return square

print("Enter coordinates of the first square: ")
a = str(input("The first coordinate (a-h): "))
b = int(input('The second coordinate (1-8): '))

print("Enter coordinates of the second square: ")
c = str(input("The first coordinate (a-h): "))
d = int(input('The second coordinate (1-8): '))

list = [['a', 'c', 'e', 'g'], ['b', 'd', 'f', 'h']]
res = check(a, b)
res2 = check(c, d)
if res == res2:
    print("Squares are both", res)
else:
    print("Squares are both", res2)
