import numpy as np
import matplotlib.pyplot as plt

import json
from fourier import b_n
from params import *

""" Points """
x_range = np.linspace(0, L, N_x)
t_range = np.linspace(0, t_final, N_t)

""" Solution """
def particular_solution(x: float) -> float:
    return (b - a)/L * x + a

def partial_sum(N: int, *funcs):
    return sum([np.prod([func(i) for func in funcs]) for i in range(1, N)])

def get_solution_at_t(t: float, N_p: int, x_range: list[float], g, p_sol) -> list[float]:
    fourier_y = np.array([g(x) - p_sol(x) for x in x_range])
    return [
        particular_solution(x) + partial_sum(N_p, lambda n: b_n(n, x_range, fourier_y, L),
                                                  lambda n: np.exp(-(n*np.pi/L)**2*k*t), 
                                                  lambda n: np.sin(n*np.pi/L*x)) 
        for x in x_range
    ]

def get_solution() -> list[list[float]]:
    return [
        get_solution_at_t(t, N_p, x_range, g, particular_solution) for t in t_range
    ]


def graph():
    res = get_solution()
    for r in res:
        plt.plot(x_range, r)
    plt.plot(x_range, [particular_solution(x) for x in x_range], '--')
    plt.grid()
    plt.show()


if __name__ == '__main__':
    graph()