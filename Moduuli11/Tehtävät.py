class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        print(f"Kirjan nimi on {self.nimi} ja kirjoittaja on {self.kirjoittaja} ja siinä on {self.sivumäärä} sivua.")

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        print(f"Lehden nimi on {self.nimi} ja päätoimittaja on {self.päätoimittaja}.")


aku_ankka = Lehti("aku", "aki hyyppä")
hytti6 = Kirja("hytti6", "Rosa Liksom", 200)

aku_ankka.tulosta_tiedot()
hytti6.tulosta_tiedot()