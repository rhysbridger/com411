import matplotlib.pylot as plt
import matplotlib.animation as animation

def animate(frame):
    print(f'frame : {frame}')

    fig, ax = plt.subplots()

    simple_animation = animation.FuncAnimation (fig, animate, frames = 10, interval = 100)

    plt.show()