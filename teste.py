import sys


from refactoring import Automaton, getValueDic,  getList, setDicEmpty


arquivo = open('automato.txt', "r")
lista = []
for linha in arquivo:
    linha = linha.strip()
    lista.append((linha))
arquivo.close()

cap = False
transicoes = {}
getDic = []
AFN = Automaton()

alfabeto = getList(lista[0])
estados = getList(lista[1])
estadosFinais = getList(lista[3])
estadoInicial = getList(lista[2])
#setando dicionario vazio
for i in  estados :
    for j in alfabeto :
        if i in transicoes : 
            transicoes[i].update({j : []})
        else:
            transicoes[i] = {j : []}
#setando epsilon
for i in  estados :
    transicoes[i].update({'block' : []})


# print(transicoes)
# print(lista)

for i in lista:
    if i == '':
        break
    if cap == True:
        
        getDic = getValueDic(i)

        if getDic[0] in transicoes : 
            transicoes[getDic[0]].update({getDic[2]: [getDic[1]]})
            # print(transicoes)
            # print('s')
            # print(getDic[0], getDic[2], getDic[1])
        else:
            transicoes[getDic[0]] =  {getDic[2]: [getDic[1]]}
            # print(transicoes)
            # print('n')
    if i == "transicoes":
        cap = True

    


print(transicoes)
# print(alfabeto)
# print(estados)
# print(estadosFinais)
# print(estadoInicial)

AFN.set_alphabet(alfabeto)
print(AFN.alphabet)
AFN.set_states(estados)
print(AFN.states)
AFN.set_initState(estadoInicial[0])
print(AFN.primaryState)
AFN.set_finallyState(estadosFinais)
print(AFN.finallyState)
AFN.set_transitions(transicoes)
print(AFN.transition)

AFN.set_Stringfy('b')

