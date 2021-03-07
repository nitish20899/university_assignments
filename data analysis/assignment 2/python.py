import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import derivative
from scipy.stats import norm

def probability_Densityfn():
    x = sp.Symbol('x')
    xGrid=np.arange(-5,5,0.01)
    def normal(x):
        return 1/np.sqrt(2*np.pi)*np.exp(-x**2/2)
    def first(x):
        return derivative(normal,x,dx=0.01)
    def second(x):
        return derivative(first,x,dx=0.01)

    values =   np.arange(-5,5,0.01)
    density =  [normal(i) for i in values]
    first1   =  [first(i) for i in values]
    second1  =  [second(i) for i in values]

    plt.ylim([-0.45,0.45])
    plt.xlim([-5,5])
    plt.plot(xGrid,density)
    plt.plot(xGrid,first1)
    plt.plot(xGrid,second1)

probability_Densityfn()
