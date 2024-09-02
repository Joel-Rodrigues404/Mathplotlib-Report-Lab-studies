import matplotlib.pyplot as plt

import numpy as np

"""
    ['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']
"""


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

    plt.show()


def linear_chart1():
    fig, ax = plt.subplots()
    x = []
    y = []

    for _ in range(10):
        x.append(_)
        y.append(_ * 3)

    print(x, y)
    ax.plot(x, y)

    plt.show()


def lienar_chart2():
    fig, ax = plt.subplots()

    ax.plot([2, 3, 6, 1], [1, 4, 8, 9], color="orange", linewidth=4, linestyle="--")
    ax.plot([1, 2, 5, 6], [1, 4, 8, 2], color="red", linewidth=4, linestyle="--")

    plt.show()


def lienar_chart3():
    fig = plt.figure()  # an empty figure with no Axes
    fig, ax = plt.subplots()  # a figure with a single Axes
    fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
    # a figure with one Axes on the left, and two on the right:
    fig, axs = plt.subplot_mosaic([["left", "right_top"], ["left", "right_bottom"]])
    plt.show()


def lienar_chart4():
    x = np.linspace(0, 2, 100)  # Sample data.

    # Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
    fig, ax = plt.subplots(figsize=(5, 2.7), layout="constrained")
    ax.plot(x, x, label="linear")  # Plot some data on the Axes.
    ax.plot(x, x**2, label="quadratic")  # Plot more data on the Axes...
    ax.plot(x, x**3, label="cubic")  # ... and some more.
    ax.set_xlabel("x label")  # Add an x-label to the Axes.
    ax.set_ylabel("y label")  # Add a y-label to the Axes.
    ax.set_title("Simple Plot")  # Add a title to the Axes.
    ax.legend()  # Add a legend.
    plt.show()


def lienar_chart5():
    ypoints = np.array([3, 8, 1, 10])

    plt.plot(ypoints, marker='o')
    plt.grid()
    plt.show()


if __name__ == "__main__":
    linear_chart0()
    # linear_chart1()
    # lienar_chart2()
    # lienar_chart3()
    # lienar_chart4()
    # lienar_chart5()
