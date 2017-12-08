# provide math functions for web service

from scipy import signal
import xalglib

# convolutional
def conv(inputC, kernel, size):
  return xalglib.convr1dcircular(inputC, size, kernel, size)

# deconvolutional
def deconv(inputC, kernel, size):
  return xalglib.convr1dcircularinv(inputC, size, kernel, size)

def curve_filter():
  return 0