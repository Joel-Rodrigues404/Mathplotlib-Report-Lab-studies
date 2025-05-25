import matplotlib.pyplot as plt


import matplotlib.pyplot as plt
import numpy as np
# import pandas as pd

# Dados da Tabela 1 (Amplitude x Período)
amplitude = np.array([10, 15, 20, 25, 30])
T_amp = np.array([1.559, 1.556, 1.552, 1.555, 1.558])

# Dados da Tabela 2 (Comprimento x Período)
comprimento = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60]) / 100  # converter para metros
T_len = np.array([0.898, 1.027, 1.140, 1.211, 1.256, 1.345, 1.433, 1.522, 1.538])

# Dados da Tabela 3 (Massa x Período)
massa = np.array([14, 31, 97])
T_mass = np.array([1.544, 1.559, 1.561])

# Análise de dependência (com correlação)
print("Correlação T vs Amplitude:", np.corrcoef(amplitude, T_amp)[0,1])
print("Correlação T vs Comprimento:", np.corrcoef(comprimento, T_len)[0,1])
print("Correlação T vs Massa:", np.corrcoef(massa, T_mass)[0,1])

plt.plot(amplitude, T_amp, 'o-', label='Dados experimentais')
plt.xlabel("Amplitude (graus)")
plt.ylabel("Período T (s)")
plt.title("Amplitude vs Período")
plt.grid(True)
plt.legend()
plt.show()

T_medio = np.mean(T_amp)
erros = np.abs(T_amp - T_medio)
print("Período médio:", T_medio)
print("Erros:", erros)
