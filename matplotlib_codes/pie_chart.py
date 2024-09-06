import matplotlib.pyplot as plt
import os


found = {"Label1": 60, "Label2": 40}

dirpath = "charts/"

export_charts = True

plt.clf()

plt.figure(figsize=[15, 7])

text_prop = {
    "fontsize": 20,
    "fontweight": "heavy",
    "color": "black",
}

plt.pie(
    found.values(),
    wedgeprops={"edgecolor": "white", "linewidth": 5, "antialiased": True},
    textprops=text_prop,
    colors=["#DC1215", "#07C136"],
    startangle=90,
    autopct="%.1f%%",
    pctdistance=1.3,
)

plt.legend(
    labels=found.keys(), loc="best", bbox_to_anchor=(0.0, 0.2), ncol=1, fontsize=16
)

centre_circle = plt.Circle((0, 0), 0.60, fc="white")
fig = plt.gcf()
fig.gca().add_artist(centre_circle)


if export_charts:
    plt.savefig(os.path.join(dirpath, "pie_chart.png"), dpi=118)
else:
    plt.show()
