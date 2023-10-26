from numerical import get_num_solution
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter

import numpy as np

NAME = 'Exercise_4'
L = 1
b = 5
k = 1
delta_x = 0.1
delta_t = 0.004
t_final = 1
x_range = np.arange(0, L + delta_x, delta_x)
t_range = np.arange(0, t_final + delta_t, delta_t)

def real_solution(x: float, t: float) -> float:
    return (t**2-1)*x + 1 + np.exp(-9*np.pi**2*k*t)*np.sin(3*np.pi*x)+1/(4*np.pi**2*k)**2*(4*np.pi**2*k*t+np.exp(-9*np.pi**2*k*t)-1)*np.sin(2*np.pi*x)

def get_real_solution_at_t(t: float) -> list[float]:
    return [
        real_solution(x,t) for x in x_range
    ]

def get_real_solution() -> list[list[float]]:
    return [
        get_real_solution_at_t(t) for t in t_range
    ]

def create_anim_gif(name: str) -> None:
    fig = plt.figure()
    plt.xlim(0, L)
    plt.ylim(0, b)
    plt.grid()
    frames_num, _ = get_num_solution(
        lambda x, t: t*(np.sin(2*np.pi*x)+2*x),
        lambda t: 1,
        lambda t: t**2,
        lambda x: 1 + np.sin(3*np.pi*x) - x,
        k,
        delta_x,
        delta_t,
        L,
        t_final
    )

    real_frames = get_real_solution()
    print(len(real_frames[0]))
    print(len(frames_num[0]))
    print(len(x_range))
    
    l1, = plt.plot([], [], 'k-', label='Real Solution')
    l2, = plt.plot([], [], 'b--', label='Finite Difference Method')
    plt.legend()
    
    writer = PillowWriter(fps=7)
    
    with writer.saving(fig, f'solutions/compare/{name}.gif', 100):
        for i in range(len(real_frames)):
            l1.set_data(x_range, real_frames[i])
            l2.set_data(x_range, frames_num[i])
            writer.grab_frame()


if __name__ == '__main__':
    create_anim_gif(NAME)