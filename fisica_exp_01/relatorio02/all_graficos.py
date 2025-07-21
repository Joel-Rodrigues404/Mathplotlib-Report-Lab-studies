import numpy as np
import matplotlib.pyplot as plt


# 1. Amplitude vs Período
A_deg = np.array([10, 15, 20, 25, 30], dtype=float)
T_A = np.array([1.559, 1.556, 1.552, 1.555, 1.558], dtype=float)

# 2. Comprimento vs Período
L_cm = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60], dtype=float)
T_L = np.array([0.898, 1.027, 1.140, 1.211, 1.256, 1.345, 1.433, 1.522, 1.538], dtype=float)

# 3. T² vs L
T_squared = T_L ** 2
mean_T = np.mean(T_A)
coeff_T_L = np.polyfit(np.sqrt(L_cm), T_L, 1)
L_range = np.linspace(L_cm.min(), L_cm.max(), 100)
T_fit = coeff_T_L[0] * np.sqrt(L_range) + coeff_T_L[1]

coeff_T2_L = np.polyfit(L_cm, T_squared, 1)
T2_fit = coeff_T2_L[0] * L_range + coeff_T2_L[1]

# ------------------ Gráfico A x T ------------------
plt.figure()
plt.scatter(A_deg, T_A, color='blue', label='Dados experimentais')
plt.axhline(mean_T, color='red', linestyle='--', label='Linha de tendência (T médio)')
plt.xlabel('Amplitude A (graus)')
plt.ylabel('Período T (s)')
plt.title('Gráfico A x T')
plt.legend()
plt.tight_layout()

# ------------------ Gráfico T x L ------------------
plt.figure()
plt.scatter(L_cm, T_L, color='blue', label='Dados experimentais')
plt.plot(L_range, T_fit, color='red', linestyle='--', label='Linha de tendência (ajuste √L)')
plt.xlabel('Comprimento L (cm)')
plt.ylabel('Período T (s)')
plt.title('Gráfico T x L')
plt.legend()
plt.tight_layout()

# ------------------ Gráfico T² x L ------------------
plt.figure()
plt.scatter(L_cm, T_squared, color='blue', label='Dados experimentais')
plt.plot(L_range, T2_fit, color='red', linestyle='--', label='Linha de tendência (ajuste linear)')
plt.xlabel('Comprimento L (cm)')
plt.ylabel('Período T² (s²)')
plt.title('Gráfico T² x L')
plt.legend()
plt.tight_layout()

plt.show()
