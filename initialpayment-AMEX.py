#!/usr/bin/python
import urllib, urllib2, json

def initialPayment():
	url = "https://test.oppwa.com/v1/payments"
	data = {
		'authentication.userId' : '8a8294174b7ecb28014b9699220015cc',
		'authentication.password' : 'sy6KJsT8',
		'authentication.entityId' : '8a8294174b7ecb28014b9699220015ca',
		'amount' : '92.00',
		'currency' : 'EUR',
		'paymentBrand' : 'AMEX',
		'paymentType' : 'PA',
		'card.number' : '377777777777770',
		'card.holder' : 'Jane Jones',
		'card.expiryMonth' : '05',
		'card.expiryYear' : '2018',
		'card.cvv' : '1234'
	}
	try:
		opener = urllib2.build_opener(urllib2.HTTPHandler)
		request = urllib2.Request(url, data=urllib.urlencode(data))
		request.get_method = lambda: 'POST'
		response = opener.open(request)
		return json.loads(response.read());
	except urllib2.HTTPError, e:
		return e.code;

responseData = initialPayment();
print responseData;
