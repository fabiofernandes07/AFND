import sys
from automato import pegarValor, Automato, pegarValorDic


arquivo = open('automato.txt', "r")
lista = []
for linha in arquivo:
    linha = linha.strip()
    lista.append((linha))
arquivo.close()

cap = False
transicoes = {}
getDic = []
AFN = Automato()

AFN.alfabeto = pegarValor(lista[0])
AFN.estados = pegarValor(lista[1])



for i in lista:
    if cap == True:
        getDic = pegarValorDic(i)

        if getDic[0] in transicoes : 
            transicoes[getDic[0]].update({getDic[2]: [getDic[1]]})
            print(transicoes)
            print('s')
            print(getDic[0], getDic[2], getDic[1])
        else:
            transicoes[getDic[0]] =  {getDic[2]: [getDic[1]]}
            print(transicoes)
            print('n')
            
        
        
    if i == "transicoes":
        cap = True\


print(getDic[0] in transicoes )