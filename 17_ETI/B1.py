line = str(input(">> ")).lower().strip()
pos = []
for char in line:
    pos_line = line.replace(char, '')
    pos.append(pos_line)

print(pos)
