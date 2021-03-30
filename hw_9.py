# imports packages
import numpy as np
from scipy.optimize import minimize
import matplotlib as plt



#Define a function    
def function(x):
    return  x+x**2+x**4
#It minimizes the  function

minimum_value = minimize(function,0)
    
print('minimum value= ',minimum_value.x)
    
   
