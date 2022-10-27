# Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
# Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa.
# Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
#
# Jokaisen auton nopeutta muutetaan siten,
# että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä. Tämä tehdään kutsumalla kiihdytä-metodia.
# Kaikkia autoja käsketään liikkumaan yhden tunnin ajan.
# Tämä tehdään kutsumalla kulje-metodia.
# Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.

import random


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

    # def __repr__(self):
        # return f"Auton rekisteritunnus on {self.rekkari}, huippunopeus on  {self.huippunopeus}."


autot = []

for i in range(10):
    autot.append(Auto("ABC-" + str(i+1), random.randint(100, 200)))


done = False
while not done:
    for i in autot:
        i.kiihdyta(random.randint(-10, 15))
        i.kulje(1)
        if i.kuljettumatka >= 10000:
            done = True


for auto in autot:
    print(f"Auton {auto.rekkari} huippunopeus: {auto.huippunopeus} km/h, nykyinen nopeus {auto.hetknopeus} km/h, "
          f"kuljettu matka: {auto.kuljettumatka} km.")
