import numpy as np
import matplotlib.pyplot as plt
import math 

def f(x):
    return (math.e)**x

def g(x):
    return 1 + x + 0.5*x**2 + 0.1667*x**3

x_range = np.linspace(-0.5, 0.5, 1000)
y_res_f = f(x_range)
y_res_g = g(x_range)

plt.plot(x_range, f(x_range), x_range, g(x_range))

plt.show()
