import pandas as pd
import numpy as np

personeller = {
    'Çalışan' : ['Ahmet Yılmaz', 'Can Ertürk', 'Hasan Korkmaz', 'Cenk Saymaz', 'Ali Turan', 'Rıza Ertürk', 'Mustafa Can'],
    'Departman' : ['İnsan Kaynakları', 'Bilgi İşlem', 'Muhasebe', 'Bilgi İşlem', 'İnsan Kaynakları', 'Muhasebe', 'Bilgi İşlem'],
    'Yaş' : [30, 25, 45, 50, 23, 34, 42],
    'Semt' : ['Kadıköy', 'Tuzla', 'Maltepe', 'Tuzla', 'Kadıköy', 'Tuzla', 'Maltepe'],
    'Maaş' : [5000, 3000, 4000, 3500, 2750, 6500, 4500]
}

df = pd.DataFrame(personeller)

result = df['Maaş'].sum()
result = df.groupby('Departman').groups
result = df.groupby(['Departman', 'Semt']).groups

#semtler = df.groupby('Semt')
#for name, group in semtler:
#    print(name)
#    print(group)

result = df.groupby('Departman').get_group('Bilgi İşlem')
result = df.groupby('Departman').sum()
result = df.groupby('Departman').mean()
result = df.groupby('Departman')['Maaş'].mean()
result = df.groupby('Departman')['Çalışan'].count()
result = df.groupby('Departman')['Maaş'].max()['Bilgi İşlem']
result = df.groupby('Departman')['Maaş'].agg([np.sum, np.mean, np.max]).loc['Muhasebe']

print(result)
