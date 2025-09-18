import numpy as np

def mult_matrix():
    a = np.random.rand(30000,300)
    b = np.random.rand(300,30000)
    return print(np.dot(np.dot(a,b),a))

mult_matrix()