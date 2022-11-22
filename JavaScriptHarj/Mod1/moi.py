# Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus,
# huippunopeus, tämänhetkinen nopeus ja kuljettu matka. Kirjoita luokkaan alustaja,
# joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
# Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
# Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
# Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus


auto1 = Auto('ABC-123', 142)

print(auto1.rekkari, auto1.huippunopeus)
