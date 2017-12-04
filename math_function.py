# provide math functions for web service

from scipy import signal

# convolutional
def conv(curve, ref_curve):
  return signal.convolve(curve, ref_curve)

# deconvolutional
def deconv(impulse_response, original):
  recorded = signal.convolve(impulse_response, original)
  return signal.deconvolve(recorded, impulse_response)

def curve_filter():
  return 0