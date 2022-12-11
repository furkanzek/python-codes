import numpy as np
import pandas as pd

data = np.random.randint(10, 100, 75).reshape(15, 5)
df = pd.DataFrame(data, columns=["Column1", "Column2", "Column3", "Column4", "Column5"])

result = df
result = df.columns
result = df.head(9)
result = df.tail(6)
result = df["Column1"].head(5)
result = df[["Column2", "Column3"]].head(5)
result = df[5:15][["Column2", "Column3"]].head(5)

result = df < 50
result = df[df < 50]
result = df[df % 2 == 0]
result = df[df["Column1"] < 50][["Column1", "Column2"]]
result = df[(df["Column1"] < 50) & (df["Column3"] > 30)]
result = df[(df["Column1"] < 50) | (df["Column3"] > 30)]

print(result)