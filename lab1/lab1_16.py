a = int(input("Enter a four-digit number: "))
a = str(a)
b = list(a)
b.reverse()
if len(b) > 4 or len(b) < 4:
    print("that number is bigger or lower than four-digit")
    quit()
if list(a) == b:
    print("It's a palindrome")
else:
    print("It isn's a palindrome")