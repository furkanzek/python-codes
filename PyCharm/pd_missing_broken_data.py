import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)
df = pd.DataFrame(data, index=['a', 'c', 'e', 'f', 'h'], columns=['Column1', 'Column2', 'Column3'])
result = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
result = df.drop('Column1', axis=1)
result = df.drop('b', axis=0)
result = df[df['Column1'].notnull()]
result = df[df['Column1'].isnull()]['Column2']
result = df.dropna(axis=1)
result = df.dropna(how='all')
result = df.dropna(how='any')
result = df.dropna(subset=['Column1', 'Column3'])
result = df.dropna(thresh=3)
result = df.fillna(value='no input')


print(result)