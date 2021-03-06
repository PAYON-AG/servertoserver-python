#!/usr/bin/python

import urllib, urllib2, json

def initialPayment():
	url = "https://test.oppwa.com/v1/payments"
	data = {
		"authentication.userId": "8a8294174b7ecb28014b9699220015cc",
		"authentication.password": "sy6KJsT8",
		"authentication.entityId": "8a8294174b7ecb28014b9699a3cf15d1",
		'amount' : '92.00',
		'currency' : 'EUR',
		'paymentBrand' : 'VISA',
		'paymentType' : 'PA',
		'card.number' : '4200000000000000',
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

responseData = initialPayment();
print responseData;