import random
noMax=True
allDice=[]

max=int(input("Montako sivua nopassa on? "))

def dice(sides):
    return random.randint(1,sides)

while noMax:
    currentDice=dice(max)
    allDice.append(currentDice)
    if currentDice==max:
        noMax=False
        print(allDice)