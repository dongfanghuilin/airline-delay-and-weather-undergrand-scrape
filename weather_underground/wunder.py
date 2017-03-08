import urllib2
import json
import re
import pandas as pd
from datetime import date, datetime, timedelta as td

# columns we are intereseted in are listed here
col_names_full = ['Date', 'state', 'city','fog', 'rain', 'snow', 'hail', 'thunder', 'tornado', 'meantempm', 
'maxtempm', 'mintempm', 'meanwindspdm', 'meanvism', 'precipm']

# columns we will scrape from the web
col_names = ['fog', 'rain', 'snow', 'hail', 'thunder', 'tornado', 'meantempm', 
'maxtempm', 'mintempm', 'meanwindspdm', 'meanvism', 'precipm']

# create a dataframe to store data
weather = pd.DataFrame(columns = col_names_full)
weather = weather.fillna(0)

# set the format of the url, 'cf4e99ce6a5a4f52' is my api key
url = "http://api.wunderground.com/api/cf4e99ce6a5a4f52/history_date/q/statecode/city.json"

# set the time period here
d1 = date(2006, 1, 1)
d2 = date(2006, 12, 31)

delta = d2 - d1

# start to scrape
for i in range(delta.days + 1):
	date_1 = d1 + td(days=i)
	date_2 = datetime.strftime(date_1, "%Y%m%d")

# edit state and city name here
	state = 'CA'
	city = 'San_Francisco' 

# set the correct url
	url_date = re.sub('history_date/q/statecode/city', 'history_%s/q/%s/%s' %(date_2,state,city), url)

	f = urllib2.urlopen(url_date)
	json_string = f.read()
	parsed_json = json.loads(json_string)

# get the daily summary
	daily_summary= parsed_json['history']['dailysummary']
	daily = pd.DataFrame(daily_summary, columns = col_names)

	daily['Date'] = date_1
	daily['state'] = state
	daily['city'] = city

# append the data to the dataframe
	weather = pd.concat([weather, daily])

	f.close()

# save the data to a csv file
weather.to_csv('weather.csv')
