"""test file for learning py in github codespaces"""

from pydoc import describe
import requests

import pandas as pd
# print(pd.__version__)

pd.set_option('display.max.columns', None)  # show all cols not elipse
# if not on, prints top 5 and last 5 rows.
pd.set_option('display.max_rows', 100)
pd.set_option('display.width', None)  # do not wrap columns with a \
pd.set_option('display.precision', 2)  # set decimal places to 2


DL_URL = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv'

resp = requests.get(DL_URL)

print(resp.status_code)

with open('nba_all_elo.csv', 'wb') as f:
    f.write(resp.content)

nba = pd.read_csv('nba_all_elo.csv')

print(nba.info())

