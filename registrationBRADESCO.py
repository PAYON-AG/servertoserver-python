#!/usr/bin/python

import urllib, urllib2, json

def registration():
	url = "https://test.oppwa.com/v1/registrations"
	data = {
		"authentication.userId": "8a8294174b7ecb28014b9699220015cc",
		"authentication.password": "sy6KJsT8",
		"authentication.entityId": "8a8294174b7ecb28014b9699a3cf15d1",
		'paymentBrand' : 'BRADESCO',
		'customer.givenName' : 'Braziliano',
		'customer.surname' : 'Babtiste',
		'billing.city' : 'Brasilia',
		'billing.country' : 'BR',
		'billing.state' : 'SP',
		'billing.street1' : 'Amazonstda',
		'billing.postcode' : '12345678',
		'customParameters[BRADESCO_cpfsacado]' : '11111111111'
	}
	try:
		response = urllib2.urlopen(url, urllib.urlencode(data))
		return json.loads(response.read());
	except urllib2.HTTPError, e:
		return e.code;

responseData = registration();
print responseData;