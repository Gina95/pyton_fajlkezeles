#Bacskó Georgina 2021.11.10
print("Bacskó Georgina 2021.11.10")
print("Kiszámolja egy téglatest térfogatát")

def terfogatSzamol(a,b,c):
    v=a*b*c
    return v



bekertSzamok=[]
for i in range(3):
    szam=int(input("Adja meg" +str(i+1)+ ". számot" ))
    bekertSzamok.append(szam)
v=terfogatSzamol(bekertSzamok[0], bekertSzamok[1], bekertSzamok[2])
print("Téglatest térfogata:" + str(v))