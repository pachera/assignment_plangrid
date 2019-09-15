#/usr/bin/env python3

# importing the requests library

from django.test import Client
from time import sleep

import requests
import json
import sys

from django.test import RequestFactory

#url = 'http://127.0.0.1:8000'
url = 'http://' + sys.argv[-1]

try:
    response = requests.get(url)
except:
    print('Your web app is not responding...')

else:
    if response.status_code == 200:
        if response.text.strip() == "<p>Hello, World!</p>":
            print("HTML pass {}".format(response.text.strip()))
        else:
            print("{} - Unexpected HTML".format(response.text.strip()))
            sys.exit(1)

    else:
        print('An Error Occurred...')
        sys.exit(1)

    response_json = requests.get(url, headers={'Accept': 'application/json'})

    #print(response_json.text)

    try:
        json.loads(response_json.text)

    except:
        print("Fail. {} is not a JSON".format(response_json.text))
        sys.exit(1)

    else:
        if json.loads(response_json.text)['message'] == 'Hello, World!':
            print("JSON pass {}".format(json.loads(response_json.text)))
        else:
            print("{} - Unexpected JSON".format(response_json.text))
            sys.exit(1)
