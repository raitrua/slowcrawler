import urllib.request
import json

url = 'https://home.komatsu/'

try:
    with urllib.request.urlopen(url) as response:
        body = response.read()
        headers = response.getheaders()
        status = response.getcode()

        print(headers)
        print(status)
        print(body)

except urllib.error.URLError as e:
     print(e.reason)