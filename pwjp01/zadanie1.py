from fractions import Fraction

def szukanie_dzielnikow(a):
    dzielniki = [1, -1]
    for i in range(2, abs(a) // 2 + 1):
        if (a % i == 0):
            dzielniki.append(i)
            dzielniki.append(i * (-1))
    if (a > 1):
        dzielniki.append(a)
        dzielniki.append(a * (-1))
    return dzielniki


def dzielniki_wspolczynnikow(wspolczynniki):
    while wspolczynniki[0] == 0:
        wspolczynniki.pop(0)
    if len(wspolczynniki) <= 1:
        print('To nie jest wielomian')
    a0 = wspolczynniki[-1]
    an = wspolczynniki[0]
    dzielniki_a0 = szukanie_dzielnikow(a0)
    dzielniki_an = szukanie_dzielnikow(an)
    return dzielniki_an, dzielniki_a0


def potencjalne_pierwiastki(dzielniki_an, dzielniki_a0):
    pierwiastki = []
    for i in range(len(dzielniki_a0)):
        for j in range(len(dzielniki_an)):
            pierwiastek = Fraction(dzielniki_a0[i], dzielniki_an[j])
            pierwiastki.append(pierwiastek)
    pierwiastki_new = []
    [pierwiastki_new.append(x) for x in pierwiastki if x not in pierwiastki_new]
    return pierwiastki_new

def liczenie_wielomianu(pierwiastek, wspolczynniki):
    wynik_list = []
    length = len(wspolczynniki)
    for j in range(len(wspolczynniki)):
        wynik = wspolczynniki[j] * (pierwiastek ** (length - 1))
        length = length - 1
        wynik_list.append(wynik)
    return wynik_list

def sprawdzenie_pierwiastkow(pierwiastki, wspolczynniki):
    pierwiastki_potwierdzone = []
    score = {}
    for i in range(len(pierwiastki)):
        krotnosc = 0
        wspolczynniki2 = wspolczynniki
        wynik_list = liczenie_wielomianu(pierwiastki[i], wspolczynniki2)
        while sum(wynik_list) == 0:
            pierwiastki_potwierdzone.append(pierwiastki[i])
            wspolczynniki2 = pochodna(wspolczynniki2)
            wynik_list = liczenie_wielomianu(pierwiastki[i], wspolczynniki2)
            krotnosc = krotnosc + 1
        if krotnosc != 0:
            score[pierwiastki[i]] = krotnosc
    return pierwiastki_potwierdzone,score

def pochodna(wspolczynniki):
    length = len(wspolczynniki)
    wspolczynniki_der = []
    for i in range(len(wspolczynniki)):
        length2 = length - (i+1)
        if length2 > 0:
            wsp = length2*wspolczynniki[i]
            wspolczynniki_der.append(wsp)
    return wspolczynniki_der


def wielomian(wspolczynniki):
    txt = ""
    if len(wspolczynniki) > 0:
        potega = len(wspolczynniki) - 1
        txt += str(wspolczynniki[0]) + "x^" + str(potega)
        for wsp in wspolczynniki[1:]:
            potega = potega - 1
            if wsp > 0:
                txt += "+"
            txt += str(wsp)
            if potega != 0:
                txt += "x^" + str(potega)
    return txt

def znajdz_dzielniki(liczba):
    dzielniki = [1, -1]
    for i in range(2, abs(liczba) // 2 + 1):
        if (liczba % i == 0):
            dzielniki.append(i)
            dzielniki.append(i * (-1))
    if (liczba > 1):
        dzielniki.append(liczba)
        dzielniki.append(liczba * (-1))
    return dzielniki

def wyswietl_wynik(score,wielomian):
    length = len(score)
    keys = list(score.keys())
    wynik = []
    krotnosc = []
    for i in range(length):
        wynik.append(float(keys[i]))
        krotnosc.append(score[keys[i]])
    print('Rozwiązaniami wielomianu '+str(wielomian)+' są następujące pierwiastki: '+str(wynik))
    print('Krotności tych pierwiastków są przedstawione kolejno w liście: '+str(krotnosc))

if __name__ == '__main__':
    wspolczynniki = [1,2,-7,-8,12]
    dzielniki_an, dzielniki_a0 = dzielniki_wspolczynnikow(wspolczynniki)
    pierwiastki = potencjalne_pierwiastki(dzielniki_an,dzielniki_a0)
    pierwiastki_potwierdzone,score = sprawdzenie_pierwiastkow(pierwiastki,wspolczynniki)
    wielomian = wielomian(wspolczynniki)
    wyswietl_wynik(score,wielomian)

