container = input("").split(' ')
A, B, C = int(container[0]), int(container[1]), int(container[2])
barco = input("").split(' ')
X, Y, Z = int(barco[0]), int(barco[1]), int(barco[2])

cap_a = X // A
cap_b = Y // B
cap_c = Z // C

cap_total = cap_a * cap_b * cap_c
print(cap_total)