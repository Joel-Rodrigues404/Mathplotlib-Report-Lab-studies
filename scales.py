import matplotlib.pyplot as plt
import numpy as np


def scale01():
    data1, data2, data3, data4 = np.random.randn(4, 100)
    fig, axs = plt.subplots(1, 2, figsize=(5, 2.7), layout="constrained")
    xdata = np.arange(len(data1))  # make an ordinal for this
    data = 10**data1
    axs[0].plot(xdata, data)

    axs[1].set_yscale("log")
    axs[1].plot(xdata, data)
    plt.show()


if __name__ == "__main__":
    scale01()
