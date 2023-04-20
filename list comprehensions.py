squares = [x * x for x in range(10)]

 #jak pętla for

squares = [1,2,3,4,5,6,7,8,9,10]
#for x in range(10):
    #squares.append(x* x)
sq2 = []
sq2 = [x * x for x in squares]

print(sq2)

my_list = [1, 2, 3, 4]
double = []
double = [value * 2 for value in my_list]
#nadpisałem podwojone wartosci w liscie o nazwie double

print(double)

users = [{'name': 'Damian', 'age': 20}, {'name': 'Marcin', 'age': 21}, {'name': 'Szymyn', 'age': 20}]
user_name = [user['name'] for user in users]
print(user_name)

names = ['adam', 'damian', 'marcin']
upper = [value.capitalize() for value in names]
print(upper)

names2 = ['szymyn', 'aleks', 'krzysziu', 'lena']
namesL = [value for value in names2 if value.count('l')]
print(namesL)

namesA = [value for value in names2 if value.endswith("a")]
print(namesA)

a = 0
for value in names:
    a += len(value)
print(a)

#############################2

def mnozenie(*num):
    iloczyn = 1
    for value in num:
        iloczyn *= value
    print('iloczyn =', iloczyn)

mnozenie(4, 2, 3)

def nr_tel(**numbers):
    for key, value in numbers.items():
        print("{} ma numer: {}".format(key, value))

nr_tel(Damian=888212013)