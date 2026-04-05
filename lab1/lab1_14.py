import numpy as np
import matplotlib.pyplot as plt

x = int(input("Enter the coordinate X: "))
y = int(input("Enter the coordinate Y: "))
if x > 0 and y > 0:
    print("The dot will stay in the first area")
elif x > 0 and y < 0:
    print("The dot will stay in the fourth area")
elif x < 0 and y < 0:
    print("The dot will stay in the third area")
elif x < 0 and y > 0:
    print("The dot will stay in the second area")
plt.scatter(x, y)
plt.axhline(0, color='black') 
plt.axvline(0, color='black')
plt.grid()
plt.title("Coordinates")

plt.show()