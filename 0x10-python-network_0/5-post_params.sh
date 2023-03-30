#!/bin/bash
# Sends a POST request to a URL, and displays the body of the response
curl "$1" -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"

