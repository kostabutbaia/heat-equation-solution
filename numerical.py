import numpy as np
import matplotlib.pyplot as plt

from params import *

x_range = np.arange(0, L + delta_x, delta_x)
t_range = np.arange(0, t_final + delta_t, delta_t)

def get_solution_at_n(n: int, u_at_prev_n: list[float]) -> list[float]:
    u_at_t = [0]*len(x_range)
    u_at_t[0], u_at_t[-1] = u_0(n*delta_t), u_L(n*delta_t)
    for i in range(1, len(x_range) - 1):
        u_at_t[i] = k**2 * delta_t/delta_x**2 * (u_at_prev_n[i+1] + u_at_prev_n[i-1] - 2*u_at_prev_n[i]) + u_at_prev_n[i]
    return u_at_t

def get_num_solution() -> list[list[float]]:
    u_init = [g(x) for x in x_range]
    sol = [0]*len(t_range)
    sol[0] = u_init
    for i in range(1, len(t_range)):
        sol[i] = get_solution_at_n(i, sol[i-1])
    return sol

def main():
    res = get_num_solution()

    for r in res:
        plt.plot(x_range, r)
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()