

N = int(input(""))
coelhos, ratos, sapos = 0,0,0

for i in range(N): 
    animal_info = input("").strip().split(' ')
    qtd, tipo = int(animal_info[0]), animal_info[1].upper()
    if qtd >= 1 and qtd <= 15:
        if tipo == "C":
            coelhos += qtd
        if tipo == "R":
            ratos += qtd
        if tipo == "S":
            sapos += qtd


total = coelhos + ratos + sapos
print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(coelhos))
print("Total de ratos: {}".format(ratos))
print("Total de sapos: {}".format(sapos))

p_coelhos = coelhos / total * 100
p_ratos = ratos / total * 100
p_sapos = sapos / total * 100

print("Percentual de coelhos: {:.2f} %".format(p_coelhos))
print("Percentual de ratos: {:.2f} %".format(p_ratos))
print("Percentual de sapos: {:.2f} %".format(p_sapos))
