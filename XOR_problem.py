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

def NAND(a,b):
    input = np.array([a, b])
    weight = np.array([-0.6, -0.5])
    bias = 0.7
    value = np.sum(input * weight) + bias
    if value <= 0:
        return 0
    else:
        return 1

def OR(a, b):
    input = np.array([a, b])
    weights = np.array([0.4, 0.5])
    bias = -0.3
    value = np.sum(input*weights) + bias

    if value <= 0:
        return 0
    else:
        return 1

def XOR(x1, x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

print(XOR(0, 0))
print(XOR(0, 1))
print(XOR(1, 0))
print(XOR(1, 1))


