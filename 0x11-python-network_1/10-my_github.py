#!/usr/bin/python3
"""Python script:
- takes your GitHub credentials (username & password/personal access token) and
- uses the GitHub API to display your id
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(argv[1], argv[2])
    response = requests.get("https://api.github.com/user", auth=auth)
    print(response.json().get("id"))
