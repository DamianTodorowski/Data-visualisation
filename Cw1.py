import math
a = int(input("wprowadz n: "))
if a>0 and a<100:
    for i in range (1,a+1):
      for j in range(1,a+1):
          print(i*j)
else:
    print("n is too large")

a = int(input("wprowadz a: "))
b = int(input("wprowadz b: "))
q = math.gcd(a,b)
p=a//q
print(f'{p}/{q}')

n = int(input("wprowadz n: "))
e1 = (1+1/n)**n
print(e1)

def silnia(n):
    if(n==0):
        return 1
    return n+silnia(n-1)

e2 = sum([1/silnia(k) for k in range (n+1)])
print(e2)