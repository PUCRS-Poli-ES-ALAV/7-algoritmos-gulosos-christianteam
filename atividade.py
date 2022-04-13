def preenche(posAt, tamanho):
    

def nrainhas(tamanho, rainhas):
    linhas = [0]*tamanho #Cria uma lista com X (tamanho) zeros
    mat = [linhas]*tamanho #Cria uma matriz com base na entrada de "linha"
    nRainhasRestantes = tamanho
    while(nRainhasRestantes > 0):
        posAt = (0,0)
        achou = False
        while(achou == False):
            if(mat[posAt[0]][posAt[1]] == 0):
                mat[posAt[0]][posAt[1]] = -1
                preenche(posAt, tamanho)
                achou = True    
            if(posAt[0] < tamanho-1 and posAt[1] < (tamanho-1)) #impede que o posAt aponte para uma posisão invalida
                if(posAt[0] < tamanho-1):
                    posAt[0]+=1
                else:
                    posAt[1]+=1
                    posAt[0] = 0
            else:
                #F****
    #print(mat)

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

def intervaloTerminator(listaDeIntervalos):
    maiorAt = -2147483648
    res = []
    for intervalo in listaDeIntervalos:
        if(intervalo[0] > maiorAt):
            res.append(intervalo)
            maiorAt = intervalo[1]

    return res

print(troco(listaDeMoedas, valor))
print("\n\n____________________________\n\n")
lista = [(4,5),(2,4),(1,6),(6,7),(4,8),(7,10),(9,11),(9,12),(3,13),(13,14)]
lista.sort(key=lambda tup: tup[1]) #Organiza a lista baseado no segundo item das tuplas
print(lista)
print(intervaloTerminator(lista))

nrainhas(5,5)
