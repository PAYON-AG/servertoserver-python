#!/usr/bin/python

import urllib, urllib2, json

def backofficeOperation():
	url = "https://test.oppwa.com/v1/payments/8a82944a4cdca5cc014ce06c9216480a"
	data = {
		'authentication.userId' : '8a8294174b7ecb28014b9699220015cc',
		'authentication.password' : 'sy6KJsT8',
		'authentication.entityId' : '8a8294174b7ecb28014b9699a3cf15d1',
		'amount' : '10.00',
		'currency' : 'EUR',
		'paymentType' : 'RF'
	}
	try:
		response = urllib2.urlopen(url, urllib.urlencode(data))
		return json.loads(response.read());
	except urllib2.HTTPError, e:
		return e.code;

responseData = backofficeOperation();
print responseData;