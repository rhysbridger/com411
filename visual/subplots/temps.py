import matplotlib.pyplot as plt


def read_data(file_path):

    temps = []

    with open(file_path) as file:
        for line in file:
            temps.append(float(line.strip()))

    return temps

def run():
    data = read_data("temps.txt")
    fig, axs = plt.subplot(1, 2, sharey="row")

    days = range(1, 8)

    axs[0].plot(days, data)
    axs[1].bar(days, data)

    axs[0].set_xlin(min(days), max(days))
    axs[1].set_xlin(min(days), max(days))

    axs[0].set_xlabel("Day")
    axs[0].set_ylabel("Temperature")
    axs[1].set_xlabel("Day")

    plt.tight_layout()
    plt.show()


run()