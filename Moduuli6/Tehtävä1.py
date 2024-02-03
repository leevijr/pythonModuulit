import random
noMax=True
allDice=[]

def dice():
    return random.randint(1,6)

while noMax:
    currentDice=dice()
    allDice.append(currentDice)
    if currentDice==6:
        noMax=False
        print(allDice)