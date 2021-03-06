import requests


def add(a, b):
    return a + b


def str_or_none(c):
    return c if isinstance(c, str) else None


def call_address_api(zipcode):
    return requests.get(f'http://api.zipaddress.net/?zipcode={zipcode}')


def parse_response_json(response):
    return response.json()


class Hoge:
    def __init__(self):
        pass

    def sub(self, d, e):
        return d - e


def create_hoge_instance():
    return Hoge()
