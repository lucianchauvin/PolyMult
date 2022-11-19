import numpy as np
import math


#the method of convelutions
def conv2D(x,y):
    if len(x) != len(y):
        if len(x) > len(y):
            y = y + [0]*(len(x) - len(y))
        else:
            x = x + [0]*(len(y) - len(x))

    x.reverse()
    a = [0]*(len(x)-1) + x + [0]*(len(x)-1)

    convl = [a[len(a)-p - len(x):len(a)-p] for p in range((len(x)-1)*2 + 1)]

    return np.dot(convl, [[j] for j in y])

# print(conv2D([1,2,3],[4,5,6]))

#the method of FFT
def fft2D(x,y):
    #roots of unity
    w = math.e**((2*math.pi*(0+1j))/max([len(x),len(y)]))

    #pre calulate all of our roots of unity to x power
    w_list = [w**(b) for b in range(max([len(x), len(y)]))]

    #x and y evaluated at these roots of unity, mod it cause we are just walking around the circle drawn by the roots of unity <- one of the most brilliant parts of the fft
    h1 = [sum([x[v]*(w_list[(v*c)%max([len(x), len(y)])]) for c in range(max([len(x), len(y)]))]) for v in range(max([len(x), len(y)]))]
    h2 = [sum([y[v]*(w_list[(v*c)%max([len(x), len(y)])]) for c in range(max([len(x), len(y)]))]) for v in range(max([len(x), len(y)]))]

    #point wise multiplication
    mult = [h1[a]*h2[a] for a in range(max([len(x), len(y)]))]

    #inverse fft of our new matrix????


    return h1

print(fft2D([1,2],[2,4]))