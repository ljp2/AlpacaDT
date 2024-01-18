from keys import paper_apikey, paper_secretkey
import pandas as pd
from datetime import datetime, timedelta
import pytz

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
        symbol=symbol, qty=qty, side=side, type="market", time_in_force=TimeInForce.DAY
    )
    return order


def limitOrderData(symbol, qty, side, limit_price):
    trading_client = TradingClient(apikey, secretkey)
    order = trading_client.submit_order(
        symbol=symbol,
        qty=qty,
        side=side,
        type="limit",
        time_in_force=TimeInForce.DAY,
        limit_price=limit_price,
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
    orders = trading_client.get_orders(
        status="open", direction="desc", limit=100, nested=True
    )
    return orders


def getOpenSellOrders():
    trading_client = TradingClient(apikey, secretkey)
    orders = trading_client.get_orders(
        status="open", direction="asc", limit=100, nested=True
    )
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


def getLatestCryptoQuote(symbol):
    client = CryptoHistoricalDataClient(apikey, secretkey)
    request_params = CryptoLatestQuoteRequest(symbol_or_symbols=symbol)
    latest_quote = client.get_crypto_latest_quote(request_params)
    return latest_quote


def getHistoricalCryptoData(symbol, timeframe, start, end) -> pd.DataFrame:
    client = CryptoHistoricalDataClient(apikey, secretkey)
    request_params = CryptoBarsRequest(
        symbol_or_symbols=symbol, timeframe=timeframe, start=start, end=end
    )
    historical_data = client.get_crypto_bars(request_params)
    df = historical_data.df.loc[symbol]
    df.columns = [s.capitalize() for s in df.columns]
    sdf = df[["Open", "High", "Low", "Close"]]
    return sdf


def getLatestBar(symbol: str, bar_minutes: int):
    end_time = datetime.utcnow()
    start_time = end_time - 2 * timedelta(minutes=bar_minutes)
    try:
        minute_df = getHistoricalCryptoData(
            symbol=symbol, timeframe=TimeFrame.Minute, start=start_time, end=end_time
        )
    except:
        minute_df = None
    if minute_df is not None:
        minute_bars = minute_df.iloc[-bar_minutes:]
        Open = minute_bars.iloc[0]["Open"]
        Close = minute_bars.iloc[-1]["Close"]
        High = minute_bars["High"].max()
        Low = minute_bars["Low"].min()
        index = minute_bars.index[0]
        df = pd.DataFrame(
            {"Open": [Open], "High": [High], "Low": [Low], "Close": [Close]},
            index=[index],
        )
    return df


if __name__ == "__main__":
    from utils import toNewYorkTime, HHMM, dayHHMM

    tnow_ny = datetime.now(pytz.timezone("America/New_York"))
    print(tnow_ny.strftime("%Y-%m-%d %H:%M"))

    utc_now = datetime.utcnow()
    print(dayHHMM(utc_now))

    for n in [1, 5, 10, 15]:
        print(n, "--------------")
        try:
            df = getLatestBar("BTC/USD", n)
            print(df)
        except:
            print("None returned")
        print("")
