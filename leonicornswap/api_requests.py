from typing import Tuple
import requests
import json

LeonicornSwap_url = """https://api.leonicornswap.com/api/tokens"""
LEON = """0x27E873bee690C8E161813DE3566E9E18a64b0381"""
LEOS = """0x2c8368f8F474Ed9aF49b87eAc77061BEb986c2f1"""


def get_data(url: str) -> str:
    return requests.post(url).text

def parse_data(raw_json: str) -> dict:
    return json.loads(raw_json)

def get_price_pair() -> Tuple[int, int]:
    data = parse_data(get_data(LeonicornSwap_url))['data']
    LEON_price = data[LEON]['price']
    LEOS_price = data[LEOS]['price']
    return (LEON_price, LEOS_price)