import json
import base64
import requests
config = json.loads(open('urls.json').read())
url = config['url']+"/oauth/token?grant_type=client_credentials"
cred = config['clientid']+":"+config['clientsecret']
cred=base64.b64encode(cred.encode('utf-8')) 
r = requests.get(url,headers= {"Authorization":"Basic "+cred})
print(url)
print(r)
