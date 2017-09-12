import numpy as np
import matplotlib.pyplot as plt
def f(t):
    return 5 * np.sin(2*np.pi*t)+2012
x1 = np.arange(2012, 2018, 0.01)
plt.plot(x1, f(x1))
plt.savefig('trig.png')
plt.show()
