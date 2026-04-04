print("Program to calculate all trigonometric functions for Angle A")
import math
def csc(x):
    return 1 / math.sin(x)
A = float(input("Enter the value of Angle A in degrees: "))
# Convert angle from degrees to radians
A_rad = math.radians(A)
A_sin = math.sin(A_rad)
A_cos = math.cos(A_rad)
A_tan = math.tan(A_rad)
A_csc = csc(A_rad)
print(f"sin(A) = {A_sin}")
print(f"cos(A) = {A_cos}")
print(f"tan(A) = {A_tan}")
print(f"csc(A) = {A_csc}")