import random
class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0
    def kiihdytä(self, kmh):
        if self.nopeus+kmh > self.huippunopeus:
            self.nopeus=self.huippunopeus
        elif self.nopeus+kmh < 0:
            self.nopeus=0
        else:
            self.nopeus+=kmh

    def kulje(self, tunti):
        self.matka+=self.nopeus*tunti
car = Auto("ABC-123", 142)
carList=[]
for x in range(10):
    carList.append(Auto(f"ABC-{x+1}", random.randint(100, 200)))

winnerFound=0
while not winnerFound:
    for x in range(10):
        carList[x].kiihdytä(random.randint(-10,15))
        carList[x].kulje(1)
        print(carList[x].rekisteri, carList[x].matka)
        if carList[x].matka >= 10000:
            winnerFound=carList[x].rekisteri
            break
print(f"Voittaja on! {winnerFound}")