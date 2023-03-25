from math import factorial as fct


def combinations(k, n):
    return fct(n) / (fct(k) * fct(n - k))


def probability(m, n):
    return m / n
