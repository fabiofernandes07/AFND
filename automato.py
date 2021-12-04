def pegarValor(valor):
    count1 =0
    valorf =[]
    for j in valor.split("="):
        count1 +=1
        if (count1 == 2):
            for i in j.split(","):
                valorf.append(i)
    return valorf

def pegarValorDic(valor):
    valorf = []
    for i in valor.split(","):
        valorf.append(i)
    return valorf


class state:
    def __init__(self):
        self.name = None
        self.nextState = None
        self.previousState = None

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
    

    def verify_repeat(self, data):
        lis = []
        for i in data:
            if(i not in lis):
                lis.append(i)
        return lis


    def alfa(self, alfabeto):
        self.alfabeto = self.verify_repeat(alfabeto)
