import random

def ranker(database, top):
    newDatabase = {}
    for node in database:
        newDatabase[node] = {}
        topSize = [0] * top
        topAdd = [''] * top
        for each in database[node]:
            minimum = min(topSize)
            if database[node][each] > minimum:
                index = topSize.index(minimum)
                topSize[index] = database[node][each]
                topAdd[index] = each
        for size, address in zip(topSize, topAdd):
            newDatabase[node][address] = size
    return newDatabase

def genLocation():
    x, y = random.randint(1, 800), random.randint(1, 500)
    return random.choice([x, -x]), random.choice([y, -y])