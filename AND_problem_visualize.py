import numpy as np
import matplotlib.pyplot as plt
plt.style.use(['seaborn-whitegrid'])

x1 = np.arange(-2, 2, 0.01)
x2 = np.arange(-2, 2, 0.01)
bias = -0.6

y = (-0.4 * x1 - bias) / 0.4

plt.axvline(x=0)
plt.axhline(y=0)

plt.plot(x1, y, 'r--')
plt.scatter(0, 0, color='orange', marker='o', s=150)
plt.scatter(0, 1, color='orange', marker='o', s=150)
plt.scatter(1, 0, color='orange', marker='o', s=150)
plt.scatter(1, 1, color='black', marker='^', s=150)
plt.xlim(-0.5, 1.5)
plt.ylim(-0.5, 1.5)
plt.grid()
plt.show()