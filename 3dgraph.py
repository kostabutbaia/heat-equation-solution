import numpy as np
import matplotlib.pyplot as plt

from heateq import *

def plot_3dgraph() -> None:
    ax = plt.axes(projection='3d')
    X, T = np.meshgrid(x_range, t_range)
    U = np.array(get_solution())
    ax.plot_surface(X, T, U, cmap='plasma')
    ax.set_xlabel('$x$')
    ax.set_ylabel('$t$')
    ax.set_zlabel('$u(x,t)$')
    plt.show()

if __name__ == '__main__':
    plot_3dgraph()