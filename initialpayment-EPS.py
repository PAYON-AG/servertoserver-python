#!/usr/bin/python

import urllib, urllib2, json

def initialPayment():
	url = "https://test.oppwa.com/v1/payments"
	data = {
		'authentication.userId' : '8a8294174b7ecb28014b9699220015cc',
		'authentication.password' : 'sy6KJsT8',
		'authentication.entityId' : '8a8294184c0378fe014c046e80340da9',
		'amount' : '12.03',
		'currency' : 'EUR',
		'paymentBrand' : 'EPS',
		'paymentType' : 'PA',
		'bankAccount.country' : 'AT',
		'shopperResultUrl' : 'https://docs.oppwa.com'
	}
	try:
		response = urllib2.urlopen(url, urllib.urlencode(data))
		return json.loads(response.read());
	except urllib2.HTTPError, e:
		return e.code;

responseData = initialPayment();
print responseData;