def troco(listaDeMoedas, valor):
    iteracoes = 0
    valor = valor * 100
    troco = [0]
    aux = 0
    while valor != 0:
        iteracoes += 1
        if valor >= listaDeMoedas[0]:
            valor -= listaDeMoedas[0]
            troco[aux] += 1
            print(valor)
        else:
            aux += 1
            troco.append(0)   
            del listaDeMoedas[0]          
    return (troco,iteracoes)

listaDeMoedas = [100, 25, 10, 5, 1]
valor = 2.89

print(troco(listaDeMoedas, valor))

