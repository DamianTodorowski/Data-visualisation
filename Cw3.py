lista=[1,2,3]
print(lista)
lista.append(4)
print(lista)
lista.insert(3,5)
print(lista)
lista.remove(5)
print(lista)
lista.pop(3)
print(lista)
lista.append(2)
lista.sort()
print(lista)
lista.reverse()
lista.copy()
lista.clear()
print(lista)

#cw1
for i in range (0,15):
    lista.append((i))
print(lista)

numbers1=[*range(0,15)]

#b)
lista1=[num**5 for num in range(15)]

lista2=[math.factorial(num) for num in range(20)]

lista3=[math.e ** num for num in range(20)]

lista_nazwisk = ["Buta","Kowalski","Todorowski","Gorczynski","Nowak"]
lista4=[len(val) for val in lista4]

lista1=[1,2,3,4,5,6,7,8,9,10]
lista2=[10,20,30,40,50,60,70,80,90,100]
wynik=[]
for i in range (0,len(lista1)):
    wynik.append(lista1[i]+lista2[i])
print(wynik)

print([x+y for x,y in zip(lista1,lista2)])

def miesiac(a):
    lista=["Styczen","Luty","Marzec",'Kwiecien',"Maj","Czerwiec","Lipiec","Sierpien","Wrzesien","Pazdziernik","Listopad","Grudzien"]
    return lista.index(a)+1
a="Kwiecien"
print(miesiac(a))

lista_nazwisk = ["Buta","Kowalski","Todorowski","Gorczynski","Nowak"]
wynik=[]
def abc(lista_nazwisk,litera):
    for nazwisko in lista_nazwisk:
        if nazwisko[0]>litera:
            wynik.append(nazwisko)
    return wynik

print(abc(lista_nazwisk,'B'))

lista_nazwisk = ["Buta","Kowalski","Todorowski","Gorczynski","Nowak"]
def funkcja3(lista_nazwisk,int):
    return [val for val in lista_nazwisk if len(val)>int]

print(funkcja3(lista_nazwisk,6))

def funkcja4(a):
    if a[::-1]==a:
        return 1
    else:
        return 0
    
  def is_sorted(list):
    return list==sorted(list,reverse=True)

def funkcja5(lista):
    for i in range(0,len(lista)):
        if(lista[i]>lista[i+1]):
            return True
        else:
            return False

def funkcja6(lista):
    return [val**3 for val in lista]
lista=[1,2,3]
print(funkcja5(lista))

def funkcja7(lista,n1,n2):
    for i in range(0,len(lista)):
        if lista[i]==n1:
             lista[i]=n2
    return lista

def func(list,n1,n2):
    return[x if x!=n1 else n2 for x in list]

lista=[1.22,4.33,4.33,6.55]
print(funkcja7(lista,4.33,5.00))

import math
def funkcja7(lista,n1,n2):
    for i in range(0,len(lista)):
        if math.isclose(lista[i],n1):
             lista[i]=n2
    return lista

#Cw2
panstwa = {"Polska","Niemcy","Finlandia","Belgia","Czechy"}

panstwa.add("Słowacja")

'Polska' in panstwa

panstwa.remove("Niemcy")

panstwa|panstwa2

panstwa & panstwa2

panstwa2 - panstwa

panstwa3.issubset(panstwa)
####################################################Cw3
#a)
T=(1,2,3,"sdsds",(5,6,7),"s","&")

T[3:5]

T[len(T)-3]

#b)  
def funkcja1(krotka,element):
    lista=list(krotka)
    lista.append(element)
    krotka=tuple(lista)
    return krotka

def funkcja2(krotka,element):
    y=(element,)
    krotka +=y
    return krotka

def funkcja3(krotka,element):
    lista = list(krotka)
    lista.remove(element)
    krotka = tuple(lista)
    return krotka


print(funkcja1((1,2,3),"abc"))
print(funkcja2((1,2,3),"abc"))
print(funkcja3((1,2,3),3))


#a)
def abc(lista):
    lista2= []
    for val in lista:
        if lista2.count(val)==0:
            lista2.append(val)
    return lista2

def abc2(lista):
    for val in set(lista):
        print(val)

lista=['raz','dwa','dwa','trzy']
print(abc(lista))
print (abc2(lista))
#Cw4
tel={'Marcin':423424,'Damian':242524,'Tomek':252506,'Gosia':226672,'Pawel':267222}
def print_phone_numbers(slownik):
    for imie,numer in slownik.items():
        print(imie,"ma numer",numer)

print(print_phone_numbers(tel))

del tel['Damian']
tel['Damian']=252525
tel['Marcin']=662626

#b)
dni=["Poniedzialek",'Wtorek','Sroda','Czwartek','Piatek','Sobota','Niedziela']
def ang(lista):
    for i in range (0,len(lista)):
        if lista[i]=="Poniedzialek":
            lista[i]="Monday"
        if lista[i]=="Wtorek":
            lista[i]="Tuesday"
            lista[i] = "Tuesday"
        if lista[i]=="Sroda":
            lista[i] = "Wednesday"
        if lista[i]=="Czwartek":
            lista[i] = "Thursday"
        if lista[i]=="Piatek":
            lista[i] = "Friday"
        if lista[i]=="Sobota":
            lista[i] = "Saturday"
        if lista[i]=="Niedziela":
            lista[i] = "Sunday"
    return lista

print(ang(dni))


return e['numer']
lista = [{'miesiac': 'styczen','numer': 1},{'miesiac': 'luty','numer': 2},
         {'miesiac': 'marzec', 'numer': 3}, {'miesiac': 'kwiecien', 'numer': 4},
         {'miesiac': 'maj', 'numer': 5}, {'miesiac': 'czerwiec', 'numer': 6},
         {'miesiac': 'lipiec', 'numer': 7}, {'miesiac': 'sierpien', 'numer': 8},
        {'miesiac': 'wrzesien','numer': 9},{'miesiac': 'pazdziernik','numer': 10},

        {'miesiac': 'listopad','numer': 11},{'miesiac': 'grudzien','numer': 12},
         ]

lista.sort(key=myFunc)

miesiace = ['luty','styczen','grudzien','listopad','marzec','kwiecien','pazdziernik','wrzesien','maj'
            ,'czerwiec','sierpien','lipiec']
numery = [12,5,2,11,3,8,7,9,1,6,4,10]
numery.sort()
final = []

print(miesiace)

#Cw3
def is_palindrome(word):
    return word == word[::-1]
print(is_palindrome('kajak'))
print(is_palindrome('aga'))
print(is_palindrome('Kubarozruba'))



