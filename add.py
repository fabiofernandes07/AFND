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
