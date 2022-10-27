# Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys,
# joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.

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

    def palohalytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alinkerros)


talo1 = Talo(1, 5, 2)
talo1.aja_hissia(2, 4)
talo1.palohalytys()

