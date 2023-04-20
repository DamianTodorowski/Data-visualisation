class Person:
    def __init__(self,age, weight, height, name, ballance):
        self.age = age
        self.weight = weight
        self.height = height
        self.name = name
        self.ballance = ballance

    def wplata(self, kwota):
        self.ballance = self.ballance+kwota

    def wyplata (self, hajsik):
        if self.ballance >= hajsik:
            self.ballance = self.ballance-hajsik
        else:
            print('nie masz vdolcow')

    def przelew(self, user, kwota):
       if self.ballance >= kwota:
           user.ballance += kwota
           self.ballance -= kwota



user = Person(20, 80, 182, 'Damian', 200)
user1 =Person(21, 86, 195, 'Marcin', 2000)
print(user.ballance)

user.wplata(300)
user.wyplata(100)

user1.przelew(user, 200)
print(user.ballance)
print(user1.ballance)



class konto_firmowe(Person):
    def __init__(self, name, ballance):
        self.name = name
        self.ballance = ballance

Marcin = konto_firmowe('marbud', 2137)

print(Marcin.name)

Marcin.wplata(1000)

print(Marcin.ballance)