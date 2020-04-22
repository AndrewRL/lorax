import pandas as pd

# Configuration Options
INPUT_FILE_PATH = 'data/weatherstndata.xlsx'
INPUT_ROWS_TO_SKIP = [1]
INPUT_DATE_COLUMN_NAME = 'DateTime'
OUTPUT_FILE_PATH = 'data/weatherstndata_filtered.xlsx'
FILTER_YEARS = [2019]

if not FILTER_YEARS:
    raise ValueError("You must provide at least one year to filter.")

# Read in the input file and convert the specified date column to a DatetimeIndex
data = pd.read_excel(INPUT_FILE_PATH, header=0, skiprows=[1])
data[INPUT_DATE_COLUMN_NAME] = pd.to_datetime(data[INPUT_DATE_COLUMN_NAME])
df = data.set_index(pd.DatetimeIndex(data[INPUT_DATE_COLUMN_NAME]))
df.index = df.index.rename(INPUT_DATE_COLUMN_NAME + " Index")

filtered = df[(df.index.year.isin(FILTER_YEARS))]

filtered = filtered.set_index(filtered['Unnamed: 0'])
filtered.index = filtered.index.rename('')
filtered.drop('Unnamed: 0', axis=1, inplace=True)

filtered.to_excel(OUTPUT_FILE_PATH)