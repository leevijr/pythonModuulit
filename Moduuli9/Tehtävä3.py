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

car.matka=40
print(car.matka)
car.kiihdytä(20)
car.kulje(1.5)
car.kiihdytä(20)
print(car.matka)