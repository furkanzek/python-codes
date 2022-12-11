import numpy as np
import pandas as pd

np1 = np.random.randint(10, 100, 5)
np2 = np.random.randint(300, 500, 5)

series1 = pd.Series(np1)
series2 = pd.Series(np2)

data = dict(data1=series1, data2=series2)

df = pd.DataFrame(data)

#***********************************************************

data = [["Furkan", 2], ["Emirhan", 6], ["Aziz", 79], ["Eda", 76]]
df = pd.DataFrame(data, columns=["İsim", "DoğumYılı"], index=[1, 2, 3, 4])
print(df)

#***********************************************************

df = pd.read_csv('world_population.csv')


print(df)