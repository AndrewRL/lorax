import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
import calendar
from datetime import datetime


#Configuration Options
PERIODIC_AVERAGES_FILE_PATH = 'data/monthly_averages.xlsx'
PERIODIC_AVERAGES_SKIPROWS = []
BAR_DATA_FILE_PATH = 'data/weatherstndata_filtered.xlsx'
BAR_DATA_SKIPROWS = [1]
BAR_DATA_DATE_COLUMN_NAME = 'DateTime'
BAR_DATA_DATA_COLUMN_NAME = 'PG_1hr'
OUTPUT_FILE_PATH = 'data/weatherstndata_chart.png'

# Read in the hourly bars
bar_data = pd.read_excel(BAR_DATA_FILE_PATH, header=0, skiprows=BAR_DATA_SKIPROWS)
bar_data[BAR_DATA_DATE_COLUMN_NAME] = pd.to_datetime(bar_data[BAR_DATA_DATE_COLUMN_NAME], format='%Y-%b-%d %H:%M:%S')
# Read in the monthly averages
print(bar_data[BAR_DATA_DATA_COLUMN_NAME])
monthly_averages = pd.read_excel(PERIODIC_AVERAGES_FILE_PATH, header=0, skiprows=PERIODIC_AVERAGES_SKIPROWS)

fig, ax = plt.subplots()
ax.bar(BAR_DATA_DATE_COLUMN_NAME, BAR_DATA_DATA_COLUMN_NAME, data=bar_data, color='black')

month_starts = [datetime(2019, month, 1, 0, 0, 0) for month in range(1, 13)]
month_starts.append(datetime(2020, 1, 1, 0, 0, 0))

for index, average in enumerate(monthly_averages['Average Precip (mm)']):
    plt.plot([month_starts[index], month_starts[index+1]], [average, average], color='crimson')

months = mdates.MonthLocator()
months_fmt = mdates.DateFormatter('%b %Y')
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(months_fmt)

datemin = pd.to_datetime(bar_data[BAR_DATA_DATE_COLUMN_NAME].iloc[0], format='%Y-%b-%d %H:%M:%S')
datemax = pd.to_datetime(bar_data[BAR_DATA_DATE_COLUMN_NAME].iloc[-1], format='%Y-%b-%d %H:%M:%S')
ax.set_xlim(datemin, datemax)

plt.bar(bar_data['DateTime'], bar_data['PG_1hr'])
plt.title('Monthly Rainfall Averages with Daily Rainfall Bars for 2019')
plt.xlabel('Month')
plt.ylabel('Precipitation (mm)')
plt.grid(True)

fig.autofmt_xdate()

plt.savefig(OUTPUT_FILE_PATH)