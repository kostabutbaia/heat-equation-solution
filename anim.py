from heateq import *
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter


def create_anim_gif(name: str) -> None:
    fig = plt.figure()
    plt.xlim(0, L)
    plt.ylim(0, b+1)
    plt.grid()
    plt.plot(x_range, [particular_solution(x) for x in x_range], '--')
    frames = get_solution()
    l, = plt.plot([], [], 'k-')
    
    writer = PillowWriter(fps=FPS)

    with writer.saving(fig, f'solutions/{name}.gif', 100):
        for frame in frames:
            l.set_data(x_range, frame)
            writer.grab_frame()


if __name__ == '__main__':
    create_anim_gif(NAME)