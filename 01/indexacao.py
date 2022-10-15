import pandas as pd

sr1 = pd.Series([x**2 for x in range(10)])
print("-----------------------------\n")
print(sr1)
print(sr1[2])
print(sr1[[2,4,7,9]])
print(sr1[0:4])
print(sr1[2:7])
print(sr1[1:9:3])
print(sr1[-1:])
print("--")
print(sr1[sr1 > 20])
print(sr1[sr1 > 20].index)
print("-----------------------------\n")

sr2 = pd.Series({"BA":"Salvador", "RN":"NATAL","AM":"Amapa"})
print(sr2)
print(sr2['RN'])
print(sr2[['RN','AM']])

#testa se rótulos fazem parte de uma Series
print("BA in sr2")
print('BA' in sr2)

#testa se valor faz parte de uma Series
print('BA isin sr2')
print(sr2.isin(['Salvador']))
print("-----------------------------\n")

