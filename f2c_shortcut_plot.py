#Exercise 5.2
import numpy as np
import matplotlib.pyplot as plt

def C_approx(F):
    return (F - 30)/2.0

def C_exact(F):
    return (F - 32)*(5.0/9)

F = np.linspace(-20, 120) #F values in interval [-20, 120]
y1 = C_approx(F)
y2 = C_exact(F)

plt.plot(F, y1)
plt.plot(F, y2)
#plotting functions in same plot

plt.xlabel('F')
plt.ylabel('C')
#labeling axis
plt.legend(['C_approx', 'C_exact)'])
#labeling functions
plt.title('f2c_shortcut_plot')
#labeling graph
plt.show()

"""
terminal >> python f2c_shortcut_plot.py 

"""
