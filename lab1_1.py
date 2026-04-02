import math 
a = float(input("Enter the value of a: "))
#We transform the angle from radians to degrees
a = a * 180 / math.pi
z = 2 * (math.sin(3 * math.pi - 2 * a))**2 * (math.cos(5 * math.pi + 2 * a))**2
print("The value of z is: ", z)