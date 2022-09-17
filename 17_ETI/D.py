nmax = int(input(""))
operation = str(input("")).strip().split(' ')
A, op, B = int(operation[0]), operation[1], int(operation[2])

if op == '+':
    result = A + B

if op == "*":
    result = A * B 

if result > nmax:
    print("OVERFLOW")

else:
    print("OK")