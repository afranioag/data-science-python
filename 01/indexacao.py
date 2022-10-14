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
print("-----------------------------\n")

sr2 = pd.Series({"BA":"Salvador", "RN":"NATAL","AM":"Amapa"})
print(sr2)
print(sr2['RN'])
print(sr2[['RN','AM']])

print("-----------------------------\n")

