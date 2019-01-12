#!/usr/bin/env python
import requests


print(requests.__version__)


r = requests.get("http://www.google.com")
print(r)

print(dir(r))
r = requests.get("https://raw.githubusercontent.com/lily06/CMPUT404lab1H05/master/main.py")

print(r.text)
# print(r.status_code)

