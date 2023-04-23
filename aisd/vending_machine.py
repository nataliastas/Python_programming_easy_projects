from random import randint

nominaly = [50000,20000,10000,5000,2000,1000,500,200,100,50,20,10,5,2,1]
liczbaNominalow = len(nominaly)
stanKasy = [0]*liczbaNominalow

def ustalKase(jak=0):
    global nominaly,stanKasy,liczbaNominalow
    if jak == 0:
        for i in range(liczbaNominalow):
            stanKasy[i] = randint(0,20)
    elif jak == 1:
        stanKasy[5] = 12

def obslugaKasy():
    global nominaly, stanKasy, liczbaNominalow
    doZaplaty = int(float(input('Podaj kwotę do zapłaty '))*100)
    nom, ile = 1, 0
    ileZaplacil = 0
    stanKasyPrzed = stanKasy.copy()
    while nom>0:
        nom, ile = input('Podaj nominał oraz jego ilość lub podaj nominał i ilość jako 0, gdy nie chcesz już podać żadnego nominału ').split()
        ile = int(ile)
        nom = int(100 * float(nom))
        if nom in nominaly or nom == 0:
            ileZaplacil += ile * nom
            if nom == 0 and (ileZaplacil < doZaplaty):
                print('Kwota zapłacona jest za niska')
                continue
            if nom == 0:
                break0
            if (ileZaplacil > doZaplaty):
                break
            idx = nominaly.index(nom)
            stanKasy[idx] += ile
        else:
            print('Podany nominał nie istnieje')
            continue
    reszta = ileZaplacil - doZaplaty
    reszta = int(reszta)
    print(reszta/100)
    wydajReszte(reszta,stanKasyPrzed,ile)

def wydajReszte(reszta,stanKasyPrzed,ile):
    global nominaly, stanKasy, liczbaNominalow
    print('Reszta:')
    for i in range(len(stanKasy)):
        if stanKasy[i]>0:
            if nominaly[i]>reszta:
                continue
            else:
                if (nominaly[i] * stanKasy[i]) >= reszta:
                    ile = reszta // nominaly[i]
                elif (reszta - (nominaly[i] * stanKasy[i])) >= 0:
                    ile = stanKasy[i]
                else:
                    reszta2 = reszta - (nominaly[i] * stanKasy[i])
                    ile = reszta2 // nominaly[i]
                reszta -= ile * nominaly[i]
                stanKasy[i] -= ile
                if stanKasy[i] < 0:
                    print('Nie można wydać reszty')
                    stanKasy = stanKasyPrzed
                    continue
                if reszta>0 and stanKasy[i] == 0 and i == len(stanKasy)-1:
                    print('Nie można wydać reszty')
                    stanKasy = stanKasyPrzed
                print('%i*%f' % (ile, nominaly[i] / 100))
            if reszta == 0:
                break
        elif stanKasy[len(stanKasy)-1] == 0 and i == len(stanKasy)-1:
            print('Nie można wydać reszty')
            stanKasy = stanKasyPrzed
        else: continue
    print(nominaly)
    print(stanKasy)


ustalKase()
print(nominaly)
print(stanKasy)
while True:
    obslugaKasy()