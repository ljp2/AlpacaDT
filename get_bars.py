import pandas as pd

from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
from datetime import datetime, timedelta
from time import sleep
import pytz

def getHistoricalCryptoBar(ticker:str, startdatetime:datetime, enddatetime:datetime, timeframe:TimeFrame=TimeFrame.Minute) -> pd.DataFrame:
    ticker = ticker
    client = CryptoHistoricalDataClient()
    # apikey = 'PKKJZYB9P6Q36H84YMXF'
    # secretkey = 'hBnEAEiD1f67p6hM4DKkUBtixY01YulNWSuGHOyx'
    # client = StockHistoricalDataClient(apikey, secretkey)
    request_params = CryptoBarsRequest(
        symbol_or_symbols=[ticker],
        timeframe=timeframe,
        start=startdatetime,
        end=enddatetime
    )
    btc_bars = client.get_crypto_bars(request_params, feed='us')
    df = btc_bars.df.loc[ticker]
    df.columns = [s.capitalize() for s in df.columns]
    df = df.rename_axis('Datetime')
    return df[['Open', 'High', 'Low', 'Close']]

def getMultipleHistoricalCryptoBars(start_day:datetime, num_days_backward:int, timeframe:TimeFrame=TimeFrame.Minute):
    for i in range(num_days_backward):
        end_day = start_day + timedelta(days=1)
        filename ='.'.join([start_day.strftime('%Y%m%d'), 'csv'])
        df = getHistoricalCryptoBar('BTC/USD', start_day, end_day)
        df.to_csv(filename)
        start_day -= timedelta(days=1)
        print(start_day.strftime('%b %d, %Y')) #, len(df))
        sleep(1)

def datetimeAwareEastern(year, month, day, hour=0, minute=0, sec=0):
    us_eastern = pytz.timezone('US/Eastern')
    t = datetime(year, month, day, hour, minute, sec)
    t = us_eastern.localize(t)
    return t

