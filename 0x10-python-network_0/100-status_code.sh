#!/bin/bash
# Passed url as an argument and displays only the status code response
curl -s -o /dev/null -w "%{http_code}" "$1"
