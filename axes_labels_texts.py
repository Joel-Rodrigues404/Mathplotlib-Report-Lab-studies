import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 115, 15
x = mu + sigma * np.random.randn(10000)
fig, ax = plt.subplots(figsize=(5, 2.7), layout="constrained")
# the histogram of the data
n, bins, patches = ax.hist(x, 50, density=True, facecolor="C0", alpha=0.75)

ax.set_xlabel("Eixo x label: Length [cm]")
ax.set_ylabel("Eixo y label: Probability")
ax.set_title("titulo: Aardvark lengths\n (not really)")
ax.text(75, 0.025, r"$\mu=115,\ \sigma=15$")
ax.axis([55, 175, 0, 0.03])
ax.grid(True)  # linhas que forma a grade
ax.annotate(
    text="anootate",
    xy=(100, 0.02),
    xytext=(60, 0.025),
    arrowprops=dict(facecolor="black", shrink=0.05),
)
ax.set_ylim(0, 0.03)
plt.show()
