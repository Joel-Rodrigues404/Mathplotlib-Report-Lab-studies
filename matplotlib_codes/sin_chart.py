import matplotlib.pyplot as plt
import numpy as np
import os

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

plt.savefig(os.path.join('charts', "sin_chart.png"), dpi=300)
plt.show()
