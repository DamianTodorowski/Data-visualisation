import math
def a2(a,b):
    if (isinstance(a,float)) or isinstance(b,float):
        return (math.fmod(a, b))
    else:
        return(a%b)

def a4(a):
    print(math.exp(a))
    print(math.e**a)
    print(math.pow(math.e,a))

def a3(a,n):
    for i in range (2,n+2):
        print(math.log(a,i),end="|")

def b1(a):
    for i in range (0,len(a)):
        if i%2==0:
            print(a[i])
def b2(n):
    print(a[n:])

def b3(a):
    print(a[::-1])
def b4(a,b):
    if len(a)>len(b):
        print(a)
    else:
        print(b)
a = "abcd"
b="abc"
b4(a,b)
txt="My name is {imie}. My date of birth is {data}"
print(txt.format(imie="Marcin",data="7.02.2022"))

a4(3.14)