# System Imports
import re
import sys
import json
import time
import math
import random
import pycurl
import urllib
import urllib2

from hashlib import md5
from oauth.oauth import OAuthRequest, OAuthSignatureMethod_HMAC_SHA1

try:
    import config
except:
    print "Configuration ERROR: copy config_example.py into config.py",
    print "and follow instructions in the file."
    sys.exit(0)

class Token(object):
    def __init__(self,key,secret):
        self.key = key
        self.secret = secret

    def _generate_nonce(self):
        random_number = ''.join(str(random.randint(0, 9)) for i in range(40))
        m = md5(str(time.time()) + str(random_number))
        return m.hexdigest()


access_token = Token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
consumer = Token(config.CONSUMER_KEY, config.CONSUMER_SECRET)
    
parameters = {
    'oauth_consumer_key': config.CONSUMER_KEY,
    'oauth_token': access_token.key,
    'oauth_signature_method': 'HMAC-SHA1',
    'oauth_timestamp': str(int(time.time())),
    'oauth_nonce': access_token._generate_nonce(),
    'oauth_version': '1.0',
}


oauth_request = OAuthRequest.from_token_and_callback(access_token,
                http_url=config.STREAM_URL,
                parameters=parameters)
signature_method = OAuthSignatureMethod_HMAC_SHA1()
signature = signature_method.build_signature(oauth_request, consumer, access_token)

parameters['oauth_signature'] = signature

data = urllib.urlencode(parameters)

def on_receive(data):
    """Hands over data to tweet processing function."""
    if data is not None or data is not '\r\n':
        # do something with the data.
        print data
        
    return None
    

print "Initializing...",
conn = pycurl.Curl()
conn.setopt(pycurl.URL, config.STREAM_URL+"?"+data)
conn.setopt(pycurl.WRITEFUNCTION, on_receive)
conn.perform()