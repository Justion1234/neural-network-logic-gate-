import numpy as np
import matplotlib.pyplot as plt
plt.style.use(['seaborn-whitegrid'])

def OR(a, b):
    input = np.array([a, b])
    weights = np.array([0.4, 0.5])
    bias = -0.3
    value = np.sum(input*weights) + bias

    if value <= 0:
        return 0
    else:
        return 1

print(OR(0, 0))
print(OR(0, 1))
print(OR(1, 0))
print(OR(1, 1))

