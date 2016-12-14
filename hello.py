from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import requests
import json



app = Flask(__name__)

@app.route("/")
def hello():
    userid = "facebook10204943661328005"
    password = "L3Sid2UJKaea3ZMB"
    tenatid = "e73765c2080d4c038efc2acb094bbc1f"
    url = 'http://x86.trystack.org:5000/v2.0/tokens'
    headers = {'content-type': 'application/json'}
    payload = {'auth':{'passwordCredentials':{'username': userid, \
        'password':password}, 'tenantId':tenatid}}    
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    #print r.headers.get('content-type')
    #print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
    json_data = r.json()
    r.close()
    tokens = json.loads(json.dumps(json_data))
    #print tokens
    tokenid = tokens['access']['token']['id']
    print tokenid
    url = 'http://x86.trystack.org:8774/v2/e73765c2080d4c038efc2acb094bbc1f/flavors'
    headers = {'X-Auth-Token':str(tokenid)}
    r = requests.get(url, headers=headers)
    json_data = r.json()
    print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
    json_data = r.json()
    r.close()
    return render_template('coba.html', json_data = json_data)

@app.route("/create")
def create():
    return "Buat mesin" 


if __name__ == "__main__":
    app.run()
