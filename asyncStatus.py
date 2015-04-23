#!/usr/bin/python

import urllib, urllib2, json

def getPaymentStatus(paymentId): 
	url = (
		"https://test.oppwa.com/v1/payments/" + paymentId +
		"?authentication.userId=8a8294174b7ecb28014b9699220015cc"
		"&authentication.password=sy6KJsT8" 
		"&authentication.entityId=8a8294174b7ecb28014b9699a3cf15d1")
	try:
		response = urllib2.urlopen(url)
		return json.loads(response.read());
	except urllib2.HTTPError, e:
		return e.code;

status = getPaymentStatus("8a8294494ce19bdf014ce509f20b13e7")
if (status["result"]["code"].startswith("000")):
	print "SUCCESS &lt;br/>&lt;br/> Here is the result of your transaction: &lt;br/>&lt;br/>"
	print status
else:
	print "ERROR &lt;br/>&lt;br/> Here is the result of your transaction: &lt;br/>&lt;br/>";
	print status