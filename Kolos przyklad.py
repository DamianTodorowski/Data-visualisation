
 

#zad 1
def zad1(lista):
    lista2=[]
    for val in lista:
        if val not in lista2:
            lista2.append(val)
    return lista2
    
    
    
#zad 2
bibl1="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPRQRSTUVWXYZ"
a="abc efghijklm ouprs"
wynik = ''.join([x for x in a if x in bibl1])
wynik2=wynik[3::4]
for val in wynik2[::-1]:
    print(val)
    
  
  


#zad3
def f(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return f(n-1)+f(n-2)

def f2(n):
    a ,b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
    
    
#zad4
    
def zad4(*num,n):
    iloczyn=1
    for liczba in num:
        iloczyn=iloczyn*liczba**n
    return iloczyn
print(zad4(1,2,3,4,5,n=2))

#zad5
a=['apple', 'banana', 'pomergranate', 'plum', 'orange', 'melon', 'cherry', 'watermelon']
lista=[len(x) for x in a if "u" in x or "o" in x]
print(lista)


#zad6
def silnia(n):
    if n==0 or n==1:
        return 1
    else:
        return n*silnia(n-1)

def Newton(n,k):
    if k>n:
        return 0
    return silnia(n)/(silnia(k)*silnia(n-k))
print(silnia(5))

print(Newton(5,5))


#zad 7
class Polynomial:
    def __init__(self, coef):
        self.coef = coef

    def __str__(self):
        s = ""
        for i in range(len(self.coef)-1, 0, -1):
            s += str(self.coef[i])+("x^")+str(i)
            if self.coef[i-1]>=0:
                s+='+'
        s += str(self.coef[0])
        return (s)

    def __add__(self, other):
        s = []
        if len(self.coef) > len(other.coef):
           for i in range(0, len(other.coef)):
               s.append(self.coef[i]+other.coef[i])
           for i in range(len(other.coef), len(self.coef)):
               s.append(self.coef[i])
        else:
            for i in range(0, len(self.coef)):
                s.append(self.coef[i] + other.coef[i])
            for i in range(len(self.coef), len(other.coef)):
                s.append(other.coef[i])
        return Polynomial(s)

    def __sub__(self, other):
        s = []
        if len(self.coef) > len(other.coef):
           for i in range(0, len(other.coef)):
               s.append(self.coef[i]-other.coef[i])
           for i in range(len(other.coef), len(self.coef)):
               s.append(self.coef[i])
        else:
            for i in range(0, len(self.coef)):
                s.append(self.coef[i] - other.coef[i])
            for i in range(len(self.coef), len(other.coef)):
                s.append(- other.coef[i])
        return Polynomial(s)



a = Polynomial([2, 3, 4])
b = Polynomial([1, 4, 2, 2])
print(f'{a}+{b}={a+b}')
print(f'{a}-({b})={a-b}')
