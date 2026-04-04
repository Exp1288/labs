A = float(input("Enter the number A: "))
B = float(input("Enter the number B: "))
if A % B == 0:
    print("B is A divisor of A")
if B % A == 0:
    print("A is a divisor of B")
elif A % B == 0 and B % A == 0:
    print("B is a divisor of A and A is a divisor of B")
else:
    print("Something gone wrong")