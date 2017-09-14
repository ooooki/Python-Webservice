#!/usr/bin/env python

import urllib
import json
import os
import requests
import json
import re
from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webservic', methods=['POST'])
def webservic():
    
    url = 'https://www.google.com'
    data = {
  "key1": "value1",
  "key2": "value2",
  "key3": "value3",
  "key4": "value4",
  "key5":"value5"
}
    headers = {"Content-Type:": "application/json"}

    print(data)
    
    #print(type(zone))
    response = requests.post(url, data=json.dumps(data),headers={"Content-Type": "application/json"})

    jsonDict = json.loads(response.text)
    print(jsonDict)
    #responseString = response.text

    return jsonDict




if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=True, port=port, host='0.0.0.0')
