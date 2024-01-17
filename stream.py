import sys
import keys

from alpaca.common.websocket import BaseStream
from typing import Optional, Dict
from alpaca.common.enums import BaseURL
from alpaca.data.enums import CryptoFeed
from alpaca.data.models import Quote, Trade

class CryptoDataStream(BaseStream):
    """
    A WebSocket client for streaming live crypto data.

    See BaseStream for more information on implementation and the methods available.
    """

    def __init__(
        self,
        api_key: str,
        secret_key: str,
        raw_data: bool = False,
        feed: CryptoFeed = 'us',
        url_override: Optional[str] = None,
        websocket_params: Optional[Dict] = None,
    ) -> None:
        """
        Instantiates a WebSocket client for accessing live cryptocurrency data.

        Args:
            api_key (str): Alpaca API key.
            secret_key (str): Alpaca API secret key.
            raw_data (bool, optional): Whether to return wrapped data or raw API data. Defaults to False.
            websocket_params (Optional[Dict], optional): Any parameters for configuring websocket connection. Defaults to None.
            url_override (Optional[str]): If specified allows you to override the base url the client
              points to for proxy/testing. Defaults to None.
        """
        super().__init__(
            endpoint=(
                url_override
                if url_override is not None
                else BaseURL.MARKET_DATA_STREAM.value + f"/v1beta3/crypto/{feed}"
            ),
            api_key=api_key,
            secret_key=secret_key,
            raw_data=raw_data,
            websocket_params=websocket_params,
        )




API_KEY = keys.paper_apikey
API_SECRET = keys.paper_secretkey

file_path = 'example.txt'
i = 0
stream = CryptoDataStream(
    api_key=API_KEY,
    secret_key=API_SECRET,
)
symbol = "BTC/USD"
async def handler(data):
    global i
    i += 1
    r = f"{str(type(data).__name__):5} {data}\n"
    print(r)
    if i > 100:
         sys.exit()
    with open(file_path, 'a') as file:
        file.write(r)

stream.subscribe_quotes(handler, symbol)
stream.subscribe_trades(handler, symbol)

stream.run()

# if isinstance(variable, Quote):
#     print("The variable is of type Quote")
# elif isinstance(variable, Trade):
#     print("The variable is of type Trade")
# else:
#     print("The variable is neither of type Quote nor Trade")