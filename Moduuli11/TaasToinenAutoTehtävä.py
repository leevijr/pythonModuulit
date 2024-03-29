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


class Sähköauto(Auto):
    def __init__(self, rekisteri, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteri, huippunopeus)
        self.akkukapasiteetti=akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteri, huippunopeus, bensatankki):
        super().__init__(rekisteri, huippunopeus)
        self.bensatankki=bensatankki



eka = Sähköauto('ABC-15', 180, 52.5)
toka = Polttomoottoriauto('ACD-123', 165, 32.3)

eka.kiihdytä(50)
toka.kiihdytä(60)
eka.kulje(3)
toka.kulje(3)
print(eka.matka, toka.matka)