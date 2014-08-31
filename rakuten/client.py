import http

from .apis import TravelApi

class RakutenClient:
    def __init__(self, app_id, **kwargs):
        self._options = {
           'api_endpoint': 'https://app.rakuten.co.jp/services/api',
           'app_id': app_id,
        }
        if self._options is not None:
            self._options.update(kwargs)

        self.travel = TravelApi(self._options)
