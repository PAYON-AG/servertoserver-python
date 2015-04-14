#!/usr/bin/python

import urllib, urllib2, json

def initialPayment():
	url = "https://test.oppwa.com/v1/payments"
	data = {
		'authentication.userId' : '8a8294174b7ecb28014b9699220015cc',
		'authentication.password' : 'sy6KJsT8',
		'authentication.entityId' : '8a8294174b7ecb28014b9699a3cf15d1',
		'amount' : '1.03',
		'currency' : 'BRL',
		'paymentBrand' : 'BRADESCO',
		'paymentType' : 'PA',
		'customer.givenName' : 'Braziliano',
		'customer.surname' : 'Babtiste',
		'billing.city' : 'Brasilia',
		'billing.country' : 'BR',
		'billing.state' : 'DE',
		'billing.street1' : 'Amazonstda',
		'billing.postcode' : '12345678',
		'customParameters[BRADESCO_cpfsacado]' : '11111111111',
		'shopperResultUrl' : 'https://docs.oppwa.com',
		'testMode' : 'EXTERNAL'
	}
	try:
		responseData = urllib2.urlopen(url, urllib.urlencode(data))
		return json.loads(responseData.read());
	except urllib2.HTTPError, e:
		return e.code;

responseData = initialPayment();
print responseData;