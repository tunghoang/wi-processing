# provide test function for web service

import requests

# test convolutional
def test_convolution():
  dict_to_send = {
      'curve' : [1.1,2.2, 3.3, 4.4],
      'refCurve': [0.1, 1.2, 2.3, 3.4]
    }
  res = requests.post('http://localhost:5000/convolution', json=dict_to_send)
  print res.text

# test deconvolutional
def test_deconvolution():
  dict_to_send = {
      'signal' : [2, 1],
      'divisor': [0, 1, 0, 0, 1, 1, 0, 0]
    }
  res = requests.post('http://localhost:5000/deconvolution', json=dict_to_send)
  print res.text

if __name__ == '__main__':
  test_convolution()
  test_deconvolution()