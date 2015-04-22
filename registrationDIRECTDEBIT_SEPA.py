#!/usr/bin/python

import urllib, urllib2, json

def registration():
	url = "https://test.oppwa.com/v1/registrations"
	data = {
		"authentication.userId": "8a8294174b7ecb28014b9699220015cc",
		"authentication.password": "sy6KJsT8",
		"authentication.entityId": "8a8294174b7ecb28014b9699a3cf15d1",
		'paymentBrand' : 'DIRECTDEBIT_SEPA',
		'bankAccount.bic' : 'MARKDEF1100',
		'bankAccount.iban' : 'DE23100000001234567890',
		'bankAccount.country' : 'DE',
		'bankAccount.holder' : 'Jane Jones'
	}
	try:
		response = urllib2.urlopen(url, urllib.urlencode(data))
		return json.loads(response.read());
	except urllib2.HTTPError, e:
		return e.code;

responseData = registration();
print responseData;