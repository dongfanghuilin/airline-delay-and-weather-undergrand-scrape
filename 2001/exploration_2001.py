import datetime
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# import graph

matplotlib.style.use('ggplot')

# custmerize plots
def air_histplt(data, column, facecolor = 'red', xlabel=None, ylabel=None, title=None):
	x = data[column]
	plt.hist(x, facecolor = facecolor, normed = True)
	#add 'best fit' line
	plt.axvline(x.mean(), color = 'black', linewidth = 2, linestyle = 'dashed')
	plt.text(x.mean()+30, 0.003, 'Mean = ', fontsize = 12)
	plt.text(x.mean()+250, 0.003, int(x.mean()), fontsize = 12)
	plt.xlabel(xlabel, fontsize = 14)
	plt.ylabel(ylabel, fontsize = 14)
	plt.title(title, fontsize = 18)

def air_row_histplt(data, column, row, facecolor = 'red', xlabel=None, ylabel=None, title=None):
	x = data[row][column]
	plt.hist(x, facecolor = facecolor, normed = True)
	#add 'best fit' line
	plt.axvline(x.mean(), color = 'black', linewidth = 2, linestyle = 'dashed')
	plt.text(x.mean()+10, 0.01, 'Mean = ', fontsize = 12)
	plt.text(x.mean()+65, 0.01, int(x.mean()), fontsize = 12)
	plt.xlabel(xlabel, fontsize = 14)
	plt.ylabel(ylabel, fontsize = 14)
	plt.title(title, fontsize = 18)

def delay_airtime_scatplot(data, title='Flight Delay ~ Fly Time'):
	fig, axarr = plt.subplots(2, sharex = True)
	data.plot(ax = axarr[0], kind = 'scatter', x = 'air_mean', y = 'arr_mean', color = 'green')
	axarr[0].set_ylabel('Arrive (min)')
	axarr[0].set_title(title)
	data.plot(ax = axarr[1], kind = 'scatter', x = 'air_mean', y = 'dep_mean', color = 'blue')
	axarr[1].set_xlabel('Average Fly Time (min)')
	axarr[1].set_ylabel('Departure (min)')

def carr_barplt(data, kind = 'bar', facecolor='red', xlabel=None, ylabel=None, title=None):
	data.plot(kind=kind, facecolor=facecolor)
	plt.xlabel(xlabel, fontsize = 18)
	plt.ylabel(ylabel, fontsize = 18)
	plt.xticks(fontsize = 14)
	plt.yticks(fontsize = 14)
	plt.title(title, fontsize = 20)

def div_histplt(data, column, facecolor = 'red', xlabel=None, ylabel=None, title=None):
	x = data[column]
	plt.hist(x, facecolor = facecolor, normed = True)
	plt.xlabel(xlabel, fontsize = 18)
	plt.ylabel(ylabel, fontsize = 18)
	plt.xticks(fontsize = 14)
	plt.yticks(fontsize = 14)
	plt.title(title, fontsize = 20)

def div_boxplt(data, xlabel = None, ylabel = None, title = None):
	data.plot(kind='box')
	plt.xlabel(xlabel, fontsize = 18)
	plt.ylabel(ylabel, fontsize = 18)
	plt.xticks(fontsize = 14)
	plt.yticks(fontsize = 14)
	plt.title(title, fontsize = 20)

def ap_barplt(data, kind = 'bar', xlabel=None, ylabel=None, title=None):
	data.plot(kind=kind)
	plt.xlabel(xlabel, fontsize = 18)
	plt.ylabel(ylabel, fontsize = 18)
	plt.xticks(fontsize = 14)
	plt.yticks(fontsize = 14)
	plt.title(title, fontsize = 20)


# read data
sample = pd.read_csv('air_01_sample01_1.csv', encoding = "ISO-8859-1")

# # Count Missing Values for each attribute
col_names = list(sample)

cat_var = ['Unnamed: 0', 'UniqueCarrier', 'FlightNum', 'TailNum', 'Origin', 'Dest', 
'Cancelled', 'CancellationCode', 'Diverted']
date_var = ['Year', 'Month', 'DayofMonth', 'DayOfWeek']
unformat_time_var = ['DepTime', 'CRSDepTime', 'ArrTime', 'CRSArrTime']
num_var = ['ActualElapsedTime', 'CRSElapsedTime', 'AirTime', 'ArrDelay', 'DepDelay', 
'Distance', 'TaxiIn', 'TaxiOut', 'CarrierDelay', 'WeatherDelay', 'NASDelay', 
'SecurityDelay', 'LateAircraftDelay']

# for i in col_names:
# 	df_1 = sample[sample[i].isnull() == False][i]
# 	df_2 = df_1.fillna(0)
# 	print (i,',',df_2.count())


# # Determine the number of outliers for each numeric attribute
# for i in num_var:
# 	df_1 = sample[sample[i].isnull() == False][i]
# 	outlier = df_1[(df_1-df_1.mean()).abs() > 3*df_1.std()]
# 	print (i,',',outlier.count())

# sample = sample.fillna(0)


# # Calculate distance
# print (sample['Distance'].describe())

# air_histplt(sample, 'Distance', xlabel = 'Distance (km)',
# 	ylabel = 'Frequency', title = '2001 Histogram for flying distance')
# plt.show()


# hist plot about Airtime, arrdelay, depdelay

# AirTime
# air_histplt(sample, 'AirTime', facecolor = 'red', xlabel='Fly time (min)', 
# 	ylabel='Frequency', title='2001 Histogram for flying time')
# plt.show()

# ArrDelay
# air_histplt(sample, 'ArrDelay', facecolor='green',xlabel='Arrive Delay (min)', 
# 	ylabel='Frequency', title='2001 Histogram for Arrive Delay Time')
# plt.show()

# Filter the delay time to less than 250
# row = sample['ArrDelay'] < 250
# air_row_histplt(sample, 'ArrDelay', row, facecolor = 'green', xlabel='Arrive Delay (min)', 
# 	ylabel='Frequency', title='2001 Histogram for Arrive Delay Time <250 min')
# plt.show()

# DepDelay
# air_histplt(sample, 'DepDelay', facecolor='green',xlabel='Departure Delay (min)', 
# 	ylabel='Frequency', title='2001 Histogram for Departure Delay Time')
# plt.show()

# Filter the delay time to less than 250
# row = sample['DepDelay'] < 250
# air_row_histplt(sample, 'DepDelay', row, facecolor='blue',xlabel='Departure Delay (min)', 
# 	ylabel='Frequency', title='2001 Histogram for Departure Delay Time')
# plt.show()


# plot showing the relationship between average fly time and average delays

# tb1 = pd.pivot_table(sample, values=['AirTime','ArrDelay','DepDelay'], 
# 	columns = ['Year','Month','DayofMonth'], aggfunc = [np.mean, np.std])
# tb1.to_csv('2001_mean_airtime_delay.csv')
# print (tb1.head())
#                                      mean        std
#         Year Month DayofMonth                       
# AirTime 2001 1     1            94.690418  70.156713
#                    2            96.916384  67.776407
#                    3            99.917555  69.639326
#                    4           100.703266  68.528224
#                    5            98.398019  71.670631



# tb2 = pd.read_csv('2001_mean_airtime_delay.csv')
# ind1 = tb2['Type'] == 'AirTime'
# mean_air = tb2[ind1]['mean']
# airtime = pd.DataFrame(mean_air)
# airtime = airtime.set_index(pd.date_range('1/1/2001', periods=365))
# airtime = airtime.rename(columns = {'mean':'air_mean'})

# ind2 = tb2['Type'] == 'ArrDelay'
# ind3 = tb2['Type'] == 'DepDelay'
# mean_arrD = tb2[ind2]['mean']
# arrD = pd.DataFrame(mean_arrD)
# arrD = arrD.set_index(pd.date_range('1/1/2001', periods=365))
# arrD = arrD.rename(columns = {'mean':'arr_mean'})

# mean_depD = tb2[ind3]['mean']
# depD = pd.DataFrame(mean_depD)
# depD = depD.set_index(pd.date_range('1/1/2001', periods=365))
# depD = depD.rename(columns = {'mean':'dep_mean'})

# df1 = pd.merge(airtime, arrD, left_index=True, right_index=True, how='outer')
# df2 = pd.merge(df1, depD, left_index=True, right_index=True, how='outer')
# # df2.to_csv('2001_mean_airtime_delay_2.csv')
# df3 = df2.sort_values(by = 'air_mean')
# # print df3.head()
# print df2.head()


# # plot AirDelay ~ Monthly
# tb3 = pd.pivot_table(sample, values=['ArrDelay','DepDelay'], 
# 	columns = ['Month'], aggfunc = np.mean)
# df4 = tb3.transpose()
# df4.plot()
# plt.xticks(fontsize = 14)
# plt.yticks(fontsize = 14)
# plt.xlabel('Month', fontsize = 18)
# plt.ylabel('Average Delay Time (min)', fontsize = 18)
# plt.title('2001 Flight Delay - Monthly', fontsize = 20)
# plt.show()


# # plot AirTime ~ Date
# airtime.plot()
# plt.xticks(fontsize = 14)
# plt.yticks(fontsize = 14)
# plt.xlabel('Date', fontsize = 18)
# plt.ylabel('Fly Time', fontsize = 18)
# plt.title('2001 Average Fly Time', fontsize = 18)
# plt.show()

# # plot Delay ~ Date
# plt.figure()
# df2.plot(y=['arr_mean', 'dep_mean'])
# plt.xticks(fontsize = 14)
# plt.yticks(fontsize = 14)
# plt.xlabel('Date', fontsize = 18)
# plt.ylabel('Average Delay Time (min)', fontsize = 18)
# plt.legend(['Arrive Delay', 'Departure Delay'], loc='best', fontsize = 18)
# plt.title('2001 Flight Delay - Daily', fontsize = 20)
# plt.show()


# # # plot AirDelay ~ AirTime
# delay_airtime_scatplot(df2, title = '2001 Flight Delay ~ Fly Time')
# plt.show()


# # plot AirDelay ~ AirTime
# df5 = df2[df2['air_mean'] > 80]

# delay_airtime_scatplot(df5, title = '2001 Flight Delay ~ Fly Time >80 min')
# plt.show()


# # Explore the relationship between Carriers and Delays
# carr_df = sample[['UniqueCarrier','ArrDelay','DepDelay']]
# carr_count = carr_df['UniqueCarrier'].value_counts()
# # print carr_count
# # # Carriers Descending
# # WN    95382
# # DL    83648
# # AA    71942
# # UA    70578
# # US    68873
# # NW    53011
# # MQ    48668
# # CO    37770
# # TW    24805
# # HP    21055
# # AS    15696
# # AQ     5350
# carr_count.sort()
# carr_count.plot(kind='barh')
# plt.xlabel('Number of Flights')
# plt.ylabel('Carrier')
# plt.title('2001 Carrier Scale')
# plt.show()

# carr_D = carr_df.groupby('UniqueCarrier').mean()
# print carr_D
#                 ArrDelay   DepDelay
# UniqueCarrier                      
# AA              5.434322   8.664813
# AQ              4.318879   3.658879
# AS             11.281346  10.833524
# CO              3.231559   5.506963
# DL              4.715427   7.118162
# HP              8.377345   9.773735
# MQ              7.207364   9.763541
# NW              3.126125   5.717945
# TW              4.157428   5.822334
# UA              8.392105  10.641177
# US              3.301511   5.538963
# WN              4.736481   8.557579

# # bar chart for average delay time ~ carriers
# ap_barplt(carr_D, kind = 'bar',
# 	xlabel = 'Carrier',
# 	ylabel = 'Average Delay Time (min)',
# 	title = '2001 Delay Time ~ Carrier')
# plt.xticks(rotation = 10)
# plt.show()

# # bar chart for ranking the average delay time ~ carriers
# carr_D['Average_Delay'] = (carr_D['ArrDelay']+carr_D['DepDelay'])/2
# carr_avg = carr_D.sort_values('Average_Delay', ascending = False)
# carr_barplt(carr_avg['Average_Delay'], kind = 'barh',
# 	xlabel = 'Average Delay Time (based on Arrive and Departure) (min)',
# 	ylabel = 'Carrier',
# 	title = '2001 Average Delay Time for different Carriers')
# plt.show()

# carr_count = pd.DataFrame(carr_count.sort_index())
# carr_D.sort_index()
# carr_delay = pd.merge(carr_count,carr_D, left_index=True, right_index=True, how='outer')
# # carr_delay.to_csv('2001_Carrier_Delay.csv')


# carr_delay['Flight_counts'] = carr_delay['UniqueCarrier']/5000
# df_temp = carr_delay[['Average_Delay','Flight_counts']]
# df_temp = df_temp.sort_values('Flight_counts', ascending=False)
# carr_barplt(df_temp, kind = 'bar',
# 	xlabel = 'Carrier',
# 	ylabel = 'Average Delay Time (min) or Counts/5000',
# 	title = '2001 Average Delay Time for Carriers')
# plt.show()


# # Diverted Flight ~ Delay
# div_df = sample[sample['Diverted'] != 0]
# print (div_df['Diverted'].value_counts())  # 1315
# div_df = div_df[['Year','Month','DayofMonth','UniqueCarrier','ArrDelay','DepDelay']]
# div_df.to_csv('2001_diverted_carrier_delay.csv')
# print div_df.head()
#       Month  DayofMonth UniqueCarrier  ArrDelay  DepDelay
# 113       9          11            AA       0.0       4.0
# 761       1           9            US       0.0      21.0
# 1956      5           7            CO       0.0      23.0
# 2160      6          22            US       0.0     242.0
# 2334     10           1            NW       0.0       4.0
# print div_df['ArrDelay'].mean()

# # Boxplot for Delay time
# div_1 = div_df[['ArrDelay','DepDelay']]
# div_boxplt(div_1, xlabel = 'Delay Type', ylabel = 'Delay Time (min)', 
# 	title = '2001 Delay Time for Diverted Flights')
# plt.show()

# # Departure Delay has a lot of outliers

# # Histogram for Departure Delay
# air_histplt(div_df, 'DepDelay', xlabel='Departure Delay Time (min)', 
# 	ylabel='Frequency', title = '2001 Departure Delay Time of Diverted Flights')
# plt.show()

# div_2 = div_df[div_df['DepDelay'] > 120]
# div_histplt(div_2, 'DepDelay', xlabel='Departure Delay Time (min)', 
# 	ylabel='Frequency', title = '2001 Departure Delay >120 min of Diverted Flights')
# plt.show()


# # ArrDelay ~ Arrive Time/Destination
# # DepDelay ~ Departure Time/Origin

# Arr = sample[['ArrTime', 'Dest', 'ArrDelay']]
# Dep = sample[['DepTime', 'Origin', 'DepDelay']]
# Arr_df = Arr[Arr['ArrTime'].notnull()]
# Dep_df = Dep[Dep['DepTime'].notnull()]
# print Arr.head()
#    ArrTime Dest  ArrDelay
# 0   1857.0  ATL      -9.0
# 1   1231.0  IAH     -12.0
# 2   2150.0  SJC     224.0
# 3   1932.0  LGA      26.0
# 4   1207.0  AZO      -5.0

# Change ArrTime format
# for j in Arr_df.index:
# 	i = Arr_df['ArrTime'][j]
# 	i = str(int(i))
# 	if len(i) == 4:
# 		i = pd.to_datetime(i, format='%H%M', errors = 'ignore')
# 	elif len(i) == 3:
# 		i = '0'+i
# 		i = pd.to_datetime(i, format='%H%M', errors = 'ignore')
# 	elif len(i) == 2:
# 		i = '00'+i
# 		i = pd.to_datetime(i, format='%H%M', errors = 'ignore')
# 	elif len(i) == 1:
# 		i = '000'+i
# 		i = pd.to_datetime(i, format='%H%M', errors = 'ignore')
# 	Arr_df.set_value(j, 'ArrTime', i)
	
# Arr_df.to_csv('2001_ArrTime_Dest_Delay.csv')


# # Change the datetime format in the document
# Arr_1 = pd.read_csv('2001_ArrTime_Dest_Delay.csv')
# for i in Arr_1.index:
# 	j = Arr_1['ArrTime'][i]
# 	j = j.replace('1900-01-01 ', '')
# 	Arr_1.set_value(i, 'ArrTime', j)
# Arr_1.to_csv('2001_ArrTime_Dest_Delay.csv')


# Change DepTime format
# for j in Dep_df.index:
# 	i = Dep_df['DepTime'][j]
# 	i = str(int(i))
# 	if len(i) == 4:
# 		i = pd.to_datetime(i, format='%H%M', errors = 'ignore')
# 	elif len(i) == 3:
# 		i = '0'+i
# 		i = pd.to_datetime(i, format='%H%M', errors = 'ignore')
# 	elif len(i) == 2:
# 		i = '00'+i
# 		i = pd.to_datetime(i, format='%H%M', errors = 'ignore')
# 	elif len(i) == 1:
# 		i = '000'+i
# 		i = pd.to_datetime(i, format='%H%M', errors = 'ignore')
# 	i = i.
# 	Dep_df.set_value(j, 'DepTime', i)
	
# Dep_df.to_csv('2001_DepTime_Dest_Delay.csv')


# # Change the datetime format in the document
# Dep_1 = pd.read_csv('2001_DepTime_Dest_Delay.csv')
# for i in Dep_1.index:
# 	j = Dep_1['DepTime'][i]
# 	j = j.replace('1900-01-01 ', '')
# 	Dep_1.set_value(i, 'DepTime', j)
# Dep_1.to_csv('2001_DepTime_Dest_Delay.csv')


# Arr_1 = pd.read_csv('2001_ArrTime_Dest_Delay.csv')

# # Plot ArrDelay ~ ArrTime
# Arr_2 = Arr_1.groupby('ArrTime').ArrDelay.mean()
# Arr_2.plot()
# plt.xlabel('Arrive Time', fontsize = 16)
# plt.ylabel('Average Arrive Delay (min)', fontsize = 16)
# plt.title('2001 Average Arrive Delay at different Arrive Time', fontsize = 18)
# plt.show()

# # Plot ArrDelay ~ Dest
# Arr_3 = Arr_1.groupby('Dest').ArrDelay.mean()
# # Arr_3.sort_values(inplace = True, ascending = False)
# # Arr_3.to_csv('2001_Dest_ArrDelay.csv')

# # Top 10 Arrive Early/Delay Airports
# Arr_3.sort_values(inplace = True, ascending = True)
# Arr_early = Arr_3[:10]
# Arr_late = Arr_3[-10:]
# Arr_t_b = Arr_early.append(Arr_late)
# carr_barplt(Arr_t_b, facecolor = 'green', xlabel = 'Airport', ylabel = 'Arrive Delay (min)',
# 	title = '2001 Top 10 Arrive Early/Delay Destinations')
# plt.xticks(rotation=30)
# plt.show()



# Dep_1 = pd.read_csv('2001_DepTime_Origin_Delay.csv')

# # Plot DepDelay ~ DepTime
# Dep_2 = Dep_1.groupby('DepTime').DepDelay.mean()
# Dep_2.plot()
# plt.xlabel('Departure Time', fontsize = 16)
# plt.ylabel('Average Departure Delay (min)', fontsize = 16)
# plt.title('2001 Average Departure Delay at different Departure Time', fontsize = 18)
# plt.show()

# # Plot ArrDelay ~ Dest
# Dep_3 = Dep_1.groupby('Origin').DepDelay.mean()
# # Dep_3.sort_values(inplace = True, ascending = False)
# # Dep_3.to_csv('2001_Origin_DepDelay.csv')

# # Top 10 Departure Early/Delay Airports
# Dep_3.sort_values(inplace = True, ascending = True)
# Dep_early = Dep_3[:10]
# Dep_late = Dep_3[-10:]
# Dep_t_b = Dep_early.append(Dep_late)
# carr_barplt(Dep_t_b, facecolor = 'green', xlabel = 'Airport', ylabel = 'Departure Delay (min)',
# 	title = '2001 Top 10 Departure Early/Delay Origins')
# plt.xticks(rotation=30)
# plt.show()

# # Top 10 Overall Early/Delay Airports
# Arr_3 = pd.DataFrame(Arr_3.sort_index())
# Dep_3 = pd.DataFrame(Dep_3.sort_index())
# Airport_D = pd.merge(Arr_3, Dep_3, left_index=True,
# 	right_index=True, how='outer')
# Airport_D['Avg_Delay'] = (Airport_D['ArrDelay']+Airport_D['DepDelay'])/2
# # Airport_D.to_csv('2001_Airport_Delay.csv')

# Airport_D.fillna(0)
# Ap_sort = Airport_D.sort_values('Avg_Delay')
# Ap_overall = Ap_sort[:10].append(Ap_sort[-10:])
# ap_barplt(Ap_overall, xlabel = 'Airport', ylabel = 'Delay (min)',
# 	title = '2001 Top 10 Early/Delay Airports')
# plt.xticks(rotation=30)
# plt.show()












