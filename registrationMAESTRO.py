#!/usr/bin/python

import urllib, urllib2, json

def registration():
	url = "https://test.oppwa.com/v1/registrations"
	data = {
		"authentication.userId": "8a8294174b7ecb28014b9699220015cc",
		"authentication.password": "sy6KJsT8",
		"authentication.entityId": "8a8294174b7ecb28014b9699a3cf15d1",
		'paymentBrand' : 'MAESTRO',
		'card.number' : '6799851000000032',
		'card.holder' : 'Jane Jones',
		'card.expiryMonth' : '05',
		'card.expiryYear' : '2018',
		'card.cvv' : '123'
	}
	try:
		response = urllib2.urlopen(url, urllib.urlencode(data))
		return json.loads(response.read());
	except urllib2.HTTPError, e:
		return e.code;

responseData = registration();
print responseData;