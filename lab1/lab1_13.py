a = int(input('Enter your hight(in cm): '))
b = int(input("Enter your weight: "))
opt = a - 100
if opt < b:
    print("You're fat")
elif opt > b:
    print("You're thin")
else:
    print("You're normal")