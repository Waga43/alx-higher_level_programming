#!/usr/bin/python3
"""This python script:
- fetches "https://alx-intranet.hbtn.io/status"
- uses the urlib package and the Python with statement
"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        body = response.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        decoded_body = body.decode("utf-8")
        print(f"\t- utf8 content: {decoded_body}")
