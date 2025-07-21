import matplotlib.pyplot as plt
import numpy as np

# === QUESTÃO 2 ===
# Gráfico de A x T (Amplitude vs Período)
A_cm = np.array([1, 2, 3, 4, 5])
T1 = np.array([0.829, 0.827, 0.835, 0.830, 0.833])

plt.figure(figsize=(6, 4))
plt.plot(A_cm, T1, 'o', color='orange')
coef_amp = np.polyfit(A_cm, T1, 1)
plt.plot(A_cm, np.polyval(coef_amp, A_cm), 'k--')
plt.title("Amplitude A (cm) vs Período T (s)")
plt.xlabel("Amplitude A (cm)")
plt.ylabel("Período T (s)")
plt.grid(True)
plt.tight_layout()
plt.show()

# === QUESTÃO 3 ===
# Gráfico de T x m (massa vs período) - Tabela 2
massa_g_2 = np.array([50, 100, 150, 200])
T2 = np.array([0.650, 0.835, 0.996, 1.123])

plt.figure(figsize=(6, 4))
plt.plot(massa_g_2, T2, 'o', color='orange')
coef_T2 = np.polyfit(massa_g_2, T2, 1)
plt.plot(massa_g_2, np.polyval(coef_T2, massa_g_2), 'k--')
plt.title("Período T vs Massa (g) - Tabela 2")
plt.xlabel("Massa (g)")
plt.ylabel("Período T (s)")
plt.grid(True)
plt.tight_layout()
plt.show()

# === QUESTÃO 4 ===
# Gráfico de T² x m (massa vs período ao quadrado) - Tabela 2
T2_squared = T2**2

plt.figure(figsize=(6, 4))
plt.plot(massa_g_2, T2_squared, 'o', color='orange')
coef_T2sq = np.polyfit(massa_g_2, T2_squared, 1)
plt.plot(massa_g_2, np.polyval(coef_T2sq, massa_g_2), 'k--')
plt.title("Período² T² vs Massa (g) - Tabela 2")
plt.xlabel("Massa (g)")
plt.ylabel("T² (s²)")
plt.grid(True)
plt.tight_layout()
plt.show()
