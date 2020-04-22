import pandas as pd
import plotly.graph_objects as go
from random import random, randint
import math

#Configuration Options
PERIODIC_AVERAGES_FILE_PATH = 'data/monthly_averages.xlsx'
PERIODIC_AVERAGES_SKIPROWS = []
BAR_DATA_FILE_PATH = 'data/weatherstndata.xlsx'
BAR_DATA_SKIPROWS = [1]
OUTPUT_FILE_PATH = 'data/weatherstndata_chart.png'

# Read in the hourly bars
hourly_rainfall = pd.read_excel(BAR_DATA_FILE_PATH, header=0, skiprows=BAR_DATA_SKIPROWS)
# Read in the monthly averages
print(hourly_rainfall['PG_1hr'])
#monthly_averages = pd.read_excel(PERIODIC_AVERAGES_FILE_PATH, header=0, skiprows=PERIODIC_AVERAGES_SKIPROWS)
# Create a bar chart of the hourly data
fig = go.Figure(data=[go.Bar(x=hourly_rainfall['DateTime'],
                             y=hourly_rainfall['PG_1hr'],
                             marker_color='black')])
fig.update_layout(bargap=1)
fig.update_yaxes(range=[-1, int(math.ceil(max(hourly_rainfall['PG_1hr'])))])

fig.show()

# Add lines for each monthly average
