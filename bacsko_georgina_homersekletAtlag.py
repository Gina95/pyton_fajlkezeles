#Bacskó Georgina 2021.11.10



print("Bacskó Georgina 2021.11.10")
print("Megvizsgálja három nap átlag hömérsékletét")
print("Fűteni kell 15 fok alatt!")
a=11.4
b=18.2
c=16.
Atlag= (a+b+c)/3

if Atlag > 15: 
    print("Az átlaghőmérséklet: " ,Atlag, " fok, nem kell fűteni.")  
if Atlag == 15:
    print("Az átlaghőmérséklet: " ,Atlag, " fok, nem kell fűteni.")
if Atlag < 15:
    print("Az átlaghömérséklet: " + Atlag + " fok, indítsa ek a fűtést.")



#SCript nyelv

#deklaralas #definialas
sarkany=11.4
sarkany=sarkany + 5
print(sarkany)
#ertekadas
sarkany="mostmar nem"
sarkany=sarkany + " meg tobb szoveggel"
print(sarkany)

sarkany = 88888
print(sarkany)


#TIPUS
print("szovegek")
print('c')
print(True)
print(True)
print(False)

#OPERATOR - barmi ami nem szoveg szam hanem valami fura karakter
# !=
# ==
# + / * -

print(44444 - True)
print(44444 - False)

# NUMBER - BOOL => TRUE = 1 , FALSE = 0

#vizsgalat
barkCounter = 55 
if True:
    print("vajon kiirija e")
if 4444 - 4:
    print("vajon kiirija e 2")
if 0:
    print("a-a sosem")
if 1 < 5:
    print("IGEN")
if 7 < 5:  
    print("NEM")
if 1 <= 1:  
    print("IGEN")
if 5 == 5:
    print("IGEN")
if 5 == 5 and 4 == 4:
    print("IGEN")
if  barkCounter == 40  and barkCounter > 10:
    print("UGATUNK")
if  barkCounter > 10 and barkCounter == 40 or barkCounter != 0:
    print("UGATUNK MEGIS")

#ELSE
if 7 < 5:  
    print("NEM")
else: 
    print("hola")
    



dobas = 1

if dobas > 3:
    dobas = 1
    if dobas == 1:
        print("nyertunk")
else:
    print("vege")

# fugvenyek / methodus / eljaras
# f(x)
# szam = input("adja szamot")
# print(szam)

# ciklus
print("1")
print("2")
print("3")
print("4")
print("5")


#range(n) -> 0 .. n-1-ig a szamokat adja vissza
#range -> [0, 1, 2, 3, 4]
# i barmi lehet, de ez egy valtozonev
for valtozo in range(100):
    print(valtozo)
#
#valtozo=0 -> kiirja
#valtozo=1 -> kiirja
#valtozo=2 -> kiirja
# ....

allatok = ["tigris", "kutya", "cica", "sarkany"] 

for aktulisAllat in allatok:
    print(aktulisAllat)


bekertszamok = []
for i in range(5):
    bekertInput = input("adj " + str(i + 1) + " szamot ")
    szam = int(bekertInput)
    bekertszamok.append(szam)

# bekertSzamok = [4,7,5,1,2]
Atlag= sum(bekertszamok)/ 5
print("Az átlag:" + str(Atlag) +"")

# i = 0 -> int
# i = 1 -> int