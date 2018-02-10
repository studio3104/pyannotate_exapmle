from typing import Any, Dict, Optional, Union

import requests
from requests.models import Response


def add(a: int, b: int) -> int:
    return a + b


def str_or_none(c: Union[int, str]) -> Optional[str]:
    return c if isinstance(c, str) else None


def call_address_api(zipcode: str) -> Response:
    return requests.get(f'http://api.zipaddress.net/?zipcode={zipcode}')


def parse_response_json(response: Response) -> Dict[str, Any]:
    return response.json()
