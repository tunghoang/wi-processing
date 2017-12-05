import flask
from flask_jwt import JWT, jwt_required
import ConfigParser
import math_function
from json_respond import json_respond

# load config from config file
configParser = ConfigParser.RawConfigParser()  
configParser.read("config")

app = flask.Flask("wi-processing");
# set secret key to generate token
app.config['SECRET_KEY'] = configParser.get('key', 'SECRET_KEY')

class User(object):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return "User(id='%s')" % self.id

# verify user to send token
def verify(username, password):
    if not (username and password):
        return False
    if configParser.get('user', 'NAME') == username \
      and configParser.get('user', 'PASSWORD') == password:
        return User(id=configParser.get('user', 'ID'))
# identity user
def identity(payload):
    user_id = payload['identity']
    return {"user_id": user_id}

jwt = JWT(app, verify, identity)

@app.route('/')
def index():
    return "this is index"

@app.route('/convolution', methods=["POST"])
@jwt_required()
def convolution():
  if flask.request.method == "POST":
    # get input from the json file
    conv_json = flask.request.get_json()
    curve = conv_json['curve']
    ref_curve = conv_json['refCurve']

    result_curve = math_function.conv(curve, ref_curve)
    content = {'curve': result_curve.tolist()}

    # return output as a json file 
    result_json = json_respond(200, "success", content)

    return flask.jsonify(result_json)

@app.route('/deconvolution', methods=["POST"])
@jwt_required()
def deconvolution():
  if flask.request.method == "POST":
    # get input from the json file
    deconv_json = flask.request.get_json()
    signal = deconv_json['signal']
    divisor = deconv_json['divisor']

    quotient, remainder = math_function.deconv(signal, divisor)
    content = {'quotient': quotient.tolist(), 'remainder': remainder.tolist()}

    # return output as a json file 
    result_json = json_respond(200, "success", content)

    return flask.jsonify(result_json)

app.run(debug=True)

