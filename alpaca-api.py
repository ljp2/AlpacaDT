from keys import paper_apikey, paper_secretkey
import pandas as pd
from datetime import datetime

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass

from alpaca.trading.client import TradingClient
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest, CryptoLatestQuoteRequest

apikey = paper_apikey
secretkey = paper_secretkey

def getAccountDetails():
    trading_client = TradingClient(apikey, secretkey)
    account = trading_client.get_account()
    return account

def getAssets():
    trading_client = TradingClient(apikey, secretkey)
    search_params = GetAssetsRequest(asset_class=AssetClass.CRYPTO)
    assets = trading_client.get_all_assets(search_params)
    return assets  

def marketOrderData(symbol, qty, side):
    trading_client = TradingClient(apikey, secretkey)
    order = trading_client.submit_order(
        symbol=symbol,
        qty=qty,
        side=side,
        type='market',
        time_in_force=TimeInForce.DAY
    )
    return order

def limitOrderData(symbol, qty, side, limit_price):
    trading_client = TradingClient(apikey, secretkey)
    order = trading_client.submit_order(
        symbol=symbol,
        qty=qty,
        side=side,
        type='limit',
        time_in_force=TimeInForce.DAY,
        limit_price=limit_price
    )
    return order


def submitMarketBuyOrder(symbol, qty):
    order = marketOrderData(symbol, qty, OrderSide.BUY)
    return order

def submitMarketSellOrder(symbol, qty):
    order = marketOrderData(symbol, qty, OrderSide.SELL)
    return order

def submitLimitBuyOrder(symbol, qty, limit_price):
    order = limitOrderData(symbol, qty, OrderSide.BUY, limit_price)
    return order

def submitLimitSellOrder(symbol, qty, limit_price):
    order = limitOrderData(symbol, qty, OrderSide.SELL, limit_price)
    return order

def getAllOpenOrders():
    trading_client = TradingClient(apikey, secretkey)
    orders = trading_client.get_orders()
    return orders

def getOpenBuyOrders():
    trading_client = TradingClient(apikey, secretkey)
    orders = trading_client.get_orders(status='open', direction='desc', limit=100, nested=True)
    return orders

def getOpenSellOrders():
    trading_client = TradingClient(apikey, secretkey)
    orders = trading_client.get_orders(status='open', direction='asc', limit=100, nested=True)
    return orders

def cancelAllOrders():
    trading_client = TradingClient(apikey, secretkey)
    orders = trading_client.cancel_orders()
    return orders

def getAllPositions():
    trading_client = TradingClient(apikey, secretkey)
    positions = trading_client.get_all_positions()
    return positions 

def closeAllPositionsAndOrders():
    trading_client = TradingClient(apikey, secretkey)
    positions = trading_client.close_all_positions(cancel_orders=True)
    return positions

def getHistoricalCryptoData(symbol, timeframe, start_date, end_date) ->pd.DataFrame:
    client = CryptoHistoricalDataClient(apikey, secretkey)
    request_params = CryptoBarsRequest(
        symbol_or_symbols=symbol,
        timeframe=timeframe,
        start=start_date,
        end=end_date
    )
    historical_data = client.get_crypto_bars(request_params)
    df = historical_data.df.loc[symbol]
    df.columns = [s.capitalize() for s in df.columns]
    return df[['Open', 'High', 'Low', 'Close']] 

def getLatestCryptoQuote(symbol):
    client = CryptoHistoricalDataClient(apikey, secretkey)
    request_params = CryptoLatestQuoteRequest(symbol_or_symbols=symbol)
    latest_quote = client.get_crypto_latest_quote(request_params)
    return latest_quote

# import time

# while True:
#     q = getLatestCryptoQuote('BTC/USD')['BTC/USD']
#     print(q.ask_price, q.bid_price)
#     time.sleep(5



# from datetime import datetime, timedelta
# import pytz

# new_york_tz = pytz.timezone('America/New_York')
# ny_time = datetime.now(new_york_tz).replace(hour=9, minute=30, second=0, microsecond=0)
    
# df = getHistoricalCryptoData(
#     symbol='BTC/USD',
#     timeframe=TimeFrame(1, TimeFrameUnit.Minute),
#     start_date=ny_time,
#     end_date=ny_time + timedelta(minutes=30)
# )

# print(df.head())
# print(df.tail())
    