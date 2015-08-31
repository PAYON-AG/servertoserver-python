#!/usr/bin/python
import urllib, urllib2, json

def request():
	url = "https://test.oppwa.com/v1/payments/8a8294494f72e836014f83959a9e7177"
	url += '?authentication.userId=8a8294174b7ecb28014b9699220015cc'
	url += '&authentication.password=sy6KJsT8'
	url += '&authentication.entityId=8a8294174b7ecb28014b9699220015ca'
	try:
		opener = urllib2.build_opener(urllib2.HTTPHandler)
		request = urllib2.Request(url, data='')
		request.get_method = lambda: 'GET'
		response = opener.open(request)
		return json.loads(response.read());
	except urllib2.HTTPError, e:
		return e.code;

responseData = request();
print responseData;
