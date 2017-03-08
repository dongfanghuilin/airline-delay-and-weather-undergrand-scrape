import pandas as pd

air = pd.read_csv('2008.csv')
sample_1 = air.sample(frac = 0.1)
sample_2 = air.sample(frac = 0.1)
sample_3 = air.sample(frac = 0.01)

sample_1.to_csv('air_08_sample01_1.csv')
sample_2.to_csv('air_08_sample01_2.csv')
sample_3.to_csv('air_08_sample001_2.csv')

air_2001 = pd.read_csv('air_08_sample001_2.csv')
print (air_2001.describe())
