import datetime as dt
class Adatok:
    def __init__(self, sor):
        split = sor.split(';')
        self.Nev=split[0]
        self.Elso=dt.datetime.strptime(split[1], "%Y-%m-%d")
        self.Utolso=dt.datetime.strptime(split[2], "%Y-%m-%d")
        self.Suly=int(split[3])
        self.Magassag=int(split[4])

with open("balkezesek.csv","r") as Beolvas:
    fejlec = Beolvas.readline().strip()
    lista = [Adatok(x.strip()) for x in Beolvas]

print(f"3. feladat: {len(lista)}")
print("4. feladat:")
[print(f"\t{x.Nev}, {float(x.Magassag*2.54):.1f} cm") for x in lista if x.Utolso.year==1999 and x.Utolso.month==10]
print("5. feladat:")
evszam = int(input("Kérek egy 1990 és 1999 közötti évszámot: "))
while evszam <1990 or evszam>1999:
    evszam = int(input("Hibás adat!Kérek egy 1990 és 1999 közötti évszámot: "))
suly=[x.Suly for x in lista if evszam >=x.Elso.year and evszam <=x.Utolso.year]
print(f"6. feladat: {sum(suly)/len(suly):.2f} font")


