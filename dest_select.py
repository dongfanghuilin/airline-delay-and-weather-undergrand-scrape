import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import graph

matplotlib.style.use('ggplot')


# read data
sample = pd.read_csv('2007.csv', encoding = "ISO-8859-1")

# # Count Missing Values for each attribute
# col_names = list(sample)

# cat_var = ['Unnamed: 0', 'UniqueCarrier', 'FlightNum', 'TailNum', 'Origin', 'Dest', 
# 'Cancelled', 'CancellationCode', 'Diverted']
# date_var = ['Year', 'Month', 'DayofMonth', 'DayOfWeek']
# unformat_time_var = ['DepTime', 'CRSDepTime', 'ArrTime', 'CRSArrTime']
# num_var = ['ActualElapsedTime', 'CRSElapsedTime', 'AirTime', 'ArrDelay', 'DepDelay', 
# 'Distance', 'TaxiIn', 'TaxiOut', 'CarrierDelay', 'WeatherDelay', 'NASDelay', 
# 'SecurityDelay', 'LateAircraftDelay']

# row_count = sample['Year'].count()

# for i in col_names:
# 	df_1 = sample[sample[i].isnull() == True][i]
# 	df_2 = df_1.fillna(0)
# 	print (i,',',df_2.count()/row_count)


# # Determine the number of outliers for each numeric attribute
# for i in num_var:
# 	df_1 = sample[sample[i].isnull() == False][i]
# 	outlier = df_1[(df_1-df_1.mean()).abs() > 3*df_1.std()]
# 	print (i,',',outlier.count()/row_count)

# Dest_count = sample.groupby('Dest').Year.agg('count')
# Dest_count = Dest_count.sort_values(ascending = False)
# dest_median = Dest_count.median()
# print (dest_median)
# print (dest_median/row_count)
# Dest_count.to_csv('Destination_count_2008.csv')


# plt.hist(Dest_count, normed = True)
# plt.xlabel('Number of flights', fontsize = 14)
# plt.ylabel('Frequency', fontsize = 14)
# plt.title('Histogram for number of flights in different destinations (2007)', fontsize = 18)
# plt.show()


# ArrDelay ~ Arrive Time/Destination

# Arr = sample[['Dest', 'ArrDelay']]
# Arr_df = Arr[Arr['ArrDelay'].notnull()]
# Arr_3 = Arr_df.groupby('Dest').ArrDelay.mean()
# Arr_3.sort_values(inplace = True, ascending = False)

# plt.hist(Arr_3, normed = True)
# plt.xlabel('Arrival delay time (min)', fontsize = 14)
# plt.ylabel('Frequency', fontsize = 14)
# plt.title('Histogram for arrival delays in different destinations (2007)', fontsize = 18)
# plt.show()

# Arr_dest_count = pd.concat([Arr_3, Dest_count], axis = 1)

# Arr_dest_count.plot(kind = 'scatter', y = 'ArrDelay', x = 'Year')
# plt.ylabel('Average arrival delay time (min)', fontsize=14)
# plt.xlabel('Number of flights',fontsize=14)
# plt.title('Arrival delay ~ Number of flights in different destinations',fontsize=18)
# plt.show()


# Arr_dest_count.to_csv('ArrDelay_dest_2007.csv')


dest_selected = 'ORD'
column_selected = ['Year', 'Month','DayofMonth', 'DayOfWeek', 'Dest', 'Cancelled',
'UniqueCarrier' ,'Diverted', 'DepTime','CRSDepTime', 'ArrTime','CRSArrTime', 
'ActualElapsedTime', 'CRSElapsedTime', 'AirTime', 'ArrDelay', 'DepDelay','Distance']
sample_selected = sample.loc[sample['Dest'] == dest_selected][column_selected]
sample_selected = sample_selected.loc[sample_selected['Cancelled'] != 1]
sample_selected = sample_selected.loc[sample_selected['ArrTime'].notnull()]
sample_selected = sample_selected.loc[sample_selected['DepTime'].notnull()]
sample_selected = sample_selected.loc[sample_selected['ArrDelay'].notnull()]
sample_selected.to_csv('2007_selected.csv')