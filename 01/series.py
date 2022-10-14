# -*- coding: UTF-8 -*-

import pandas as pd

# Criando listas para depois criar as series a partir dessas.
# Poderia criar uma serie com listas diretamente dentro do construtor.
notas = [9.2, 8.5, 8.7, 9.8, 10.0]

alunos = ['jorge', 'marta', 'gaby', 'laiz', 'henrique']
mat = ['M01', 'M02', 'M03', 'M04', 'M05']

# Ao criar dessa forma, os indices serão numeros inteiros crescentes.
print('Criando series a partir de uma lista sem indices custom: ')
notas_s = pd.Series(notas)
print(notas_s)

# Dessa forma estou passando os novos indices com o atributo index 
print('\nCriando series com listas passando indices custom: ')
alunos_mat = pd.Series(alunos, index=mat)
print(alunos_mat)


# Dessa forma estou criando series a partir de um dicionario
capitais = {'RN':'Natal','PB':'João Pessoa', 'CE':'Fortaleza', 'BA':'Salvador'}
print('\nCriando series a partir de um dicionario, nesse caso os indices serão as chaves: ')
capitais_s = pd.Series(capitais)
print(capitais_s)




