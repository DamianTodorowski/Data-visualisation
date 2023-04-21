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




class Frac:
    def __init__(self, licznik, mianownik=1):
        if mianownik == 0:
            raise ValueError("Mianownik nie może być równy zero.")
        if mianownik < 0:
            licznik, mianownik = -licznik, -mianownik
        nwd = self._nwd(licznik, mianownik)
        self.licznik = licznik // nwd
        self.mianownik = mianownik // nwd

    def __str__(self):
        if self.mianownik == 1:
            return str(self.licznik)
        else:
            return f"{self.licznik}/{self.mianownik}"

    def dodawanie(self, other):
        licznik = self.licznik * other.mianownik + self.mianownik * other.licznik
        mianownik = self.mianownik * other.mianownik
        return Frac(licznik, mianownik)

    def odejmowanie(self, other):
        licznik = self.licznik * other.mianownik - self.mianownik * other.licznik
        mianownik = self.mianownik * other.mianownik
        return Frac(licznik, mianownik)

    def mnozenie(self, other):
        licznik = self.licznik * other.licznik
        mianownik = self.mianownik * other.mianownik
        return Frac(licznik, mianownik)

    def dzielenie(self, other):
        if other.licznik == 0:
            raise ZeroDivisionError("Nie można dzielić przez zero.")
        licznik = self.licznik * other.mianownik
        mianownik = self.mianownik * other.licznik
        return Frac(licznik, mianownik)

    def rowne(self, other):
        return self.licznik == other.licznik and self.mianownik == other.mianownik

    def mniejsze(self, other):
        return self.licznik * other.mianownik < self.mianownik * other.licznik

    def mniejsze_rowne(self, other):
        return self.licznik * other.mianownik <= self.mianownik * other.licznik

    def wieksze_rowne(self, other):
        return self.licznik * other.mianownik > self.mianownik * other.licznik

    def _nwd(self, a, b):
        while b:
            a, b = b, a % b
        return a

f1 = Frac(1, 2)
f2 = Frac(3, 4)

f3 = f1.dodawanie(f2)
print(f"({f1}) + ({f2}) = {f3}")

f4 = f1.odejmowanie(f2)
print(f"({f1}) - ({f2}) = {f4}")

f5 = f1.mnozenie(f2)
print(f"({f1}) * ({f2}) = {f5}")


f6 = f1.dzielenie(f2)
print(f"({f1}) / ({f2}) = {f6}")

print(f"({f1}) == ({f2}): {f1.rowne(f2)}")
print(f"({f1}) < ({f2}): {f1.mniejsze(f2)}")
print(f"({f1}) <= ({f2}): {f1.mniejsze_rowne(f2)}")
print(f"({f1}) > ({f2}): {f1.wieksze_rowne(f2)}")
