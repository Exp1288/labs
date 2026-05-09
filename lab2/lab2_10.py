a = 0
b = []
for i in range(0, 100):
    if i % 7 == 0:
        a += i
        b.append(i)
    else:
        pass
print("Length: ", len(b))
print("Summ: ", a)