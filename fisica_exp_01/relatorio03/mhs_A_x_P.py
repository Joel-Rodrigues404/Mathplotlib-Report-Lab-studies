import matplotlib.pyplot as plt
import numpy as np


# === QUESTÃO 2 ===
# Gráfico de A x T (Amplitude vs Período)
A_cm = np.array([1, 2, 3, 4, 5])
T1 = np.array([0.829, 0.827, 0.835, 0.830, 0.833])
T1_mean = np.mean(T1)

plt.figure(figsize=(6, 4))
plt.plot(A_cm, T1, 'o', color='orange')
plt.axhline(y=T1_mean, color='k', linestyle='--', label=f'T = {T1_mean:.3f} s')
plt.title("Amplitude A (cm) vs Período T (s)")
plt.xlabel("Amplitude A (cm)")
plt.ylabel("Período T (s)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
