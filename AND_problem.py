import numpy as np
import matplotlib.pyplot as plt
plt.style.use(['seaborn-whitegrid'])

def AND(a,b):
    input = np.array([a, b])
    weight = np.array([0.4]) #가중치
    bias = -0.6 #편향
    value = np.sum(input * weight) + bias
    if value <= 0:
        return 0
    else:
        return 1



print(AND(0, 0))
print(AND(0, 1))
print(AND(1, 0))
print(AND(1, 1))