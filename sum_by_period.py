# Takes a date column and a data column and aggregates the data column over the specified intervals
import pandas as pd
import numpy as np
from sys import argv

# Configuration Options
INPUT_FILE_PATH = 'data/weatherstndata_filtered.xlsx'
INPUT_DATE_COLUMN_NAME = 'DateTime'
INPUT_DATE_FORMAT = '%Y-%b-%D %h:%m:%s'
SKIP_INPUT_ROWS = [1]
INPUT_DATA_COLUMN_NAME = 'PG_1hr'
AGGREGATION_PERIOD = 'M'
OUTPUT_FILE_PATH = 'data/monthly_averages.xlsx'
OUTPUT_INDEX_HEADER = 'Month'
OUTPUT_DATETIMEINDEX_FORMAT = '%B %Y'
OUTPUT_DATA_HEADER = 'Average Precip (mm)'

# Read in the Excel file and use the specified date column to create a pandas DatetimeIndex
data = pd.read_excel(INPUT_FILE_PATH, header=0, skiprows=[1])
data[INPUT_DATE_COLUMN_NAME] = pd.to_datetime(data[INPUT_DATE_COLUMN_NAME])
dates = data[INPUT_DATE_COLUMN_NAME]
df = data.drop(INPUT_DATE_COLUMN_NAME, axis=1)
df = df.set_index(pd.DatetimeIndex(dates))

# Average the data over the specified period(s)
period_groups = df.groupby(pd.Grouper(freq=AGGREGATION_PERIOD), group_keys=df.index.month_name())
period_sums = period_groups.agg(period_sum = pd.NamedAgg(column=INPUT_DATA_COLUMN_NAME, aggfunc=sum))

# Reformat DatetimeIndex based on user-provided format
period_sums.index = period_sums.index.strftime(OUTPUT_DATETIMEINDEX_FORMAT)

# Rename columns based on user-provided names
period_sums.index = period_sums.index.rename(OUTPUT_INDEX_HEADER)
period_sums.rename(columns = {'period_sum': 'Average Precip (mm)'}, inplace=True)

# Write the results to the specified output path
period_sums.to_excel(OUTPUT_FILE_PATH)