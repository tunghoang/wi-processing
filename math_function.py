# provide math functions for web service

from scipy import signal
import numpy as np

# convolutional
def conv(inputC, kernel):
  max_len = max(len(inputC), len(kernel))
  result = np.real(np.fft.ifft( np.fft.fft(inputC, max_len)*np.fft.fft(kernel, max_len))).tolist()
  result = [round(result[i], 4) for i in range(len(result))]
  return result

# deconvolutional
def deconv(inputC, kernel):
  max_len = max(len(inputC), len(kernel))
  result = np.real(np.fft.ifft( np.fft.fft(inputC, max_len)/np.fft.fft(kernel, max_len))).tolist()
  result = [round(result[i], 4) for i in range(len(result))]
  return result

# median
def median(inputC, kernel_size=None):
  result = signal.medfilt(inputC, kernel_size).tolist()
  result = [round(result[i], 4) for i in range(len(result))]
  return result

#Savitzky-Golay filter
def savgol(inputC, window_length, polyorder):
  result = signal.savgol_filter(inputC, window_length, polyorder).tolist()
  result = [round(result[i], 4) for i in range(len(result))]
  return result

def curve_filter():
  return 0
