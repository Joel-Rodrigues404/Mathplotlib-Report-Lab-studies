import matplotlib.pyplot as plt
import numpy as np
import os

data1, data2, data3, data4 = np.random.randn(4, 100)
fig, ax = plt.subplots(figsize=(5, 2.7))
ax.plot(data1, "o", label="data1")
ax.plot(data2, "d", label="data2")
ax.plot(data3, "v", label="data3")
ax.plot(data4, "s", label="data4")
ax.legend()

plt.savefig(os.path.join('charts', "scatter_chart.png"), dpi=300)
plt.show()
