import numpy as np
from utils import get_func

import matplotlib.pyplot as plt

def get_var_pos(i: int, j: int, N_x: int) -> int:
    return i + N_x*j

def add_laplace_eqs(eq_matrix: list[list[float]], f: list[float], N_x: int, N_y: int) -> None:
    for i in range(1, N_x-1):
        for j in range(1, N_y-1):
            eq_to_add = np.zeros((N_x*N_y))
            eq_to_add[get_var_pos(i, j, N_x)] = -4
            eq_to_add[get_var_pos(i+1, j, N_x)] = 1
            eq_to_add[get_var_pos(i-1, j, N_x)] = 1
            eq_to_add[get_var_pos(i, j+1, N_x)] = 1
            eq_to_add[get_var_pos(i, j-1, N_x)] = 1
            eq_matrix.append(eq_to_add)
            f.append(0)

def add_boundary_x0(f_func, eq_matrix: list[list[float]], f: list[float], N_x: int, N_y: int) -> None:
    for i in range(N_x):
        eq_to_add = np.zeros((N_x*N_y))
        eq_to_add[get_var_pos(i, 0, N_x)] = 1
        eq_matrix.append(eq_to_add)
        f.append(f_func[i])

def add_boundary_xM(g_func, eq_matrix: list[list[float]], f: list[float], N_x: int, N_y: int) -> None:
    for i in range(N_x):
        eq_to_add = np.zeros((N_x*N_y))
        eq_to_add[get_var_pos(i, N_y-1, N_x)] = 1
        eq_matrix.append(eq_to_add)
        f.append(g_func[i])


def add_boundary_0y(eq_matrix: list[list[float]], f: list[float], N_x: int, N_y: int) -> None:
    for i in range(1, N_y-1):
        eq_to_add = np.zeros((N_x*N_y))
        eq_to_add[get_var_pos(0, i, N_x)] = 1
        eq_matrix.append(eq_to_add)
        f.append(0)


def add_boundary_Ly(eq_matrix: list[list[float]], f: list[float], N_x: int, N_y: int) -> None:
    for i in range(1, N_y-1):
        eq_to_add = np.zeros((N_x*N_y))
        eq_to_add[get_var_pos(N_x-1, i, N_x)] = 1
        eq_matrix.append(eq_to_add)
        f.append(0)

def split_array_N(arr: list[float], N: int) -> list[float]:
    if len(arr) % N != 0:
        raise Exception(f'cannot evenly divide arr with each array of length {N}')
    return [arr[i*N:(i+1)*N] for i in range(int(len(arr)/N))]

def get_num_sol(delta_x: float, delta_y: float, L: float, M: float, g_func, f_func) -> list[list[float]]:
    x_range = np.arange(0, L + delta_x, delta_x)
    y_range = np.arange(0, M + delta_y, delta_y)
    N_x = len(x_range)
    N_y = len(y_range)
    eq_matrix = list()
    f = list()

    # Add laplace equations
    add_laplace_eqs(eq_matrix, f, N_x, N_y)

    # Add boundary conditions
    f_func_values = get_func(f_func, x_range)
    add_boundary_x0(f_func_values, eq_matrix, f, N_x, N_y)

    g_func_values = get_func(g_func, x_range)
    add_boundary_xM(g_func_values, eq_matrix, f, N_x, N_y)

    add_boundary_0y(eq_matrix, f, N_x, N_y)
    add_boundary_Ly(eq_matrix, f, N_x, N_y)

    # Solve system of equations
    eq_matrix_np = np.array(eq_matrix)
    f_np = np.array(f)
    sol = np.linalg.solve(eq_matrix_np, f_np)

    return x_range, y_range, split_array_N(sol, N_x)


def main():
    f = lambda x: 9*np.sin(8*np.pi/L*x)
    g = lambda x: 3*np.sin(np.pi/L*x)
    L = 5
    M = 5
    delta_x = 0.1
    delta_y = 0.1
    x_range, y_range, u = get_num_sol(delta_x, delta_y, L, M, g, f)

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