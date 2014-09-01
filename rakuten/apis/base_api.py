import re
import json
import requests
from .api_exception import RakutenApiException

class BaseApi:
    def __init__(self, options):
        self._options = options
        self._base_url = self._options['api_endpoint']
        if self._base_url.endswith('/'):
            self._base_url = self._base_url[:-1]
        self._default_params = {
            'applicationId': self._options['app_id'],
            'format': 'json',
        }

    def _make_url(self, path):
        if not path.startswith('/'):
            path = path + '/'
        return self._base_url + path

    def _dict_to_camel_case(self, old_params):
        params = {}
        for (key, value) in old_params.items():
            params[self._to_camel_case(key)] = value
        return params

    def _to_camel_case(self, name):
        splitted = name.split('_')
        return splitted[0] + ''.join(map(lambda x: x.capitalize(), splitted[1:]))

    def _request(self, path, params, parser=None, method='get', payload=None):
        params = self._dict_to_camel_case(params)
        params.update(self._default_params)
        url = self._make_url(path)
        headers = {'content-type': 'application/json'}
        args = {'params': params, 'headers': headers}
        if payload is not None:
            args['data'] = json.dumps(payload)
        r = getattr(requests, method)(url, **args)
        if r.status_code == 200:
            result = r.json()
            if parser is not None:
                result = parser(result)
            return result
        else:
            raise RakutenApiException(r.status_code, r.text)
