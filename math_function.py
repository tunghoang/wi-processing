# provide math functions for web service

from scipy import signal, fftpack
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

# Savitzky-Golay filter
def savgol(inputC, window_length, polyorder, deriv):
  result = signal.savgol_filter(inputC, window_length, polyorder, deriv).tolist()
  result = [round(result[i], 4) for i in range(len(result))]
  return result

def curve_filter():
  return 0

# smooth curve by using Fourier
def fft(y, length=4):
  w = fftpack.rfft(y)
  cutoff_idx = abs(w) < w.max()/int(length)
  w[cutoff_idx] = 0
  y_new = fftpack.irfft(w).tolist()
  y_new = [round(y_new[i], 4) for i in range(len(y_new))]
  return y_new

  
# N = 1000
# x = np.linspace(0,2*np.pi,N)
# y = np.sin(x) + np.random.random(N) * 0.2
# y_new = fft(y)
# y_new_2 = fft(y, 5)
# y_new_3 = fft(y, 10)
# import matplotlib.pyplot as plt
# plt.figure()
# plt.plot(x, y, c="red")
# plt.plot(x, y_new, c="green")
# plt.plot(x, y_new_2, c="blue")
# plt.plot(x, y_new_3, c="black")
# plt.show()
