import numpy as np
import matplotlib.pyplot as plt
plt.style.use(['seaborn-whitegrid'])

def NAND(a,b):
    input = np.array([a, b])
    weight = np.array([-0.6, -0.5])
    bias = 0.7
    value = np.sum(input * weight) + bias
    if value <= 0:
        return 0
    else:
        return 1


print(NAND(0, 0))
print(NAND(0, 1))
print(NAND(1, 0))
print(NAND(1, 1))