from fractions import Fraction
from functools import reduce

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a*b) // gcd(a,b)

def lcmm(args):
    return reduce(lcm, args)

def subtract_matrices(a, b):
    return [[a[i][j]-b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def invert_matrix(a):
    n = len(a)
    a_inv = [[Fraction(int(i==j), 1) for j in range(n)] for i in range(n)]

    for i in range(n):
        if a[i][i] == 0:
            for j in range(i+1, n):
                if a[j][i] != 0:
                    a[i], a[j] = a[j], a[i]
                    a_inv[i], a_inv[j] = a_inv[j], a_inv[i]
                    break

        scale = a[i][i]
        for j in range(n):
            a[i][j] /= scale
            a_inv[i][j] /= scale

        for j in range(n):
            if i != j:
                scale = a[j][i]
                for k in range(n):
                    a[j][k] -= scale * a[i][k]
                    a_inv[j][k] -= scale * a_inv[i][k]

    return a_inv

def solution(m):
    if all(row == [0]*len(row) for row in m):
        return [1] + [0]*(len(m)-1)

    n = len(m)
    sums = list(map(sum, m))
    terminal_states = [i for i, row_sum in enumerate(sums) if row_sum == 0]
    transient_states = list(set(range(n)) - set(terminal_states))

    terminal_states.sort()  # Ensure the terminal states are in order
    transient_states.sort()  # Ensure the transient states are in order

    normalized_m = []
    for row in m:
        row_sum = sum(row)
        if row_sum == 0:
            normalized_m.append(row)
        else:
            normalized_m.append([Fraction(x, row_sum) for x in row])

    Q = [[normalized_m[i][j] for j in transient_states] for i in transient_states]
    R = [[normalized_m[i][j] for j in terminal_states] for i in transient_states]

    I = [[Fraction(int(i==j), 1) for j in range(len(Q))] for i in range(len(Q))]
    F = invert_matrix(subtract_matrices(I, Q))

    FR = [[0]*len(R[0]) for _ in range(len(F))]
    for i in range(len(F)):
        for j in range(len(R[0])):
            for k in range(len(R)):
                FR[i][j] += F[i][k] * R[k][j]

    probabilities = FR[0]
    lcm_denominator = lcmm([x.denominator for x in probabilities])
    result = [int(x * lcm_denominator) for x in probabilities] + [lcm_denominator]

    # Handle the case where the sum of probabilities is 0
    if sum(result) == 0:
        return [1] + [0] * len(result)

    return result

m = [
    [0, 1, 0, 0, 0, 1],
    [4, 0, 0, 3, 2, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

print(solution(m))  # Output: [0, 3, 2, 9, 14]
