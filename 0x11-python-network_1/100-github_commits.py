#!/usr/bin/python3
"""Python script:
- takes two arguments
- 1st argument: github repository name
- 2nd argument: github repository owner name
- and lists in descending order, the 10 most recent commits on the repository
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        argv[2], argv[1])

    response = requests.get(url)
    commits = response.json()
    try:
        for i in range(10):
            print(commits[i].get('sha'), end = ': ')
            print(commits[i].get('commit').get('author').get('name'))
    except IndexError:
        pass
