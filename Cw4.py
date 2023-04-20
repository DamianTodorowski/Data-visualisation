#-----------------------------------cw1---------------------------
names = ["michal","nela","ola","przemek"]
names2 = [wartosc.capitalize() for wartosc in names]
print(names2)

names2 = [wartosc for wartosc in names if wartosc.count("l")]

names2 = [wartosc.capitalize() for wartosc in names if wartosc.endswith("a")]
names2 = [x for x in names if 'l' in x]
print(names2)

a = 0
for imie in names:
    a += len(imie)
print(a)

#-----------------------------------cw2---------------------------
def funkcja(*num):
    iloczyn = 1
    for liczba in num:
        iloczyn *= liczba

    print("Iloczyn: ", iloczyn)

funkcja(4, 2, 3)

def funkcja(*num, n):
    suma = 0
    for liczba in num:
        suma += liczba**n

    print("Suma n poteg: ", suma)

funkcja(4, 2, 3, n=2)

def mean(*num):
    suma = sum(num)
    print("Srednia: ", suma/len(num))

mean(4, 2, 3)

def gmean(*num):
    iloczyn = 1
    for liczba in num:
        iloczyn *= liczba

    print("Srednia geometryczna: ", iloczyn**(1/len(num)))

gmean(4, 2, 3)

def len_string(*string):
    suma = sum([len(slowo) for slowo in string])
    print(suma)

len_string("raz", "dwa", "trzy")

def tel(**numbers):
    for key, value in numbers.items():
        print("{} ma numer {}".format(key, value))

tel(Marcin=2424242)

def zarobki(**zarobki):
    suma = sum(zarobki.values())
    print("Srednia zarobkow wynosi: ", suma/len(zarobki))

zarobki(Styczen=2400, Luty=2555, Marzec=6929, Kwiecien=2999)
