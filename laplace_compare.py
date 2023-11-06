import numpy as np
from laplace_real import get_sol
from laplace_numerical import get_num_sol

import matplotlib.pyplot as plt

L = 5
M = 5
delta_x = 0.1
delta_y = 0.1

def f(x: float) -> float:
    return 9*np.sin(8*np.pi/L*x)

def g(x: float) -> float:
    return 3*np.sin(np.pi/L*x)

def compare_graph() -> None:
    x_range, y_range, u_real = get_sol(delta_x, delta_y, L, M, f, g, 10)
    _, _, u_num = get_num_sol(delta_x, delta_y, L, M, g, f)

    X, Y = np.meshgrid(x_range, y_range)
    U_real = np.array(u_real)
    U_num = np.array(u_num)

    # Plot The Solutions
    fig = plt.figure(figsize=plt.figaspect(0.5))

    ax = fig.add_subplot(1, 2, 1, projection='3d')
    ax.set_title('Real Solution')
    ax.plot_surface(X, Y, U_real, cmap='plasma')
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlabel('$u(x,y)$')

    ax = fig.add_subplot(1, 2, 2, projection='3d')
    ax.set_title('Finite Difference Solution')
    ax.plot_surface(X, Y, U_num, cmap='plasma')
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlabel('$u(x,y)$')
    plt.show()

if __name__ == '__main__':
    compare_graph()
