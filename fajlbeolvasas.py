#Név:Település:utca:Fizetés:Jutalom:Születés:Belépés
#beolvasas



fileReader = open("feherBt.txt", encoding="utf-8")

sorokSzama = 0
nyiregyhaziak = 0
gyoriekFizetes=0
gyoriek=0
#egy sor beolvasasa, azert hogy a fejlecet atlepjuk (el tudnank menteni egy valtozoba az erteket, de itt nem kell)
fileReader.readline()

for sor in fileReader:
    #itt barmit csinalhatok a sorokkal, egy sor a SOR valtozoban van.
    lista = sor.split(":")
    if  (lista[1] == "Nyíregyháza"):
        nyiregyhaziak=nyiregyhaziak+1
    if(lista[1] == "Győr"):
        gyoriekFizetes=int(lista[3])+ gyoriekFizetes
        gyoriek=gyoriek+1
    sorokSzama=sorokSzama+1
Atlag=gyoriekFizetes/gyoriek    
print("Dolgozók száma: " +str(sorokSzama) )
print("Nyiregyhaziak száma: " +str(nyiregyhaziak) )
gyoriek = open("gyoriek.txt", mode="w", encoding="utf-8")
gyoriek.writelines("Győriek átlaga: " +str(Atlag) )


