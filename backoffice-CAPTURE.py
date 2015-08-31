#!/usr/bin/python
import urllib, urllib2, json

def request():
	url = "https://test.oppwa.com/v1/payments/8a8294494f72e836014f8391946d701b"
	data = {
		'authentication.userId' : '8a8294174b7ecb28014b9699220015cc',
		'authentication.entityId' : '8a8294174b7ecb28014b9699220015ca',
		'authentication.password' : 'sy6KJsT8',
		'amount' : '10.00',
		'currency' : 'EUR',
		'paymentType' : 'CP'
	}
	try:
		opener = urllib2.build_opener(urllib2.HTTPHandler)
		request = urllib2.Request(url, data=urllib.urlencode(data))
		request.get_method = lambda: 'POST'
		response = opener.open(request)
		return json.loads(response.read());
	except urllib2.HTTPError, e:
		return e.code;

responseData = request();
print responseData;
