import requests
import sys
import urllib.parse

client_id = open('client_id').read()
client_secret = open('client_secret').read()

payload = {
    'grant_type': 'fb_exchange_token',
    'client_id': client_id,
    'client_secret': client_secret,
    'fb_exchange_token': sys.argv[1] # takes short-lived Access Token
}

r = requests.get("https://graph.facebook.com/oauth/access_token", params=payload)
try:
    access_token = urllib.parse.parse_qs(r.text)['access_token'][0]
    print(access_token, end="")
except:
    print(r.text, file=sys.stderr)