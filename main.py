import flask
from flask_cors import CORS
from flask_jwt import JWT, jwt_required
from flask_cors import CORS
import ConfigParser
import math_function
from json_respond import json_respond
import ctypes

lib = ctypes.cdll.LoadLibrary('./alglib.so')
lib.conv.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
lib.conv.restype = ctypes.c_char_p
lib.deconv.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
lib.deconv.restype = ctypes.c_char_p

# load config from config file
configParser = ConfigParser.RawConfigParser()
configParser.read("config")

app = flask.Flask("wi-processing");
CORS(app)
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
#@jwt_required()
def convolution():
  if flask.request.method == "POST":
    # get input from the json file
    conv_json = flask.request.get_json()
    
    inputCurve = conv_json['input']
    m = len(inputCurve)
    input_str = "["+",".join(map(str,inputCurve))+"]"
    
    kernel = conv_json['kernel']
    n = len(kernel)
    kernel_str = "["+",".join(map(str,kernel))+"]"
    
    result_curve = lib.conv(input_str, m, kernel_str, n)

    content = {'curve': result_curve}
    # return output as a json file
    result_json = json_respond(200, "success", content)
    return flask.jsonify(result_json)


@app.route('/deconvolution', methods=["POST"])
#@jwt_required()
def deconvolution():
  if flask.request.method == "POST":
    # get input from the json file
    deconv_json = flask.request.get_json()
    inputCurve = deconv_json['input']
    m = len(inputCurve)
    input_str = "["+",".join(map(str,inputCurve))+"]"

    kernel = deconv_json['kernel']
    n = len(kernel)
    kernel_str = "["+",".join(map(str,kernel))+"]"
    
    result_curve = lib.deconv(input_str, m, kernel_str, n)

    content = {'curve': result_curve}

    # return output as a json file
    result_json = json_respond(200, "success", content)

    return flask.jsonify(result_json)


@app.route('/median', methods=["POST"])
#@jwt_required()
def median():
    if flask.request.method == "POST":
        # get input from the json file
        median_json = flask.request.get_json()
        inputCurve = median_json['input']

        result_curve = math_function.median(inputCurve)
        content = {'curve': result_curve}

        # return output as a json file
        result_json = json_respond(200, "success", content)

        return flask.jsonify(result_json)


@app.route('/savgol', methods=["POST"])
#@jwt_required()
def savgol():
    if flask.request.method == "POST":
        # get input from the json file
        savgol_json = flask.request.get_json()
        inputCurve = savgol_json['input']
        window_length = savgol_json['window_length']
        polyorder = savgol_json['polyorder']

        result_curve = math_function.savgol(
            inputCurve, window_length, polyorder)
        content = {'curve': result_curve}

        # return output as a json file
        result_json = json_respond(200, "success", content)

        return flask.jsonify(result_json)


app.run(debug=True)
