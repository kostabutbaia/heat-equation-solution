import numpy as np

def get_func(func, x_range: list[float]) -> list[float]:
    return [
        func(x) for x in x_range
    ]

def partial_sum(N: int, *funcs):
    return sum([np.prod([func(i) for func in funcs]) for i in range(1, N)])