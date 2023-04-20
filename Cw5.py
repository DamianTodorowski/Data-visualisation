#----------------------------------zad1-----------------------------------
class Fruit:
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight
    def isfresh(self):
        if self.color == "brown":
            return False
        else:
            return True
    def str(self):
        return ("color:" + str(self.color) + " weight:" + str(self.weight))

class Apple(Fruit):
    def __init__(self, color="green", weight=0.1):
        self.color = color
        self.weight = weight
class Banana(Fruit):
    def __init__(self, color="yellow", weight=0.4):
        self.color = color
        self.weight = weight
class Orange(Fruit):
    def __init__(self, color="orange", weight=0.6):
        self.color = color
        self.weight = weight

obiekt1=Apple()
obiekt2=Banana()
print(obiekt1.str())

#----------------------------------zad2-----------------------------------

class Account:
    def __init__(self, saldo=0):
        self.saldo = saldo
        self.saldo_p = saldo

    def saldo_poczatkowe(self):
        print(f"Saldo poczatkowe wynosiło: {self.saldo_p} zl")
    def saldo_koncowe(self):
        print(f"Saldo koncowe wynosi: {self.saldo} zl")

    def wplata(self, kwota):
        self.saldo += kwota
        print(f"Wpłacono: {kwota} na konto\nśrodki wynoszą:{self.saldo}\n")

    def wyplata(self, kwota):
        if(self.saldo>=kwota):
            self.saldo -= kwota
            print(f"Wypłacono: {kwota} na konto\nśrodki wynoszą:{self.saldo}\n")

    def przelew(self,obiekt2,kwota):
        if(self.saldo >= kwota):
            obiekt2.saldo+=kwota
            self.saldo-=kwota
            print(f"Wykonano przelew na kwote:{kwota}")
        else:
            print(f"Nie wykonano przelewu")



Marcin=Account(3400.30)
Marcin.wplata(343)
Marcin.saldo_koncowe()
Damian=Account(5300)
Damian.saldo_koncowe()
Marcin.przelew(Damian,400)
Damian.saldo_koncowe()
Marcin.saldo_koncowe()


#------------------------------------------------------------------------------------------------
class Romanian:
    def __init__(self, val):
        if(isinstance(val,str)):
            self.rzymska=val
        else:
            self.liczba=val
    def convert_romanian(self):
        liczba=self.liczba
        liczby = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
                  (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        rzymska=''
        while(liczba>0):
            for l,r in liczby:
                while(liczba>=l):
                    rzymska=rzymska+r
                    liczba=liczba-l
        return rzymska

    def convert_arabic(self):
        roman_numeral=self.rzymska
        roman_to_decimal = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        arabic_numeral = 0
        previous_value = 0

        for numeral in roman_numeral[::-1]:
            current_value = roman_to_decimal[numeral]

            if current_value >= previous_value:
                    arabic_numeral += current_value
            else:
                    arabic_numeral -= current_value

            previous_value = current_value


print(Romanian("MCMXCV").convert_arabic())
