
import matplotlib.pyplot as plt
import numpy as np
# === QUESTÃO 4 ===
# Gráfico de T² x m (massa vs período ao quadrado) - Tabela 2
massa_g_2 = np.array([50, 100, 150, 200])
T2 = np.array([0.650, 0.835, 0.996, 1.123])
T2_squared = T2**2

plt.figure(figsize=(6, 4))
plt.plot(massa_g_2, T2_squared, 'o', color='red')
coef_T2sq = np.polyfit(massa_g_2, T2_squared, 1)
plt.plot(massa_g_2, np.polyval(coef_T2sq, massa_g_2), 'k--')
plt.title("Período² T² vs Massa (g) - Tabela 2")
plt.xlabel("Massa (g)")
plt.ylabel("T² (s²)")
plt.grid(True)
plt.tight_layout()
plt.show()
