#Qs 2b
from scipy import random
import numpy as np
 
# limits of integration
a = 0
b = np.pi
N = 1000
 
# array of zeros 
xrand = np.zeros(N)
 
for i in range (len(xrand)):
    xrand[i] = random.uniform(a,b) #filling random values between a and b

integral = 0.0
 
# define function
# function can be changed according to the qs
def f(x):
    return np.sin(x) #example
 
# iterate and sum up values of different functions of x
for i in xrand:
    integral += f(i)
 
#derived formula
ans = (b-a)/float(N)*integral
print ('Answer :', ans)