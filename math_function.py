# provide math functions for web service

from scipy import signal
import numpy as np

# convolutional
def conv(inputC, kernel):
  max_len = max(len(inputC), len(kernel))
  return np.real(np.fft.ifft( np.fft.fft(inputC, max_len)*np.fft.fft(kernel, max_len))).tolist()

# deconvolutional
def deconv(inputC, kernel):
  max_len = max(len(inputC), len(kernel))
  return np.real(np.fft.ifft( np.fft.fft(inputC, max_len)/np.fft.fft(kernel, max_len))).tolist()

# median
def median(inputC, kernel_size=None):
  return signal.medfilt(inputC, kernel_size).tolist()

#Savitzky-Golay filter
def savgol(inputC, window_length, polyorder):
  return signal.savgol_filter(inputC, window_length, polyorder).tolist()

def curve_filter():
  return 0
