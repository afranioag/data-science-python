import pandas as pd
import numpy as np

sr = pd.Series([x for x in range(10)])
sr1 = pd.Series([x for x in range(-10,1)])

print(sr)
print(sr1)
print("\nRaiz")
print(np.sqrt(sr))
print("\nSoma")
print(sr + sr1)
print("\nSubtracao")
print(sr - sr1)
print("\nMulti")
print(sr * sr1)
print("\nDivi")
print(sr / sr1)