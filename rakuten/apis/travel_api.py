from .api_exception import RakutenApiException
from .base_api import BaseApi

class TravelApi(BaseApi):
    def __init__(self, options):
        super(TravelApi, self).__init__(options)
        self._default_params['datumType'] = 1

    def vacant_hotel_search(self, **kwargs):
        return self._request(
            '/Travel/VacantHotelSearch/20131024',
            kwargs,
            self._parse_hotels_result
        )

    def _parse_hotels_result(self, result):
        return [self._parse_hotel(r) for r in result['hotels']]

    def _parse_hotel(self, hotel_info):
        hotel = hotel_info['hotel'][0]['hotelBasicInfo']
        room_infos = [r['roomInfo'][0]['roomBasicInfo'] for r in hotel_info['hotel'] if 'roomInfo' in r]
        hotel['room_infos'] = room_infos
        return hotel
