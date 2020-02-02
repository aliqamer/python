from flask import Flask, jsonify, request
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


def checkPostedDate(postedData, functionName):
    if(functionName == 'add'):
        if 'x' not in postedData or 'y' not in postedData:
            return 404
        else:
            return 200


class Add(Resource):

    def post(self):
        data = request.get_json()

        statusCode = checkPostedDate(data, 'add')
        if statusCode != 200:
            retJson = {
                'Message': 'Missing arguments',
                'Status': 404
            }
            return jsonify(retJson)

        x = data["x"]
        y = data["y"]
        x = int(x)
        y = int(y)
        ret = x+y
        retMap = {
            'Message': ret,
            'Status': 200
        }
        return jsonify(retMap)


class Sub(Resource):
    pass


class Mul(Resource):
    pass


class Div(Resource):
    pass


api.add_resource(Add, '/add')


@app.route('/')
def hello_world():
    return "hello world !"


if __name__ == "__main__":
    app.run(debug=True)
