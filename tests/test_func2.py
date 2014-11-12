from mean import func_2
import numpy as np

def test_func_2_10():
    assert func_2.dim(range(10))[0] == 10

def test_func_2_2d():
    assert func_2.dim(np.ones([4,6]))[0] == 4
    assert func_2.dim(np.ones([4,6]))[1] == 6

