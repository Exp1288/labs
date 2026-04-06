a = input("Enter the coordinate (e.g. a1): ")
b = input("Enter the coordinate (e.g. g8): ")

col1 = ord(a[0]) - ord('a') + 1
row1 = int(a[1])

col2 = ord(b[0]) - ord('a') + 1
row2 = int(b[1])

if col1 == col2 or row1 == row2:
    print("The roook beats your figure")
else:
    print("The rook doesn't beat your figure")