#coding:UTF-8
'''
Created on 2018年8月19日-下午6:19:56
author: Gary-W
'''
from math import *

def f(mu, sigma2, x):
    return 1/sqrt(2.*pi*sigma2) * exp(-.5*(x-mu)**2 / sigma2)

print f(10.,4.,10.) 

# Write a program to update your mean and variance
# when given the mean and variance of your belief
# and the mean and variance of your measurement.
# This program will update the parameters of your
# belief function.

def update(mean1, var1, mean2, var2):
    new_mean = 1.0 * (mean1*var2 + mean2*var1) / (var1 + var2)  
    new_var = 1.0 * var1 * var2 / (var1 + var2)
    return [new_mean, new_var]

# Write a program that will predict your new mean
# and variance given the mean and variance of your 
# prior belief and the mean and variance of your 
# motion. 
def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]


measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.

#Please print out ONLY the final values of the mean
#and the variance in a list [mu, sig]. 

# Insert code here
for i in range(len(measurements)):
    mu, sig = update(mu, sig, measurements[i], measurement_sig)
    mu, sig = predict(mu, sig, motion[i], motion_sig)

print [mu, sig]
if __name__=="__main__":
    pass

