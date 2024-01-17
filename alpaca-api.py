from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass

from alpaca.trading.client import TradingClient
from alpaca.trading.enums import OrderSide, TimeInForce

from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoLatestQuoteRequest

from keys import paper_apikey, paper_secretkey

def getAccountDetails():
    trading_client = TradingClient(paper_apikey, paper_secretkey)
    account = trading_client.get_account()
    return account

def getAssets():
    trading_client = TradingClient(paper_apikey, paper_secretkey)
    search_params = GetAssetsRequest(asset_class=AssetClass.CRYPTO)
    assets = trading_client.get_all_assets(search_params)
    return assets  

def marketOrderData(symbol, qty, side):
    trading_client = TradingClient(paper_apikey, paper_secretkey)
    order = trading_client.submit_order(
        symbol=symbol,
        qty=qty,
        side=side,
        type='market',
        time_in_force=TimeInForce.DAY
    )
    return order

def limitOrderData(symbol, qty, side, limit_price):
    trading_client = TradingClient(paper_apikey, paper_secretkey)
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
    trading_client = TradingClient(paper_apikey, paper_secretkey)
    orders = trading_client.get_orders()
    return orders

def getOpenBuyOrders():
    trading_client = TradingClient(paper_apikey, paper_secretkey)
    orders = trading_client.get_orders(status='open', direction='desc', limit=100, nested=True)
    return orders

def getOpenSellOrders():
    trading_client = TradingClient(paper_apikey, paper_secretkey)
    orders = trading_client.get_orders(status='open', direction='asc', limit=100, nested=True)
    return orders

def cancelAllOrders():
    trading_client = TradingClient(paper_apikey, paper_secretkey)
    orders = trading_client.cancel_orders()
    return orders

def getAllPositions():
    trading_client = TradingClient(paper_apikey, paper_secretkey)
    positions = trading_client.get_all_positions()
    return positions 

def closeAllPositionsAndOrders():
    trading_client = TradingClient(paper_apikey, paper_secretkey)
    positions = trading_client.close_all_positions(cancel_orders=True)
    return positions



def getLatestCryptoQuote(symbol):
    client = CryptoHistoricalDataClient()
    request_params = CryptoLatestQuoteRequest(symbol_or_symbols=symbol)
    latest_quote = client.get_crypto_latest_quote(request_params)
    return latest_quote

import time

while True:
    q = getLatestCryptoQuote('BTC/USD')['BTC/USD']
    print(q.ask_price, q.bid_price)
    time.sleep(5)
    