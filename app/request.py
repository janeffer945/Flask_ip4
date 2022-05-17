# import requests,json

from flask import request_finished


def get_quotes():
    response = request_finished.get('http://quotes.stormconsultancy.co.uk/random.json')
    if response.status_code == 200:
        quote = response.json()
        # print(quote)
        return quote
