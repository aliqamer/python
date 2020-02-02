from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/add_number', methods=['POST'])
def add_number():
    dataDict = request.get_json()
    x = dataDict['x']
    y = dataDict['y']
    z = x+y

    retJson = {
        "z": z
    }

    return jsonify(retJson), 200
