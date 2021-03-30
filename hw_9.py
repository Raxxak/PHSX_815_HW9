# imports packages
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt



#Define a function    
def function(x):
    return  pow(x,2)+4*x
#It minimizes the  function

minimum_value = minimize(function,0)
    
print('minimum value= ',minimum_value.x)

#Visualization part

x=[]
y=[]
j=0
for j in range(60):
    i=j/10-5
    x.append(i)
    y.append(function(i))


plt.plot(x,y)
plt.plot([],[],label='minimum= '+str(minimum_value.x))
plt.legend()
plt.savefig('minimize.png')
plt.show()
    
    
   
