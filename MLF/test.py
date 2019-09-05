import os
from flask import Flask , request
from flask_cors import CORS,cross_origin
import json
import requests 
from base64 import b64encode

app = Flask(__name__)
cors = CORS(app)

port = int(os.environ.get('PORT'))


@app.route('/topicDetection',methods = ['POST'])
def hello():

    config = json.loads(open('urls.json').read());
    print(config["serviceurls"]["TOPIC_DETECTION_URL"])
    url = config["url"] + '/oauth/token?grant_type=client_credentials'
    auth = config["clientid"]+":"+config["clientsecret"]
    userAndPass = b64encode(bytes(auth, encoding= 'utf-8')).decode("ascii")
    headers = { 'Authorization' : 'Basic %s' %  userAndPass }
    r=requests.get(url, headers=headers)
    y = json.loads(r.content)
    f= request.files["files"]
    f ={"files": (f.filename, f.stream, f.mimetype)}
    print(f)

    headers = { 'Authorization' : 'Bearer %s' %  y["access_token"] }

    r = requests.post(config["serviceurls"]["IMAGE_CLASSIFICATION_URL"],files=f,headers=headers)

    return str(r.content)
    

if __name__ == '__main__':
	
	
	app.run(host='0.0.0.0',port=port)

