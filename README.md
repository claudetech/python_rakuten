## python_rakuten_api

Python API for Rakuten API.

## Usage

Create a client.

```
from rakuten import RakutenClient
client = RakutenClient("API_KEY")
```

### Travel API

Available methods:

* `simple_hotel_search`

```
response = client.travel.simple_hotel_search(
  middle_class_code="akita",
  large_class_code="japan",
  small_class_code="tazawa"
)
```

* `vacant_hotel_search`

```
response = client.travel.vacant_hotel_search(
  checkin_date="2014-10-01",
  checkout_date="2014-10-01",
  middle_class_code="akita",
  large_class_code="japan",
  small_class_code="tazawa"
)
```

* `get_area_class`

```
response = client.travel.vacant_hotel_search()
```

* `keyword_hotel_search`

```
response = client.travel.keyword_hotel_search('keyword')
```

* `get_hotel_chain_list`

```
response = client.travel.get_hotel_chain_list()
```
