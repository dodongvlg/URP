import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

if __name__ == '__main__':