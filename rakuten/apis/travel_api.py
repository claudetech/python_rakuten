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
            hotels = [self._parse_hotel(r) for r in result['hotels']]
            return hotels
        else:
            raise RakutenApiException(r.status_code, r.text)

    def _parse_hotel(self, hotel_info):
        hotel = hotel_info['hotel'][0]['hotelBasicInfo']
        room_infos = [r['roomInfo'][0]['roomBasicInfo'] for r in hotel_info['hotel'] if 'roomInfo' in r]
        hotel['room_infos'] = room_infos
        return hotel
