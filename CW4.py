#------------------------CW1------------------------------


lista_imion=["michal","nela","ola","przemek"]

imiona_duze=[x.capitalize() for x in lista_imion]

#print(imiona_duze)

imiona_bez_i=[x for x in lista_imion if "i" in x]

#print(imiona_bez_i)

im_zenskie=("Aleksandra", "Zuzanna", "Marta" , "Natalia")

a=0

for x in im_zenskie:
    a+=len(x)

#print(a)


#------------------------CW2------------------------------
def fun1(*args):
    x=1
    for num in args:
        x*= num
    print(x)

#fun1(3,2,5)

def fun2(*argv):
    suma=0
    n=int(input("podaj n"))
    for num in argv:
        suma += num**n
    print(suma)

#fun2(3,2,4)

def mean(*args):
    suma = 0
    srednia = 0
    for x in args:
     suma += x
    srednia = suma / len(args)

    print(srednia)

mean(3,2,7)






