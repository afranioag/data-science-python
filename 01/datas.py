import pandas as pd

dias = ['10/02/2019', '11/02/2019','12/02/2019','13/02/2019','14/02/2019','15/02/2019']
temp_max = [31,35,34,28,27,27]

dias_temp = pd.Series(temp_max, index=dias)
print(dias_temp)

dias_temp.index = pd.to_datetime(dias_temp.index)
print(dias_temp)