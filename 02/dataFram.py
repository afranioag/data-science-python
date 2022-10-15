import pandas as pd

dados = {'nome': ['Argentina','Brasil','França','Itália','Reino Unido'],
'continente': ['América','América','Europa','Europa','Europa'],
'extensao': [2780,8511,644,301,244],
'corVerde': [0,1,0,1,0]}

siglas = ['AR','BR','FR','IT','UK']

paises = pd.DataFrame(dados,index=siglas)

print(paises)
