import re
import http

from .apis import TravelApi


class RakutenClient:
    def __init__(self, application_id, application_secret=None, options=None):
        self.application_id = application_id
        self.application_secret = application_secret
        self.options = {
           'api_endpoint': 'https://app.rakuten.co.jp/services/api'
        }
        if options is not None:
            self.options.update(options)

        m = re.match("^(https?)://(.*?)/?$", self.options['api_endpoint'])
        if m is None:
            raise ValueError("Invalid endpoint {0}".format(self.options['api_endpoint']))
        if m.group(0) == 'http':
            self.client = http.client.HTTPConnection(m.group(1))
        else:
            self.client = http.client.HTTPSConnection(m.group(1))

        self.travel = TravelApi(self.client)
