import urllib.request
with urllib.request.urlopen('http://www.python.org/') as f:
	print(f.read(100).decode('utf-8'))

import urllib.request
with urllib.request.Request('http://python.org/') as req:
	response = urllib.request.urlopen(req)
	print(response.read())

import urllib.request
import urllib.parse
params = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
url = "http://www.musi-cal.com/cgi-bin/query?%s" % params
with urllib.request.urlopen(url) as f:
	print(f.read().decode('utf-8'))

import urllib.request
import urllib.parse
data = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
data = data.encode('ascii')
with urllib.request.urlopen("http://requestb.in/xrbl82xr", data) as f:
	print(f.read().decode('utf-8'))

import requests
with requests.get('http://www.python.org/') as r:
	print(r.headers,'\n',r.status_code,'\n',r.headers['content-type'])

import urllib3
http = urllib3.PoolManager()
with http.request('GET', 'http://httpbin.org/robots.txt') as r:
	print(r.status,'\n',r.data.decode('utf-8'))