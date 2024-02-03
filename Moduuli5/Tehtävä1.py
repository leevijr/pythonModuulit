import random
maara = int(input("Montako arpaa heitetään? :) "))
summa=0
for x in range(maara):
    summa+=random.randint(1,6)

print(summa)