# update at 8 Oct 17
# get the pulblic IP address

import requests


response = requests.get('https://httpbin.org/ip')
print('Your IP is {0}'.format(response.json()['origin']))

