import hashlib
import math
from flask import Flask
from flask import jsonify
from flask import request
from datetime import datetime
path = '/op/v0/device/real/query'
lang = 'pl'

##timestamp = math.trunc(datetime.timestamp(datetime.now()))*1000
app = Flask(__name__)


@app.route('/', methods=['GET'])
def api_get():
        return jsonify(result='zastosuj POST')


@app.route('/', methods=['POST'])
def api_post():
        #token = request.headers['token']
        #timestampH = request.headers['timestamp']
        body = request.get_json()
        timestamp = body['timestamp']
        token = body['token']
        body = request.get_json()
        print(body['signature'])
        print(fr"{path}\r\n{token}\r\n{timestamp}")
        body['signature'] = hashlib.md5(fr"{path}\r\n{token}\r\n{timestamp}".encode('UTF-8')).hexdigest()
        print(body['signature'])
        return body

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
