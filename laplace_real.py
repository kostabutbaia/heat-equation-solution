import numpy as np
from fourier import b_n
from heateq import partial_sum
from utils import get_func, partial_sum

import matplotlib.pyplot as plt

def u(x: float, y: float, N: int, x_range: list[float], L: float, M: float, f, g) -> float:
    return partial_sum(N,
                       lambda n: 1/np.sinh(n*np.pi*M/L)*b_n(n, x_range, get_func(f, x_range), L),
                       lambda n: np.sin(n*np.pi/L*x),
                       lambda n: np.sinh(n*np.pi/L*(M-y))
                       ) + \
           partial_sum(N,
                       lambda n: 1/np.sinh(n*np.pi*M/L)*b_n(n, x_range, get_func(g, x_range), L),
                       lambda n: np.sin(n*np.pi/L*x),
                       lambda n: np.sinh(n*np.pi/L*y)
                       )

def get_sol(delta_x: float, delta_y: float, L: float, M: float, f, g, N: int) -> list[list[float]]:
    x_range = np.arange(0, L + delta_x, delta_x)
    y_range = np.arange(0, M + delta_y, delta_y)
    return x_range, y_range, [
        [u(x, y, N, x_range, L, M, f, g) for x in x_range] for y in y_range
    ]


def main():
    L = 5
    M = 5
    delta_x = 0.1
    delta_y = 0.1
    f = lambda x: 9*np.sin(8*np.pi/L*x)
    g = lambda x: 3*np.sin(np.pi/L*x)
    x_range, y_range, u = get_sol(delta_x, delta_y, L, M, f, g, 10)
    X, Y = np.meshgrid(x_range, y_range)
    U = np.array(u)
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, U, cmap='plasma')
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlabel('$u(x,y)$')
    plt.show()


if __name__ == '__main__':
    main()