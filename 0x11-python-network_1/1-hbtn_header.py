#!/usr/bin/python3
"""Python script:
- takes in a URL,
- sends a request to the URL and displays the value of the X-Request-Id
"""
from sys import argv

import urllib.request

if __name__ == "__main__":
    url = argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(response.headers.get('X-Request-Id'))
