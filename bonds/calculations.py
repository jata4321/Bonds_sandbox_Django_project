import numpy as np

def mult_matrix():
    a = np.random.rand(300_000,300_000)
    b = np.random.rand(300_000,300_000)
    return print(np.dot(np.dot(a,b),a))

mult_matrix()