#!/usr/bin/python

import urllib, urllib2, json

def initialPayments():
	url = "https://test.oppwa.com/v1/payments"
	data = {
		'authentication.userId' : '8a8294174b7ecb28014b9699220015cc',
		'authentication.password' : 'sy6KJsT8',
		'authentication.entityId' : '8a8294184c0378fe014c046e80340da9',
		'amount' : '92.12',
		'currency' : 'EUR',
		'paymentBrand' : 'GIROPAY',
		'paymentType' : 'PA',
		'bankAccount.bic' : 'TESTDETT421',
		'bankAccount.iban' : 'DE14940593100000012346',
		'bankAccount.country' : 'DE',
		'shopperResultUrl' : 'https://docs.oppwa.com'
	}
	try:
		response = urllib2.urlopen(url, urllib.urlencode(data))
		return json.loads(response.read());
	except urllib2.HTTPError, e:
		return e.code;

responseData= initialPayments();
print responseData;