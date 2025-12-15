import re
import math

def solve():
    data = re.split(r'[,.\n? ]+', open("input.txt", "r").read().strip())
    it = iter(data)

    M = int(next(it))
    C = int(next(it))
    n = int(next(it))
    
    a = [[[0 for _ in range(n)] for _ in range(M)] for _ in range(C)]


    for i in range(C):
        for j in range(M):
            for k in range(n):
                a[i][j][k] = int(next(it))

    k = [[0 for _ in range(n)] for _ in range(C)]
    
    for c in range(C):
        for i in range(n):
            x_ci = sum([a[c][j][i] for j in range(M)]) / (M+1)

            if 1/x_ci > 0.05:
                k[c][i] = 0.05
            elif 1/x_ci < 0.002:
                k[c][i] = 0.002
            else:          
                k[c][i] = 1/x_ci

    x_test = [int(next(it)) for _ in range(n)]

    best_log_likelihood = -float('inf')
    best_class = c

    for c in range(C):
        log_likelihood = 0
        k_class = k[c]
        for i in range(n):
            log_likelihood += math.log(k_class[i]) - k_class[i]*x_test[i]
        
        if log_likelihood > best_log_likelihood:
            best_log_likelihood= log_likelihood
            best_class = c
    
    with open('output.txt', 'w') as f:
        print(best_class + 1, file=f)



if __name__ == "__main__":
    solve()