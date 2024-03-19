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
car = Auto("ABC-123", 142)


car.kiihdytä(30)
car.kiihdytä(70)
car.kiihdytä(50)
car.kiihdytä(-200)
print(car.nopeus)