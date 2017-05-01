import datetime
from datetime import date
import pandas as pd
import numpy as np


# def time_format_1(df, column):
# 	for j in df.index:
# 		i = df[column][j]
# 		i = str(int(i))
# 		if len(i) == 4:
# 			i = pd.to_datetime(i, format='%H%M', errors = 'ignore')
# 		elif len(i) == 3:
# 			i = '0'+i
# 			i = pd.to_datetime(i, format='%H%M', errors = 'ignore')
# 		elif len(i) == 2:
# 			i = '00'+i
# 			i = pd.to_datetime(i, format='%H%M', errors = 'ignore')
# 		elif len(i) == 1:
# 			i = '000'+i
# 			i = pd.to_datetime(i, format='%H%M', errors = 'ignore')
# 		df.set_value(j, column, i)

# def time_format_2(df, column):
# 	for i in df.index:
# 		j = df[column][i]
# 		j = j.replace('1900-01-01 ', '')
# 		df.set_value(i, column, j)




# sample = pd.read_csv('2008_selected.csv', encoding = "ISO-8859-1")

# time_format_1(df = sample, column = 'CRSArrTime')
# time_format_1(df = sample, column = 'ArrTime')
# time_format_1(df = sample, column = 'CRSDepTime')
# time_format_1(df = sample, column = 'DepTime')

# sample.to_csv('2008_ORD_formated.csv')

sample_1 = pd.read_csv('2008_ORD_formated_1.csv', encoding = "ISO-8859-1")
# time_format_2(df = sample_1, column = 'CRSArrTime')
# time_format_2(df = sample_1, column = 'ArrTime')
# time_format_2(df = sample_1, column = 'CRSDepTime')
# time_format_2(df = sample_1, column = 'DepTime')

for i in sample_1.index:
	j = date(sample_1['Year'][i], sample_1['Month'][i], sample_1['DayofMonth'][i])
	j = j.strftime("%d/%m/%y")
	sample_1.set_value(i, 'Date', j)

sample_1.to_csv('2008_ORD_formated_2.csv')
