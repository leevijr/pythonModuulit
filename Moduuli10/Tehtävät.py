import random
class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def siirry_kerrokseen(self, kohde):
        if kohde >= self.alin and kohde <= self.ylin:
            while not self.kerros == kohde:
                if self.kerros < kohde:
                    self.kerros_ylös()
                elif self.kerros > kohde:
                    self.kerros_alas()
    def kerros_ylös(self):
        self.kerros+=1
    def kerros_alas(self):
        self.kerros+=-1

ekaHissi = Hissi(0,60)
ekaHissi.siirry_kerrokseen(36)
print(ekaHissi.kerros)


class Talo:
    def __init__(self, alin, ylin, hissitMaara):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []
        for x in range (hissitMaara):
            self.hissit.append(Hissi(alin, ylin))
    def aja_hissia(self, numero, kohde):
        self.hissit[numero].siirry_kerrokseen(kohde)

    def PALOHALYTYS(self):
        for x in self.hissit:
            x.siirry_kerrokseen(0)

linna = Talo(0,60,24)
linna.aja_hissia(4, 48)
print(linna.hissit[4].kerros)
linna.PALOHALYTYS()
print(linna.hissit[4].kerros)







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
class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot
    def tunti_kuluu(self):
        for x in self.autot:
            x.kulje(1)
    def tulosta_tilanne(self):
        for x in self.autot:
            print(f"Auto {x.rekisteri} on mennyt {x.matka} kilometriä!")
        print("\n")
    def kilpailu_ohi(self):
        for x in self.autot:
            if x.matka >= self.pituus:
                return True
        return False

dumbcarlist=[]
for x in range(10):
    dumbcarlist.append(Auto(x, 200))

tyhma = Kilpailu("Suuri romuralli", 8000, dumbcarlist)


tunnit=0
while not tyhma.kilpailu_ohi():
    for x in tyhma.autot:
        x.kiihdytä(random.randint(-5, 25))
    tyhma.tunti_kuluu()
    if tunnit % 10 == 0:
        tyhma.tulosta_tilanne()
    tunnit+=1

tyhma.tulosta_tilanne()
winner=[0,0]
for x in tyhma.autot:
    if x.matka > winner[1]:
        winner[0]=x.rekisteri
        winner[1]=x.matka
print(f"Voittaja on! {winner[0]} ja hän kulki {winner[1]} kilometriä!")