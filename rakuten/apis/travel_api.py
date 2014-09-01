from .base_api import BaseApi


class TravelApi(BaseApi):
    def __init__(self, options):
        super(TravelApi, self).__init__(options)
        self._default_params['datumType'] = 1

    def simple_hotel_search(self, **kwargs):
        return self._request(
            '/Travel/SimpleHotelSearch/20131024',
            kwargs,
            self._parse_hotels_result
        )

    def vacant_hotel_search(self, **kwargs):
        return self._request(
            '/Travel/VacantHotelSearch/20131024',
            kwargs,
            self._parse_hotels_result
        )

    def hotel_detail_search(self, **kwargs):
        return self._request(
            '/Travel/HotelDetailSearch/20131024',
            kwargs,
            self._parse_hotels_result
        )

    def get_area_class(self, **kwargs):
        return self._request(
            '/Travel/GetAreaClass/20131024',
            kwargs,
            self._parse_areas
        )

    def keyword_hotel_search(self, keyword, **kwargs):
        kwargs['keyword'] = keyword
        return self._request(
            '/Travel/KeywordHotelSearch/20131024',
            kwargs,
            self._parse_hotels_result
        )

    def get_hotel_chain_list(self, **kwargs):
        return self._request(
            '/Travel/GetHotelChainList/20131024',
            kwargs,
            self._parse_hotel_chain
        )

    def _parse_hotel_chain(self, result):
        chains = []
        for chainInfo in result['largeClasses'][0]['largeClass']:
            new_chains = [r['hotelChain'] for r in chainInfo['hotelChains']]
            chains.append({'largeClass': chainInfo['largeClassCode'], 'chains': new_chains})
        return chains

    def _parse_areas(self, result):
        final_res = result['areaClasses']['largeClasses'][0]['largeClass'][0]
        final_res['middle_classes'] = []
        middle_classes = result['areaClasses']['largeClasses'][0]['largeClass'][1]['middleClasses']
        for m in middle_classes:
            cl = m['middleClass'][0]
            cl['small_classes'] = []
            sub_classes = m['middleClass'][1]['smallClasses']
            for s in sub_classes:
                d = s['smallClass'][0]
                if len(s['smallClass']) > 1:
                    d['detail_classes'] = s['smallClass'][1]
                else:
                    d['detail_classes'] = []
                cl['small_classes'].append(d)
            final_res['middle_classes'].append(cl)
        return final_res

        r = result['areaClasses']['largeClasses'][0]['largeClass'][1]

    def _parse_hotels_result(self, result):
        return [self._parse_hotel(r) for r in result['hotels']]

    def _parse_hotel(self, hotel_info):
        hotel = hotel_info['hotel'][0]['hotelBasicInfo']
        room_info = [r['roomInfo'][0]['roomBasicInfo'] for r in hotel_info['hotel'] if 'roomInfo' in r]
        rating_info = [r['hotelRatingInfo'] for r in hotel_info['hotel'] if 'hotelRatingInfo' in r]
        hotel['room_info'] = room_info
        hotel['rating_info'] = rating_info
        return hotel
