import matplotlib.pyplot as plt
import numpy as np
import os

mu, sigma = 115, 15
x = mu + sigma * np.random.randn(10000)
fig, ax = plt.subplots(figsize=(5, 2.7), layout="constrained")
n, bins, patches = ax.hist(x, 50, density=True, facecolor="C0", alpha=0.75)

ax.set_xlabel("Eixo x label: Length [cm]")
ax.set_ylabel("Eixo y label: Probability")
ax.set_title("titulo: Aardvark lengths\n (not really)")
ax.text(75, 0.025, r"$\mu=115,\ \sigma=15$")

ax.axis([55, 175, 0, 0.03])
ax.grid(True)
ax.annotate(
    text="anootate",
    xy=(100, 0.02),
    xytext=(60, 0.025),
    arrowprops=dict(facecolor="black", shrink=0.05),
)
ax.set_ylim(0, 0.03)

plt.savefig(os.path.join('charts', "axes_labels_texts.png"), dpi=300)

plt.show()
