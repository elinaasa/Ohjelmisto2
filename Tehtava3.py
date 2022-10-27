# Laajenna ohjelmaa siten, että mukana on kulje-metodi,
# joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on
# tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
# Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.
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


auto1 = Auto("ABC-123", 142)

print(f"Auton rekisteritunnus on {auto1.rekkari}, huippunopeus on  {auto1.huippunopeus}, tämän hetkinen nopeus on {auto1.hetknopeus} ja kuljettu matka on {auto1.kuljettumatka}.")

auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)

print(f"Auton hetkellinen nopeus on {auto1.hetknopeus} km/h")

auto1.kiihdyta(-200)

print(f"Auton hetkellinen nopeus on {auto1.hetknopeus} km/h")

