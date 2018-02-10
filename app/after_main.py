import requests
from typing import Optional
from typing import Union
from requests.models import Response
from typing import Any
from typing import Dict


def add(a, b):
    # type: (int, int) -> int
    return a + b


def str_or_none(c):
    # type: (Union[int, str]) -> Optional[str]
    return c if isinstance(c, str) else None


def call_address_api(zipcode):
    # type: (str) -> Response
    return requests.get(f'http://api.zipaddress.net/?zipcode={zipcode}')


def parse_response_json(response):
    # type: (Response) -> Dict[str, Any]
    return response.json()
