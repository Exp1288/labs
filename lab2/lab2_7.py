from random import randint
import random 
r = []
a = 0
for i in range(1, 20):
    r.append(random.randint(1, 10))
for j in range(1, 10):
    if r[j] % 3 == 0:
        a += r[j]
    else:
        pass
print(r)
print("Summ: ", a)