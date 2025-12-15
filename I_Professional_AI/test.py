# algorithm AnalyticalSolution(k, s, p, L):
#     // INPUT
#     //    k = layer parameters [k_1, k_2, ..., k_L]
#     //    s = layer parameters [s_1, s_2, ..., s_L]
#     //    L = the number of layers
#     // OUTPUT
#     //    r = the calculated receptive field size
    
#     r <- 1
#     S <- 1
    
#     for l <- 1 to L:
#         for i <- 1 to l:
#             S <- S * s[i]
#         r <- r + (k[l] - 1) * S
    
#     return r

def CalculateReceptiveFieldSize(k,s,L):
    """
    Docstring for CalculateReceptiveFieldSize
    
    :param k: layer parameters [k_1, k_2, ..., k_L]
    :param s: layer parameters [s_1, s_2, ..., s_L]
    :param L: the number of layers
    """

    r = 1
    S = 1

    for l in range(0,L):
        for i in range(0,l):
            S = S * s[i]

        r = r + (k[l] - 1) * S
    
    return r

if __name__ == "__main__":
    k = [3,5,2]
    s = [1,2,2]
    p = [1,2,0]
    L = 3
    print(CalculateReceptiveFieldSize(k,s,L))
    # print(RecursiveSolution(k,s,p,L))