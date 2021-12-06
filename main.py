import sys
from AFND import Automaton, getValueDic,  getList, setDicEmpty

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

#setando o automato
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
    
#preenchendo dicionario
for i in lista:
    if i == '':
        break
    if cap == True:
        
        getDic = getValueDic(i)

        if getDic[0] in transicoes : 
            transicoes[getDic[0]].update({getDic[2]: [getDic[1]]})
        else:
            transicoes[getDic[0]] =  {getDic[2]: [getDic[1]]}
    if i == "transicoes":
        cap = True 

AFN.set_alphabet(alfabeto)
AFN.set_states(estados)
AFN.set_initState(estadoInicial[0])
AFN.set_finallyState(estadosFinais)
AFN.set_transitions(transicoes)

entrada = input(str("Digite a cadeia de entrada: "))

AFN.set_Stringfy(entrada)

