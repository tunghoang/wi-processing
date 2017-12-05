# provide test function for web service

import requests

# test convolutional
def test_convolution(headers):
  dict_to_send = {
      'curve' : [1.1,2.2, 3.3, 4.4],
      'refCurve': [0.1, 1.2, 2.3, 3.4]
    }
  res = requests.post('http://localhost:5000/convolution', json=dict_to_send, headers=headers)
  print res.text

# test deconvolutional
def test_deconvolution(headers):
  dict_to_send = {
      'signal' : [2, 1],
      'divisor': [0, 1, 0, 0, 1, 1, 0, 0]
    }
  res = requests.post('http://localhost:5000/deconvolution', json=dict_to_send, headers=headers)
  print res.text

if __name__ == '__main__':
  try:
    # get token
    token = requests.post('http://localhost:5000/auth', json={"username":"test","password":"test"})
    token = token.json()["access_token"]
    token = "JWT " + token
    headers = {"Authorization": token}
    
    # request with token
    test_convolution(headers)
    test_deconvolution(headers)
  except:
    print("Failed")