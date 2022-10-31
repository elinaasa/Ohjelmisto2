# Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto. Sähköautolla on
# ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena on bensatankin koko litroina.
# Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen,
# huippunopeuden ja akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa
# oman kapasiteettinsa.

class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.hetknopeus = 0
        self.kuljettumatka = 0

    def kiihdyta(self, nopeudenmuutos):
        self.hetknopeus = self.hetknopeus + nopeudenmuutos
        if self.hetknopeus < 0:
            self.hetknopeus = 0
        elif self.huippunopeus < self.hetknopeus:
            self.hetknopeus = self.huippunopeus

    def kulje(self, tuntimaara):
        self.kuljettumatka = self.kuljettumatka + tuntimaara * self.hetknopeus


class Sahkoauto:
    def __init__(self, rekkari, huippunopeus, akkukapasiteetti):
        super().__init__(rekkari)
        super().__init__(huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto:
    def __init__(self, rekkari, huippunopeus, tankinkoko):
        super().__init__(rekkari)
        super().__init__(huippunopeus)
        self.tankinkoko = tankinkoko


# Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden
# polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan
# kolmen tunnin verran ja tulosta autojen matkamittarilukemat.

sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.kiihdyta(60)
polttomoottoriauto.kiihdyta(60)

sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)

print(sahkoauto.hetknopeus)
print(polttomoottoriauto.hetknopeus)