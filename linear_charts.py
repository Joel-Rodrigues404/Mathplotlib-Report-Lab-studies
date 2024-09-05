import matplotlib.pyplot as plt
import numpy as np
import os

"""
    ['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']
"""

dirpath = 'charts'


def linear_chart0():
    # print(plt.style.available)
    # plt.style.use("seaborn-v0_8-paper")

    axis_x_days = [1, 5, 10, 15, 20, 25, 30]
    axis_y_min_temp = [28, 29, 25, 32, 34, 36, 31]
    axis_y_max_temp = [21, 22, 17, 23, 23, 24, 20]

    plt.title('Temperature max and mins')
    plt.xlabel('Days')
    plt.ylabel('Temperature')

    plt.plot(axis_x_days, axis_y_max_temp, linestyle='--', marker='o', color='#00fff0', linewidth=1)
    plt.plot(axis_x_days, axis_y_min_temp, linestyle='--', marker='o', color='#ff0000', linewidth=2)

    plt.legend(['tem max', 'temp min'])
    plt.grid(True)

    return plt


def linear_chart1():
    fig, ax = plt.subplots()
    x, y = []

    for _ in range(10):
        x.append(_)
        y.append(_ * 3)

    ax.plot(x, y)

    return plt


def linear_chart2():
    fig, ax = plt.subplots()

    ax.plot([2, 3, 6, 1], [1, 4, 8, 9], color="orange", linewidth=4, linestyle="--")
    ax.plot([1, 2, 5, 6], [1, 4, 8, 2], color="red", linewidth=4, linestyle="--")

    return plt


def linear_chart3():
    fig = plt.figure()
    fig, ax = plt.subplots()
    fig, axs = plt.subplots(2, 2)
    fig, axs = plt.subplot_mosaic([["left", "right_top"], ["left", "right_bottom"]])

    return plt


def linear_chart4():
    x = np.linspace(0, 2, 100)

    fig, ax = plt.subplots(figsize=(5, 2.7), layout="constrained")

    ax.plot(x, x, label="linear")
    ax.plot(x, x**2, label="quadratic")
    ax.plot(x, x**3, label="cubic")

    ax.set_xlabel("x label")
    ax.set_ylabel("y label")
    ax.set_title("Simple Plot")
    ax.legend()

    return plt


def linear_chart5():
    ypoints = np.array([3, 8, 1, 10])

    plt.plot(ypoints, marker='o')
    plt.grid()

    return plt


if __name__ == "__main__":
    data = linear_chart0()
    # data = linear_chart1()
    # data = linear_chart2()
    # data = linear_chart3()
    # data = linear_chart4()
    # data = linear_chart5()

    data.savefig(os.path.join(dirpath, "linear_charts.png"), dpi=300)
    data.show()
