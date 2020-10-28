import plotly.graph_objects as go
import pandas as pd
from datetime import datetime

Filename = 'BTC1h2020.csv'

if __name__ ==  '__main__':
    df = pd.read_csv(Filename)

#change timestamp(MTS) to UTC-Time, drop unnecessary columns
df.insert(loc=0, column='Date', value=pd.to_datetime(df["MTS"], unit='ms'))
df = df.drop(['MTS', 'Unnamed: 0'], axis=1)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['OPEN'],
                high=df['HIGH'],
                low=df['LOW'],
                close=df['CLOSE'])])

fig.show()
