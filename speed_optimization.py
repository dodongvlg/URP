import numpy as np

def opt_sigmoid(x):
    temp = x - 3.5
    temp = 1 / (1 + np.exp(-2 * temp)) - 0.5
    temp *= 2
    return temp

def opt_tanh(x):
    temp = x - 3.5
    return np.tanh(temp)

def opt_ReLU(x):
    if x <= 1.5:
        return -1
    elif x >= 5.5:
        return 1
    else:
        return 0.5 * x - 1.75

def opt_linear(x):
    return 0.4 * x - 1.4

def opt_log(x):
    if x >= 3.5:
        temp = x - 2.5
        temp = np.log(temp)
        temp *= 0.75
        return temp
    else:
        temp = 4.5 - x
        temp = np.log(temp)
        temp *= -0.75
        return temp

if __name__ == '__main__':
    pass