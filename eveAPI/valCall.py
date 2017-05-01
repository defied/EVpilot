#!/bin/python
import httplib2 as http
import json

try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json; charset=UTF-8'
}

uri = 'https://vkpilot.live-valkyrieapi.com'
path = '/live/pilots/193295'

target = urlparse(uri+path)
method = 'GET'
body = '{"username": "problah@deadplanet.net","password": "4rgonSpr34d"}'

h = http.Http()

# If you need authentication some example:
#if auth:
#    h.add_credentials(auth.user, auth.password)
#
#response, content = h.request(
#        target.geturl(),
#        method,
#        body,
#        headers)
#
# assume that content is a json reply
# parse content with the json module
data = json.loads(content)
