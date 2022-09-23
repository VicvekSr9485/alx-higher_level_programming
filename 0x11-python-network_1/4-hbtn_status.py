#!/usr/bin/python3
"""
Python script that fetches an URL with requests package
"""
import requests


if __name__ == "__main__":
    req = requests.get('https://intranet.hbtn.io/status')
    res = req.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(res), res))
