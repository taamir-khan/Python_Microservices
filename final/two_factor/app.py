from flask import Flask, request
import json
import random

app = Flask(__name__)

# Possible 2-factor authentication codes that could be sent to someone's phone
possible_codes = ['50239', '89439', '59230']

#
# curl http://localhost:9003
#
@app.route('/')
def index():
    return json.dumps({
        'message': 'Hello, this is the 2-factor authentication microservice.'
    })

#
# curl -d '{ "first_name": "first_name", "code" : "code_sent_to_phone" }' -X POST http://localhost:9003/authorize -H "Content-type: application/json"
#
@app.route("/authorize", methods=["POST"])
def authorize():
    first_name = request.json['first_name']
    code_sent_to_phone = request.json['code']
    correct_code = code_sent_to_phone in possible_codes

    return json.dumps({
        'first_name': first_name,
        'code': code_sent_to_phone,
        'auth': correct_code
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9003)
