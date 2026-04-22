a = int(input("Enter the first integer number: "))
b = int(input("Enter the second integer number: "))
c = input("Enter the operation sign(*, +, -, /): ")
if c == '+': 
    print(a+b)
elif c == '/': 
    if b == 0:
        print("b != 0")
    else:
        print(a/b) 
elif c == '*': 
    print(a*b) 
elif c == '-': 
    print(a-b) 
else:
    print("Something gone wrong")
