import pandas as pd
import numpy as np



sample = pd.read_csv('2007_ORD_formated_2.csv', encoding = "ISO-8859-1")

# Aggregate on Date
LateArr = sample[sample['ArrDelay'] > 0]
grouped_1 = LateArr.groupby('Date')
late_agg_day = grouped_1['ArrDelay'].agg(['count',np.mean])

grouped_2 = sample.groupby('Date')
delay_agg_day = grouped_2[['CRSElapsedTime','ArrDelay',
'DepDelay']].agg(['count',np.mean,np.std])

delay_agg_day = delay_agg_day.merge(late_agg_day, left_index = True, right_index = True, how = 'inner')

delay_agg_day.to_csv('2007_mean_CRSElapsedTime_delay.csv')

print (delay_agg_day.head())