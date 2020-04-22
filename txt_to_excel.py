import pandas as pd
from sys import argv

# Configuration options
INPUT_FILE_PATH = 'data/weatherstndata.txt'
INPUT_DELIMITER = ','
OUTPUT_FILE_PATH = 'data/weatherstndata.xlsx'

# Read in text file
data = pd.read_table(INPUT_FILE_PATH, sep=INPUT_DELIMITER)
data.to_excel(OUTPUT_FILE_PATH)

