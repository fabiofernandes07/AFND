from os import stat

def getList(value):
    countO = 0
    valueF = []
    for j in value.split("="):
        countO += 1
        if (countO == 2):
            for i in j.split(","):
                valueF.append(i)
    return valueF

def getValueDic(value):
    valueF = []
    for j in value.split(","):
        valueF.append(j)
    return valueF


def setDicEmpty(states):
    transitions = {}
    for j in states :
        print(j)



class state:
    def __init__(self):
        self.name = None
        self.stateNext = None
        self.statePrevious = None

    def get_stateNext(self):
        return self.stateNext
    
    def set_stateNext(self, nextstate):
        self.stateNext = nextstate

    def get_statePrevious(self):
        return self.statePrevious
    
    def set_statePrevious(self, previous):
        self.statePrevious = previous

class Automaton:
    def __init__(self):
        self.finallyState = []
        self.primaryState = None
        self.lastState = None
        self.lenghtState = 0
        self.alphabet = []
        self.transition = {}
        self.states = []
        self.initState = None
    ## Verificação necessária com tratamento dos erros de repetição.
    def repeatVerify(self, data):
        v = []
        for j in data:
            if(j not in v):
                v.append(j)
        return v

    def set_alphabet(self, alfa):
        self.alphabet = self.repeatVerify(alfa)

    def set_states(self, state):
        self.states = self.repeatVerify(state)
        self.states.sort()
        self.alphabet.append("block")
    
    def set_initState(self, state):
        if state in self.states:
           self.initState = state
        else:
            print("Error: Invalid State")
    
    def set_finallyState(self, states):
        states = self.repeatVerify(states)
        for j in states:
            if j in self.states:
                if j not in self.finallyState:
                    self.finallyState.append(j)
        #-> caso precisa-se de adição de print dos estados finais era só colocar um print com a lista.

    #verificação de tratamentos de todas as transições
    def verifyTransitions(self, transitions):
        statesTransitions = []
        for state in transitions:

            boxState = []; statesTransitions.append(state)
            if(state not in boxState and state in self.states):
                boxState.append(state); boxAlpha = []
                for prohi in transitions[state]:
                    boxAlpha.append(prohi)
                    if(prohi in self.alphabet):
                        for i in transitions[state][prohi]:     
                            if(i not in self.states):
                                
                                return False
                    else:
                          
                        return False
                boxAlpha.sort()
                self.alphabet.sort()
                if(boxAlpha != self.alphabet):          
                    return False
            else:
                
                return False
        
        statesTransitions.sort()
        if(statesTransitions != self.states):
            return False
        return True

    def set_transitions(self, transitions):
        #Se passar no teste de verificação atribui essa transição -> transições
        if(self.verifyTransitions(transitions) == True):
            self.transition = transitions
        else:
            print("No return AFND: Default")

    def linkTransitions(self, inc):
        state = self.primaryState
        startAUX = None
        endAUX = None
        if state != None:
            switch = False
            while state.get_stateNext() != None:
                #auxiliares de swap oneInc e twoInc
                oneInc, twoInc = self.applyTran(inc, state)
                if((startAUX and startAUX) == None):
                    startAUX = oneInc
                    endAUX = twoInc
                else:
                    endAUX.set_stateNext(oneInc)
                    if oneInc != None:
                        oneInc.set_statePrevious(endAUX)
                        endAUX = twoInc
                state = state.get_stateNext()
                if(state == None):
                    break
            else: 
                oneInc, twoInc = self.applyTran(inc, state)
                if((oneInc and twoInc) != None):
                    if((startAUX and endAUX) == None):
                        startAUX = oneInc
                        endAUX = twoInc
                    else:
                        endAUX.set_stateNext(oneInc)
                        oneInc.set_statePrevious(endAUX)
                        endAUX = twoInc
            if((startAUX and endAUX) != None):
                state.set_stateNext(startAUX)
                startAUX.set_statePrevious(state)
                self.lastState = endAUX

    #organização das transições através do termo block posto no dicionário, buscando o estado de cada linha e o início e fim do mesmo
    
    ###SESSÃO DE TRATAMENTO E APLICAÇÃO DE TRANSIÇÕES
    
    


    def orgBlock(self, state, initDic, endedDic):
        if((initDic and endedDic) == None):
            initDic = state
            endedDic = state
        else:
            endedDic.set_stateNext(state)
            state.set_statePrevious(endedDic)
            state.set_statePrevious(endedDic)
            endedDic = state
        return initDic,endedDic

    # transição entre os blocks
    def tranBlock(self,actState):
        switch = False
        initDic = None
        endedDic = None
        for j in range(len(self.transition[actState]["block"])):
            newState = state()
            newState.name = self.transition[actState]["block"][j]
            if(j == len(self.transition[actState]["block"])):
                switch = True
            while(self.transition[newState.name]["block"] != []):
                checkState = newState.name
                for j in range(len(self.transition[newState.name]["block"])):
                    if(j>0):
                        newEstado = state()
                        newEstado.name = self.transition[checkState]["block"][j]
                        initDic, endedDic = self.orgBlock(newEstado,initDic,endedDic)
                    else:
                        newState.name = self.transition[newState.name]["block"][j]
                        #print de um novo estado incluso no construtor state
                        initDic, endedDic = self.orgBlock(newState,initDic,endedDic)
                    self.lenghtState += 1
            else:
                if(switch == False):
                    initDic, endedDic = self.orgBlock(newState,initDic,endedDic)
                    self.lenghtState += 1
        return initDic,endedDic
 
    def applyTran(self, inc,actState):    
        startAUX = None
        endAUX = None
        states = actState.name

        for j in range(len(self.transition[states][inc])):
            if(j == 0):

                actState.name = self.transition[states][inc][j]
                #variaveis de abertura de cada linha com transições incluindo o Block
                initBlock, endedBlock = self.tranBlock(actState.name) 
                if((startAUX and endAUX) == None):
                    startAUX = initBlock
                    endAUX = endedBlock
                else:  
                    print(initBlock.name, endedBlock.name)
                    endAUX.set_stateNext(initBlock)
                    initBlock.set_statePrevious(endAUX)
                    endAUX =endedBlock
            else:
                newState = state()
                newState.name = self.transition[states][inc][j]
                initBlock, endedBlock = self.tranBlock(newState.name)
                if((startAUX and endAUX) == None):
                    startAUX = newState
                    endAUX = newState
                else:
                    endAUX.set_stateNext(newState)
                    newState.set_statePrevious(endAUX)
                    endAUX = newState
                if((initBlock and endedBlock) != None):
                    endAUX.set_stateNext(initBlock)
                    initBlock.set_statePrevious(endAUX)
                    endAUX =endedBlock

                self.lenghtState += 1
        if(len(self.transition[states][inc]) == 0):
            self.entryNoFound(actState)
        return startAUX, endAUX

    def entryNoFound(self, state):
        if(state == self.primaryState):
            self.primaryState = self.primaryState.get_stateNext()
        elif(state == self.lastState):
            self.lastState = self.lastState.get_statePrevious()
            self.lastState.set_stateNext(None)
        else:
            n1 = state.get_statePrevious()
            n2 = state.get_stateNext()
            n1.set_stateNext(n2)
            n2.set_statePrevious(n1)
        self.lenghtState += -1


    #SESSÃO STRING 
    def set_Stringfy(self, string):
        for inc in list(set(string)):
            if(inc not in self.alphabet):
                print("'"+ inc +"' not found in alphabet")
                return
            
        if(self.lenghtState == 0):
            if(self.initState == None):
                print("Init State Empty")
                return
            newState = state()
            newState.name = self.initState
            self.primaryState = newState
            self.lastState = newState
            self.lenghtState += 1

        for inc in string:
            self.linkTransitions(inc)
        
        actState = self.primaryState

        if(actState != None):
            while(actState.get_stateNext() != None):
                if(self.verifyAutomaton(actState.name) == True):
                    self.end()
                    return True
                actState = actState.get_stateNext()
            else:

                if(self.verifyAutomaton(actState.name) == True):
                    self.end()
                    return True
                else:
                    print("Recuse")
                    self.end()
                    return False
        else:
            print("Recuse")
            self.end()
            return False



     ## Por fim, verificação do automato para entregar a string a ser aceita   
    def verifyAutomaton(self, state):
        if(state in self.finallyState):
            print("Aceppt")
            return True


    #por fim, zera-se tudo para uma nova leitura de arquivo
    def end(self):
        self.primaryState = None
        self.lastState = None
        self.lenghtState = 0            
