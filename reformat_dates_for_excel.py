import pandas as pd

# Configuration Options
INPUT_FILE_PATH = 'data/weatherstndata.xlsx'
OUTPUT_FILE_PATH = 'data/weatherstndata_with_excel_dates.xlsx'
INPUT_DATE_COLUMN_NAMES = ['DateTime']
INPUT_DATE_FORMAT = '%Y-%b-%d %H:%M:%S'
SKIP_INPUT_ROWS = [1]

if not INPUT_DATE_COLUMN_NAMES:
    raise ValueError("You must provide at least one column of dates to convert.")

# Read in an Excel file

data = pd.read_excel(INPUT_FILE_PATH, header=0, skiprows=SKIP_INPUT_ROWS)
for column in INPUT_DATE_COLUMN_NAMES:
    data[column] = pd.to_datetime(data[column], format=INPUT_DATE_FORMAT)
    data[column] = data[column].dt.strftime('%m/%d/%Y %I:%M:%S %p')

data.to_excel(OUTPUT_FILE_PATH)

# NOTE! You MUST go to Data -> Text to Columns -> Finish to get Excel to recognize the formatted dates.
# You do not need to change any options in Text to Columns