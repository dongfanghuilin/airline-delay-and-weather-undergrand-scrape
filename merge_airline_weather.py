import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.style.use('ggplot')

def div_boxplt(data, xlabel = None, ylabel = None):
	data.plot(kind='box')
	plt.xlabel(xlabel, fontsize = 12)
	plt.ylabel(ylabel, fontsize = 12)
	plt.xticks(fontsize = 11)
	plt.yticks(fontsize = 11)

# read data
# air = pd.read_csv('2007_ORD.csv', encoding = "ISO-8859-1")
weather_1 = pd.read_csv('2007_weather_delay.csv', encoding = "ISO-8859-1")
weather_2 = pd.read_csv('2008_weather_delay.csv', encoding = "ISO-8859-1")

print weather_1.describe()
print weather_2.describe()

# col_1 = ['Date', 'DayOfWeek', 'UniqueCarrier', 'CRSDepTime', 'Distance', 'ArrClass']
# air = air[col_1]
# air = air.sort_values(by = 'Date')

# col_2 = ['Date', 'meanvism', 'meanwindspdm', 'thunder']
# weather = weather[col_2]
# weather = weather.sort_values(by = 'Date')

# air_weather = air.merge(weather, left_on = 'Date', right_on = 'Date', how = 'left')

# air_weather.to_csv('2008_airline_weather_merge.csv')
# print air_weather.head()

# div_boxplt(air[['ArrDelay','DepDelay']], xlabel='Delay Type', ylabel='Delay Time (min)')
# plt.show()

# z = np.polyfit(x=air.loc[:, 'CRSElapsedTime'], y=air.loc[:, 'Distance'], deg=1)
# p = np.poly1d(z)
# air['trendline'] = p(air.loc[:, 'CRSElapsedTime'])

# ax = air.plot.scatter(x = 'CRSElapsedTime', y = 'Distance')
# air.set_index('CRSElapsedTime', inplace=True)
# air.trendline.sort_index(ascending=False).plot(ax=ax)
# plt.gca().invert_xaxis()
# plt.xlabel('Scheduled flight time (min)')
# plt.ylabel('Distance (km)')
# plt.show()

# air = air.sort_values('CRSArrTime', ascending = True)
# air.plot(x = 'CRSArrTime', y = 'ArrDelay', color = 'black')
# plt.xlabel('Scheduled Arrive Time (min)')
# plt.ylabel('Arrival Delay (min)')
# plt.show()


