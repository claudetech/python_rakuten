import re

class BaseApi:
    def __init__(self, options):
        self._options = options
        self._base_url = self._options['api_endpoint']
        if self._base_url.endswith('/'):
            self._base_url = self._base_url[:-1]

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
