etapa1 = [['A', 'B'], ['C', 'D'], ['E', 'F'], ['G', 'H'], ['I', 'J'], ['K', 'L'], ['M', 'N'], ['O', 'P']]

etapa2 = []
for j in etapa1:
    ### PRIMEIRA FASE ###
    result = input("").strip().split(' ')
    if int(result[0]) > int(result[1]):
        etapa2.append(j[0])
    if int(result[1]) > int(result[0]):
        etapa2.append(j[1])

etapa2 = [[etapa2[0], etapa2[1]], [etapa2[2], etapa2[3]], [etapa2[4], etapa2[5]], [etapa2[6], etapa2[7]]]

etapa3 = []
for j in etapa2:
    ### SEGUNDA FASE ###
    result = input("").strip().split(' ')
    if int(result[0]) > int(result[1]):
        etapa3.append(j[0])
    if int(result[1]) > int(result[0]):
        etapa3.append(j[1])
    
etapa3 = [[etapa3[0], etapa3[1]], [etapa3[2], etapa3[3]]]

semi = []
for j in etapa3:
    result = input("").strip().split(' ')
    if int(result[0]) > int(result[1]):
        semi.append(j[0])
    if int(result[1]) > int(result[0]):
        semi.append(j[1])

final = input("").strip().split(' ')
if int(final[0]) > int(final[1]):
    print(semi[0])
if int(final[1]) > int(final[0]):
    print(semi[1])
