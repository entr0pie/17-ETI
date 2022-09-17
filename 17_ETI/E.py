times = [['A', 'B'], ['C', 'D'], ['E', 'F'], ['G', 'H'], ['I', 'J'], ['K', 'L'], ['M', 'N'], ['O', 'P']]
# times = [['A', 'B'], ['C', 'D'], ['E', 'F'], ['G', 'H']]

etapa_2 = []
etapa_3 = []
etapa_4 = []

def criaTime(times):
    winners = []
    jogo = []
    for time in times:
        result = input("").strip().split()
        if int(result[0]) > int(result[1]):
            jogo.append(time[0])
            print("Jogo Atual: {}".format(jogo))
        else:
            print(result[1])
            jogo.append(time[1])
            print("Jogo atual: {}".format(jogo))
        if len(jogo) > 1:
            winners.append(jogo)
            print("Lista Jogo Tamanho: {}".format(len(jogo)))

    return winners

etapa_1 = criaTime(times)
print("Etapa 1 {}".format (etapa_1))
etapa_2 = criaTime(etapa_1)
print(etapa_2)
etapa_3 = criaTime(etapa_2)
print(etapa_3)
etapa_4 = criaTime(etapa_3)
print(etapa_4)
