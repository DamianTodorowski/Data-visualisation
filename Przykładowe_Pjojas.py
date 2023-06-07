import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import pandas as pd
import openpyxl as xl

labels=['A','B','C','D','E','F']
sizes=[15.70,25.58,16.86,21.51,12.79,7.56]
sizes2=[20.37,17.59,9.72,19.91,15.74,16.67]
colors=['brown','pink','tan','greenyellow','brown','steelblue']
colors2=['brown','pink','tan','greenyellow','brown','steelblue']
my_explode=(0,0.1,0,0,0,0)
plt.subplot(2,3,1)

plt.pie(sizes,labels=labels,colors=colors,explode=my_explode,autopct='%1.2f%%',startangle=30)
plt.tight_layout()
plt.title('Lewo Góra')


plt.subplot(2,2,4)
plt.pie(sizes2,labels=labels,colors=colors2,explode=my_explode,autopct='%1.2f%%',startangle=30)

plt.title('Prawo Dół')

#plt.savefig('zad1.jpg',format='jpg')
plt.show()


# Wczytaj dane z pliku Excel do ramki danych
df = pd.read_excel('ceny21.xlsx')


markers = {'mąka pszenna - za 1kg': 'o', 'kasza jęczmienna - za 0,5kg': 's'}
colors = {'mąka pszenna - za 1kg': 'red', 'kasza jęczmienna - za 0,5kg': 'blue'}

# Iteracja po danych i tworzenie wykresu punktowego
for index, row in df.iterrows():
    plt.scatter(row['Rok'], row['Wartość'], marker=markers[row['Rodzaje towarów']], color=colors[row['Rodzaje towarów']])


# Ustawienia wykresu
plt.xlabel('Rok')
plt.ylabel('Wartość')
plt.title('Wykres2')
plt.text(1,-1, 'Damian')
plt.legend()

# Wyświetl wykres
plt.show()
print(df)
