def solve():
    data = open("input.txt", "r").read().strip().split()
    it = iter(data)

    d = int(next(it))
    x0 = [float(next(it)) for _ in range(d)]
    x1 = [float(next(it)) for _ in range(d)]
    W = [[float(next(it)) for _ in range(d)] for _ in range(d)]
    c = [0 for _ in range(d)]

    for i in range(d):
        c[i] = x1[i] - x0[i]

    A = [[0 for _ in range(d)] for _ in range(d)]
    B = [[0 for _ in range(d)] for _ in range(d)]

    for i in range(d):
        for j in range(d):
            A[i][j] = x0[i]*x0[j] + 1/2*(x0[i]*c[j]+c[i]*x0[j]) + 1/3 * c[i]*c[j]
            B[i][j] = c[i]*x0[j] + 1/2*c[i]*c[j]

    grad_L = [[0 for j in range(d)] for i in range(d)]
    for i in range(d):
        for j in range(d):
            grad_L[i][j] = 2 *(sum([W[i][t]*A[t][j] for t in range(d)]) - B[i][j])
    
    out = []
    for row in grad_L:
        out.append(" ".join(str(x) for x in row))

    with open('output.txt', 'w') as f:
        print("\n".join(out),file=f)

if __name__ == "__main__":
    solve()