import numpy as np
from scipy.optimize import minimize_scalar

def entropy(y):
    x = (1-3*y)/2

    if x <= 0 or y <= 0:
        return 1e9
    
    pA = pB = x
    pD = y
    pC = 2*y

    p = np.array([pA, pB, pC, pD])
    return -(p*np.log2(p)).sum()

if __name__ == "__main__":
    res = minimize_scalar(lambda y: -entropy(y), bounds=(1e-12, 1/3 - 1e-12))

    y_opt = res.x
    x_opt = (1 - 3*y_opt)/2

    pA = pB = x_opt
    pD = y_opt
    pC = 2 * y_opt

    print(f"{pA:.3f}, {pB:.3f}, {pC:.3f}, {pD:.3f}")

    print(entropy(y_opt))
