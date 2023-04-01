#!/usr/bin/python3
"""Python script:
- takes in a letter
- sends POST request to http://0.0.0.0:5000/search_user
- with the letter as a parameter.
"""
from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) == 2:
        letter = argv[1]
    else:
        letter = ""
    payload = {"q": letter}

    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
       json_ response = response.json()
        if json_response == {}:
            print("No result")
        else:
            print(f"[{json_response.get('id')}] {json_response.get('name')}")
    except ValueError:
        print("Not a valid JSON")
