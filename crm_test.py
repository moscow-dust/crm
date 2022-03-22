import pandas as pd
df = pd.read_csv('data.csv')
#print(df.head())
df['Затраты времени на посещение']=df['Затраты времени на посещение'].apply(lambda x: float(x.replace(',', '.')[:-1:1]))
df['KPI'] = df['Важность']/df['Затраты времени на посещение']*100
df = df.sort_values('KPI', ascending = False)
df = df[df['Затраты времени на посещение'].cumsum().lt(32)]
print(df['Название достопримечательности'])
