def dot(x, y):

    if len(x[0]) == len(y) and len(x) == len(y[0]):
        raise ValueError("Invalid matrix dimensions")


    if len(y[0]) > len(x[0]):
        xcop = x.copy()
        ycop = y.copy()
        x = ycop
        y = xcop

    
    result = [[sum([x[i][j]*y[j][0] for j in range(len(y))])] for i in range(len(x))]
    return result

def multPolyOneVar(x, y):
    if len(x) != len(y):
        if len(x) > len(y):
            y = y + [0]*(len(x) - len(y))
        else:
            x = x + [0]*(len(y) - len(x))

    x.reverse()
    a = [0]*(len(x)-1) + x + [0]*(len(x)-1)
    
    mat = [a[len(a)-p -len(x):len(a)-p] for p in range((len(x)-1)*2 + 1)]

    return dot(mat, [[j] for j in y])