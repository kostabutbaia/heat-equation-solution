from heateq import *
from numerical import get_num_solution
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter


def create_anim_gif(name: str) -> None:
    fig = plt.figure()
    plt.xlim(0, L)
    plt.ylim(0, b+1)
    plt.grid()
    plt.plot(x_range, [particular_solution(x) for x in x_range], '--')
    frames = get_solution()
    frames_num = get_num_solution(source, u_0, u_L, g, k, delta_x, delta_t)
    l1, = plt.plot([], [], 'k-', label='Real Solution')
    l2, = plt.plot([], [], 'b--', label='Finite Difference Method')
    plt.legend()
    
    writer = PillowWriter(fps=FPS)

    with writer.saving(fig, f'solutions/compare/{name}.gif', 100):
        for i in range(len(frames)):
            l1.set_data(x_range, frames[i])
            l2.set_data(x_range, frames_num[i])
            writer.grab_frame()


if __name__ == '__main__':
    create_anim_gif(NAME)