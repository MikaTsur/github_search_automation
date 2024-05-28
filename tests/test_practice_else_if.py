from playwright.sync_api import sync_playwright
import pytest
import requests
from bs4 import BeautifulSoup
import logging
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def test_if_num():
    somevar = 10
    if isinstance(somevar, bool):
        logging.info('bool')
    elif isinstance(somevar, str):
        logging.info('str')
    elif isinstance(somevar, (int, float)):
        logging.info('aaaaaaaaaaaa-num')
    else:
        logging.info('unknown type')

def test_if_a():
    a = 20
    if (a>30):
        logging.info('a>30')
    elif(a>20):
        logging.info('a>30')
    else:
        logging.info('kkkkkkkkkkkkkkkkkkkkkkkkk')






def test_if_else():
    morell = {
        'yonatan': 'father',
        'mika': 'mother',
        'children': {
            'hodaya': '7',
            'Iscah': 5,
            'Hanoch': '1'
        }
    }
    hodaya_age = int(morell['children']['hodaya'])
    Iscah_age = str(morell['children']['Iscah'])

    if Iscah_age == '1':
        logging.info("Iscah_age set to 1")
    elif Iscah_age == '4':
        logging.info("Iscah_age set to 5")
    else:
        logging.info("None")


def test_lang():
    langs = ["Python"]
    for lang in langs:
        match lang:
            case "JavaScript":
                print(f"{lang}: You can become a web developer.")

            case "Python":
                print(f"{lang}: You can become a Data Scientist")

            case "PHP":
                print(f"{lang}: You can become a backend developer")

            case "Solidity":
                print(f"{lang}: You can become a Blockchain developer")

            case "Java":
                print(f"{lang}: You can become a mobile app developer")

            case _:
                print(f"{lang}: The language doesn't matter, what matters is solving problems.")

# Test the function
test_lang()



