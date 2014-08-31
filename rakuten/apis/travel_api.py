import requests
from .api_exception import RakutenApiException
from .base_api import BaseApi

class TravelApi(BaseApi):
    def __init__(self, options):
        super(TravelApi, self).__init__(options)

    def vacant_hotel_search(self, **kwargs):
        params = self._dict_to_camel_case(kwargs)
        params.update(self._default_params)
        url = self._make_url('/Travel/VacantHotelSearch/20131024')
        r = requests.get(url, params=params)
        if r.status_code == 200:
            result = r.json()
            hotels = [r['hotel'] for r in result['hotels']]
            return hotels
        else:
            raise RakutenApiException(r.status_code, r.text)
