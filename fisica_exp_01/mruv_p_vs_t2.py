import matplotlib.pyplot as plt
import numpy as np

tempos_mruv = np.array([0.441, 0.648, 0.764, 0.831])
posicoes_mruv = np.array([0.450, 0.650, 0.800, 0.900])

tempos2_mruv = tempos_mruv ** 2

# Ajuste linear
coef_mruv_t2 = np.polyfit(tempos2_mruv, posicoes_mruv, 1)
reta_t2 = np.poly1d(coef_mruv_t2)

plt.figure()
plt.scatter(tempos2_mruv, posicoes_mruv, color='purple', label='Dados')
plt.plot(tempos2_mruv, reta_t2(tempos2_mruv), color='black', linestyle='--',
         label=f'Ajuste Linear\nx = {coef_mruv_t2[0]:.3f}t² + {coef_mruv_t2[1]:.3f}')
plt.xlabel('Tempo² (s²)')
plt.ylabel('Posição (m)')
plt.title('MRUV - Posição vs Tempo²')
plt.legend()
plt.grid(True)
plt.show()
