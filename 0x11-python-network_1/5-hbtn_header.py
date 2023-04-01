#!/usr/bin/python3
"""Python script:
- takes in a URL,
- sends a request to the URL,
- displays the value of the variable X-Request-Id in the response header
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]

    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))
