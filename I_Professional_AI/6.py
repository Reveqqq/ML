def solve():

    data = open("input.txt", "r").read().strip().split()
    it = iter(data)

    L = int(next(it))
    d = int(next(it))

    # читаем A, C, V
    A = [[float(next(it)) for _ in range(d)] for _ in range(L)]
    C = [[float(next(it)) for _ in range(d)] for _ in range(L)]
    V = [[float(next(it)) for _ in range(d)] for _ in range(L)]

    O = [[0.0 for _ in range(d)] for _ in range(L)]

    for t in range(L):
        for j in range(t + 1):
            coef = sum(A[t][k] * C[j][k] for k in range(d))
            for k in range(d):
                O[t][k] += coef * V[j][k]

    out = []
    for row in O:
        out.append(" ".join(str(x) for x in row))

    with open('output.txt', 'w') as f:
        print("\n".join(out),file=f)


if __name__ == "__main__":
    solve()