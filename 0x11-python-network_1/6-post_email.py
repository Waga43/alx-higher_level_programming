#!/usr/bin/python3
"""Python script:
- takes in a URL and an email address,
- sends a POST request to the passed URL with the email as a parameter
- displays the body of the reponse
"""
import requests
from sys import argv


if __name__ == "__main__":
    email_payload = {'email': argv[2]}
    response = requests.post(argv[1], data = email_payload)
    print(response.text)
