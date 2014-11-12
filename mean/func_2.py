import numpy as np

def dim(x):
    x_np = np.array(x)
    return x_np.shape

print(dim(range(10))[0] == 10)
