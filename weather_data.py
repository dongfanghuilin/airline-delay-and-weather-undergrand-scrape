import pandas as pd
import numpy as np


delay_07 = pd.read_csv('2007_mean_CRSElapsedTime_delay.csv', encoding = "ISO-8859-1")
delay_08 = pd.read_csv('2008_mean_CRSElapsedTime_delay.csv', encoding = "ISO-8859-1")

weather = pd.read_csv('weather_ORD_0708.csv', encoding = "ISO-8859-1")


cols = ['Date','ArrDelay_mean', 'LateArrMean', 'LatePercnt']
delay_07 = delay_07[cols]
delay_08 = delay_08[cols]

weather_07 = weather.merge(delay_07, left_on = 'Date', right_on = 'Date', how = 'inner')
weather_08 = weather.merge(delay_08, left_on = 'Date', right_on = 'Date', how = 'inner')

weather_07.to_csv('2007_weather_delay.csv')
weather_08.to_csv('2008_weather_delay.csv')