from requests.models import Response

from app.main import add, str_or_none, call_address_api, parse_response_json


def test_add():
    assert add(1, 2) == 3


def test_str_or_none_str():
    assert isinstance(str_or_none('str'), str)


def test_str_or_none_none():
    assert str_or_none(1) is None


def test_call_address_api():
    assert isinstance(call_address_api('1600022'), Response)


def test_parse_response_json():
    address_api_response = call_address_api('1600022')
    assert isinstance(parse_response_json(address_api_response), dict)
