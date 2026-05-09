import random 
r = []
d = []
a = 0
for i in range(10, 99):
    r.append(i)
for j in range(0, 89):
    if r[j] % 4 == 0 and r[j] % 6 != 0:
        d.append(r[j])
    else:
        pass
print(d)
