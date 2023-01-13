import pandas as pd
import requests
from pandas.io.json import json_normalize

params = (
    ('league_id', '7'),
    ('per_page', '250'),
    ('projection_type_id', '1'),
    ('single_stat', 'true'),
)

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"

}
session = requests.Session()
response = session.get('https://api.prizepicks.com/projections', data=params, headers=headers)
print(response.status_code)

df1 = json_normalize(response.json()['included'])
df1 = df1[df1['type'] == 'new_player']

df2 = json_normalize(response.json()['data'])

df = pd.DataFrame(zip(df1['attributes.name'], df2['attributes.line_score']), columns=['name', 'points'])
print(df)