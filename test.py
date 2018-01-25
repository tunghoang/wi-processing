# provide test function for web service

import requests
import numpy as np

# test convolutional
def test_convolution(headers):
  dict_to_send = {
      'input' : [2, 1, 2, 1 ,5],
      'kernel': [1, 2, 3, 4]
  }
  res = requests.post('http://localhost:5000/convolution', json=dict_to_send, headers=headers)
  print res.text

# test deconvolutional
def test_deconvolution(headers):
  dict_to_send = {
      'input' : [23.0000,24.0000,30.0000,16.0000,17.0000],
      'kernel': [1, 2, 3, 4]
  }
  res = requests.post('http://localhost:5000/deconvolution', json=dict_to_send, headers=headers)
  print res.text

def test_median(headers):
  dict_to_send = {
      'input' : [1.1,2.2, 3.3, 4.4],
      'length' : 3
  }
  res = requests.post('http://localhost:5000/median', json=dict_to_send, headers=headers)
  print res.text

def test_savgol(headers):
  dict_to_send = {
      'input' : [2, 2, 5, 2, 1, 0, 1, 4, 9],
      'length': 5,
      'poly': 2,
      'deriv': 1
  }
  res = requests.post('http://localhost:5000/savgol', json=dict_to_send, headers=headers)
  print res.text

def test_fft(headers):
  N = 100
  x = np.linspace(0,2*np.pi,N)
  y = np.sin(x) + np.random.random(N) * 0.2
  dict_to_send = {
      'input': y.tolist(),
      'length': 4
  }
  res = requests.post('http://localhost:5000/fft', json=dict_to_send, headers=headers)
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
    test_median(headers)
    test_savgol(headers)
    test_fft(headers)
  except:
    print("Failed")
