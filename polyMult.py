import numpy as np


#the method of convelutions
def conv(x,y):
    if len(x) != len(y):
        if len(x) > len(y):
            y = y + [0]*(len(x) - len(y))
        else:
            x = x + [0]*(len(y) - len(x))

    x.reverse()
    a = [0]*(len(x)-1) + x + [0]*(len(x)-1)

    convl = [a[len(a)-p - len(x):len(a)-p] for p in range((len(x)-1)*2 + 1)]

    return np.dot(convl, [[j] for j in y])

print(conv([1,2,3],[4,5,6]))