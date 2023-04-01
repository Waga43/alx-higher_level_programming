#!/usr/bin/python3
"""Python script:
- takes in a URL
- sends a request to the URL
- displays the body of the response.
- if the HTTP status code is >= 400, it prints:-
- "Error code:" followed by the value of the HTTP status code
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
