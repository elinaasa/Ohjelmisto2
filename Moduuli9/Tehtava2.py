# Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi,
# joka saa parametrinaan nopeuden muutoksen (km/h). Jos nopeuden muutos on negatiivinen, auto hidastaa.
# Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
# Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
# Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h,
# sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus.
# Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
# Kuljettua matkaa ei tarvitse vielä päivittää.

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


auto1 = Auto("ABC-123", 142)

print(f"Auton rekisteritunnus on {auto1.rekkari}, huippunopeus on  {auto1.huippunopeus}, tämän hetkinen nopeus on "
      f"{auto1.hetknopeus} ja kuljettu matka on {auto1.kuljettumatka}.")

auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)

print(f"Auton hetkellinen nopeus on {auto1.hetknopeus} km/h")

auto1.kiihdyta(-200)

print(f"Auton hetkellinen nopeus on {auto1.hetknopeus} km/h")
