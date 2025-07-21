import matplotlib.pyplot as plt
import numpy as np


# Dados MRU
tempos_mru = np.array([0.222, 0.446, 0.893, 1.344])
posicoes_mru = np.array([0.450, 0.550, 0.750, 0.950])

# Ajuste linear
coef_mru = np.polyfit(tempos_mru, posicoes_mru, 1)
reta_mru = np.poly1d(coef_mru)

plt.figure()
plt.scatter(tempos_mru, posicoes_mru, color='blue', label='Dados')
plt.plot(tempos_mru, reta_mru(tempos_mru), color='red', linestyle='--',
         label=f'Ajuste Linear\nx = {coef_mru[0]:.3f}t + {coef_mru[1]:.3f}')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.title('MRU - Posição vs Tempo')
plt.legend()
plt.grid(True)
plt.show()
