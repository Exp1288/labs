import random 

r = random.randint(1, 10)
ra = random.randint(1, 10)

a = int(input("Enter a number: "))

d = ra - r

if d != 0 and (a - r) % d == 0:
    print("YES, belongs")
else:
    print("NO, doesn't belong")