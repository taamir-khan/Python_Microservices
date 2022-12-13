from flask import Flask, request
import json

app = Flask(__name__)

# Hard-coded login information for example purposes
logins = {
    'username1': 'password1',
    'username2': 'password2',
    'username3': 'password3'
}

#
# curl http://localhost:9003
#
@app.route('/')
def index():
    return json.dumps({
        'message': 'Hello, this is the login verification microservice.'
    })

#
# curl -d '{ "username": "username1", "password" : "password1" }' -X POST http://localhost:9003/verify -H "Content-type: application/json"
#
@app.route("/verify", methods=["POST"])
def verify():
    username = request.json['username']
    password = request.json['password']
    correct_login = False

    if username in logins and logins[username] == password:
        correct_login = True

    return json.dumps({
        'username': username,
        'password': password,
        'auth': correct_login
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9003)

