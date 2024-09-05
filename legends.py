import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as mpatches

"""
https://matplotlib-org.translate.goog/stable/api/_as_gen/matplotlib.pyplot.legend.html?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=pt-BR#matplotlib.pyplot.legend
https://matplotlib.org/stable/users/explain/axes/legend_guide.html
"""


def legend01():
    fig, ax = plt.subplots()
    ax.set_title("legend01")
    red_patch = mpatches.Patch(color="red", label="The red data")   
    ax.legend(handles=[red_patch], loc="center")

    return plt


def legend02():
    fig, ax = plt.subplots()
    ax.set_title("legend02")
    blue_line = mlines.Line2D(
        [], [], color="blue", marker="*", markersize=15, label="Blue stars"
    )
    ax.legend(handles=[blue_line])

    return plt


def legend03():
    fig, ax_dict = plt.subplot_mosaic(
        [["top", "top"], ["bottom", "BLANK"]], empty_sentinel="BLANK"
    )

    ax_dict["top"].plot([1, 2, 3], label="test1")
    ax_dict["top"].plot([3, 2, 1], label="test2")

    # ax_dict['top'].set_title("chart01")
    ax_dict["top"].legend(
        bbox_to_anchor=(0.0, 1.02, 1.0, 0.102),
        loc="lower left",
        ncols=2,
        mode="expand",
        borderaxespad=0.0,
    )

    ax_dict["bottom"].plot([1, 2, 3], label="test1")
    ax_dict["bottom"].plot([3, 2, 1], label="test2")

    # ax_dict['bottom'].set_title("chart02")
    ax_dict["bottom"].legend(
        bbox_to_anchor=(1.05, 1), loc="upper left", borderaxespad=0.0
    )

    return plt


def legend04():
    fig, axs = plt.subplot_mosaic([["left", "right"]], layout="constrained")
    axs["left"].plot([1, 2, 3], label="test1")
    axs["left"].plot([3, 2, 1], label="test2")

    axs["right"].plot([1, 2, 3], "C2", label="test3")
    axs["right"].plot([3, 2, 1], "C3", label="test4")

    fig.legend(loc="outside upper right")

    return plt


def legend05():
    # ucl = ['upper', 'center', 'lower']
    # lcr = ['left', 'center', 'right']
    fig, ax = plt.subplots(figsize=(6, 4), layout='constrained', facecolor='0.7')

    ax.plot([1, 2], [1, 2], label='TEST')

    for loc in [
            'outside upper left',
            'outside upper center',
            'outside upper right',
            'outside lower left',
            'outside lower center',
            'outside lower right']:
        fig.legend(loc=loc, title=loc)

    fig, ax = plt.subplots(figsize=(6, 4), layout='constrained', facecolor='0.7')
    ax.plot([1, 2], [1, 2], label='test')

    for loc in [
        'outside left upper',
        'outside right upper',
        'outside left lower',
        'outside right lower'
    ]:
        fig.legend(loc=loc, title=loc)

    return plt


def legend06():
    data1, data2, data3, data4 = np.random.randn(4, 100)

    fig, ax = plt.subplots(figsize=(5, 2.7))

    ax.plot(np.arange(len(data1)), data1, label='data1')
    ax.plot(np.arange(len(data2)), data2, label='data2')
    ax.plot(np.arange(len(data3)), data3, 'd', label='data3')
    ax.legend(loc='lower right')

    return plt


if __name__ == "__main__":
    # data = legend01()
    # data = legend02()
    # data = legend03()
    data = legend04()
    # data = legend05()
    # data = legend06()

    data.savefig(os.path.join('charts', "legends.png"), dpi=300)
    data.show()
