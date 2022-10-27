# Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
# Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
# Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena.
# Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
# Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.
class Hissi:
    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.kerros = alinkerros

    def kerros_ylos(self):
        self.kerros = self.kerros + 1
        if self.kerros >= self.ylinkerros:
            self.kerros = self.ylinkerros

    def kerros_alas(self):
        self.kerros = self.kerros - 1
        if self.kerros <= self.alinkerros:
            self.kerros = self.alinkerros

    def siirry_kerrokseen(self, kerros):
        while self.kerros != kerros:
            if self.kerros < kerros:
                self.kerros_ylos()
            else:
                self.kerros_alas()


class Talo:
    def __init__(self, alinkerros, ylinkerros, hissitlkm):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.hissitlkm = hissitlkm
        self.hissit = [Hissi(alinkerros, ylinkerros) for i in range(hissitlkm)]

    def aja_hissia(self, hissinumero, kohdekerros):
        self.hissit[hissinumero - 1].siirry_kerrokseen(kohdekerros)


talo1 = Talo(1, 5, 2)
talo1.aja_hissia(2, 4)
