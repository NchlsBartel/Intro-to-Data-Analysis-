import pandas as pd
import numpy as np
import datetime as DT
df= pd.read_csv('https://raw.githubusercontent.com/cwkteacher/Data/master/athletes.csv')

#rugby = df.where(df['sport'] == 'rugby')




sport = df['sport'].value_counts()[:10].index.tolist()

print(sport)