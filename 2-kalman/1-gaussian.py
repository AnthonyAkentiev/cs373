from math import *

# We don't need a histogram of position probabilities, and can reduce it to single function with 2 parameters - Gaussian
# (10., 4.)

# Gaussian function with 2 params:
# mu - expected value
# sigma2 - covariance
# 
# x
def gaussian(mu,sigma2,x):
     return 1/sqrt(2. * pi * sigma2) * exp(-.5 * (x-mu)**2 / sigma2)

print gaussian(10., 4., 8.)
