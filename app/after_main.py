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


class Hoge:
    def __init__(self):
        # type: () -> None
        pass

    def sub(self, d, e):
        # type: (int, int) -> int
        return d - e


def create_hoge_instance():
    # type: () -> Hoge
    return Hoge()
