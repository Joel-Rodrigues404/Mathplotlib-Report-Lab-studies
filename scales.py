import matplotlib.pyplot as plt
import numpy as np
import os


def scale01():
    data1, data2, data3, data4 = np.random.randn(4, 100)
    fig, axs = plt.subplots(1, 2, figsize=(5, 2.7), layout="constrained")
    xdata = np.arange(len(data1))
    data = 10**data1
    axs[0].plot(xdata, data)

    axs[1].set_yscale("log")
    axs[1].plot(xdata, data)

    return plt


if __name__ == "__main__":
    data = scale01()

    data.savefig(os.path.join('charts', "scales.png"), dpi=300)
    data.show()
