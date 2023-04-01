#!/usr/bin/python3
"""
Python script fetches a URL using the requests package
"""
import requests

if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    txt = response.text
    print("Body response:")
    print(f"\t- type: {type(txt)}")
    print(f"\t- content: {txt}")
