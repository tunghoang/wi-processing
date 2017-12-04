import flask
import math_function
from json_respond import json_respond

app = flask.Flask("wi-processing");
@app.route('/')
def index():
    return "this is index"

@app.route('/convolution', methods=["POST"])
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

app.run()

