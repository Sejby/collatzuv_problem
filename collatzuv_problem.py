from trida import Graf

def main():
    pocatecni_cislo = int(input("Zadejte počáteční celé číslo:"))
    graf = Graf(pocatecni_cislo=pocatecni_cislo)    
    graf.vykresliGraf()

if __name__ == "__main__":
    main()