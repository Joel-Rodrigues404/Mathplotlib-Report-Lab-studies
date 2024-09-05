import matplotlib.pyplot as plt
import numpy as np
import os

linestyle_str = [
    ("solid", "solid"),  # Same as (0, ()) or '-'
    ("dotted", "dotted"),  # Same as (0, (1, 1)) or ':'
    ("dashed", "dashed"),  # Same as '--'
    ("dashdot", "dashdot"),
]  # Same as '-.'

linestyle_tuple = [
    ("loosely dotted", (0, (1, 10))),
    ("dotted", (0, (1, 1))),
    ("densely dotted", (0, (1, 1))),
    ("long dash with offset", (5, (10, 3))),
    ("loosely dashed", (0, (5, 10))),
    ("dashed", (0, (5, 5))),
    ("densely dashed", (0, (5, 1))),
    ("loosely dashdotted", (0, (3, 10, 1, 10))),
    ("dashdotted", (0, (3, 5, 1, 5))),
    ("densely dashdotted", (0, (3, 1, 1, 1))),
    ("dashdotdotted", (0, (3, 5, 1, 5, 1, 5))),
    ("loosely dashdotdotted", (0, (3, 10, 1, 10, 1, 10))),
    ("densely dashdotdotted", (0, (3, 1, 1, 1, 1, 1))),
]


def plot_linestyles(ax, linestyles, title):
    X, Y = np.linspace(0, 100, 10), np.zeros(10)
    yticklabels = []

    for i, (name, linestyle) in enumerate(linestyles):
        ax.plot(X, Y + i, linestyle=linestyle, linewidth=1.5, color="black")
        yticklabels.append(name)

    ax.set_title(title)
    ax.set(
        ylim=(-0.5, len(linestyles) - 0.5),
        yticks=np.arange(len(linestyles)),
        yticklabels=yticklabels,
    )
    ax.tick_params(left=False, bottom=False, labelbottom=False)
    ax.spines[:].set_visible(False)

    for i, (name, linestyle) in enumerate(linestyles):
        ax.annotate(
            repr(linestyle),
            xy=(0.0, i),
            xycoords=ax.get_yaxis_transform(),
            xytext=(-6, -12),
            textcoords="offset points",
            color="blue",
            fontsize=8,
            ha="right",
            family="monospace",
        )
    
    return plt


fig, (ax0, ax1) = plt.subplots(2, 1, figsize=(10, 8), height_ratios=[1, 3])

data = plot_linestyles(ax0, linestyle_str[::-1], title="Named linestyles")
data = plot_linestyles(ax1, linestyle_tuple[::-1], title="Parametrized linestyles")

data.tight_layout()

data.show()
data.savefig(os.path.join('charts', "line_styles.png"), dpi=300)
