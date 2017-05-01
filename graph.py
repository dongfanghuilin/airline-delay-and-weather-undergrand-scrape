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

