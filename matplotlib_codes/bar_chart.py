import matplotlib.pyplot as plt
import os
from random import randint


export_charts = True
dirpath = "charts"


bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange', '#00fff0']
bar_labels = ['red', 'blue', 'red', 'orange', 'blue',
              'red', 'orange', 'blue', 'orange', 'blue']


x = ["algo", "algo2", "algo3", "algo4", "algo5",
     "algo6", "algo7", "algo8", "algo9", "algo10"]
y = [randint(1, 1000) for x in range(10)]


plt.figure(figsize=[15, 10])
plt.bar(x, y, edgecolor="white", color=bar_colors, label=bar_labels)
plt.ylabel("Count", fontsize=20, fontweight='bold')
# plt.xticks(rotation=23, fontweight='bold')
plt.xticks(range(len(x)), rotation=23, fontsize=12,
           color='black', fontweight='bold', ha='center')

plt.legend(title='legenda', loc='upper right', bbox_to_anchor=(1.1, 1.013))


for i in range(len(x)):
    plt.text(i, y[i] + (10 / 100 * 1.5), y[i], ha="center")


if export_charts:
    plt.savefig(os.path.join(dirpath, "bar_chart.png"), dpi=300)
else:
    plt.show()
