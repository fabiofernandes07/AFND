
def pegarValor(valor):
    count1 =0
    valorf =[]
    for j in valor.split("="):
        count1 +=1
        if (count1 == 2):
            for i in j.split(","):
                valorf.append(i)
    return valorf

class Automato:
    def __init__(self):
        self.alfabeto = []
        self.transicoes = {}
        self.estados = []
        self.estadoInicial = None
        self.estadosFinais = []
        self.primeiro_estado = None
        self.ultimo_estado = None
        self.quantidade_estados = 0
    