import numpy as np
import matplotlib.pyplot as plt
def f(t):
    return 5 * np.sin(2*np.pi*t)+2012
def d(t):
    return 1994 + t
x1 = np.linspace(2012, 2017, 300)
x2 = np.linspace(0, 23, 300)
plt.figure(1)
plt.subplot(211)
plt.ylabel('Anio')
plt.xlabel('Edad')
plt.plot(x2, f(x2), x2, d(x2), 'k')
plt.subplot(212)
plt.plot(x1, f(x1))
plt.savefig('doble.png')
plt.show()
