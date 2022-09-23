#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status """
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        stat = response.read()
        print('Body response:', end='$\n')
        print('\t- type: {}'.format(type(stat)), end='$\n')
        print('\t- content: {}'.format(stat), end='$\n')
        print('\t- utf8 content: {}'.format(stat.decode("utf-8")), end='$\n')
