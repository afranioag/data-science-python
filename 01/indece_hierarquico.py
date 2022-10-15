import pandas as pd

moedas = ['Peso', 'Real', 'Euro', 'Euro', 'Libra']
paises = [['América','América','Europa','Europa','Europa'],
['AR','BR','FR','IT','UK']]

paises = pd.Series(moedas, index=paises)

print(paises)


lista_lista = [[1,2,3], ['A', 'B', 'C'], ['D','E','F']]
lista = [['UM', 'DOIS', 'TRES'],['ONE','TWO','THREE']]

listas = pd.Series(lista_lista, index=lista)
print(listas)