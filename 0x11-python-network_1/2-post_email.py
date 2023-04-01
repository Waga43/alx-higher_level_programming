#!/usr/bin/python3
"""Python script:
- takes in a URL
- sends a POST request to the passed URL with email as a parameter
- displays the body of the response (decoded in utf-8)
"""
from sys import argv
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = argv[1]
    data = {"email": argv[2]}
    data = urllib.parse.urlencode(data).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
