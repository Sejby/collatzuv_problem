import matplotlib.pyplot as plt

class Graf:
    def __init__(self, pocatecni_cislo: int) -> None:
        self._pocatecni_cislo = pocatecni_cislo
        self._vysledne_pole = [pocatecni_cislo]
    
    @property
    def pocatecni_cislo(self):
        return self._pocatecni_cislo
    
    @pocatecni_cislo.setter
    def pocatecni_cislo(self, value):
        self._pocatecni_cislo = value
    
    @property
    def vysledne_pole(self):
        return self._vysledne_pole
    
    @vysledne_pole.setter
    def vysledne_pole(self, value):
        self._vysledne_pole.append(value)
    
    # metody
    def sudostlichost(self):
        if self._pocatecni_cislo % 2 == 1:
            self._pocatecni_cislo = 3*(self._pocatecni_cislo)+1
            self._vysledne_pole = self._vysledne_pole + [self._pocatecni_cislo]
        elif self._pocatecni_cislo % 2 == 0:
            self._pocatecni_cislo = self._pocatecni_cislo/2
            self._vysledne_pole = self._vysledne_pole + [self._pocatecni_cislo]
    
    def vypocti(self):
        while not self._vysledne_pole[-1] == 1:
            self.sudostlichost()

    def vykresliGraf(self):
        self.vypocti()
        plt.plot(range(0, len(self._vysledne_pole)), self._vysledne_pole)
        plt.xlabel("Počet operací")
        plt.ylabel("Hodnota")
        plt.title("Collatzova posloupnost")
        plt.show()