import matplotlib.pyplot as plt
import numpy as np
from math_function import Function

# Plot the function
def plot_function(f,x):
    y = f.value(x)
    plt.plot(x,y)
    plt.show()
    
def plot_changes(f,x, old_x, new_x, title = '', show = False):
    # if old_x outside of x range, plot a point at the edge
    if old_x < x[0]:
        old_x = x[0]
    