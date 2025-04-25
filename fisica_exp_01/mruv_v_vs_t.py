import matplotlib.pyplot as plt
import numpy as np

tempos_mruv = np.array([0.441, 0.648, 0.764, 0.831])
posicoes_mruv = np.array([0.450, 0.650, 0.800, 0.900])

velocidades_inst = np.array([0.680, 1.080, 1.308, 1.444])

# Ajuste linear
coef_vt = np.polyfit(tempos_mruv, velocidades_inst, 1)
reta_vt = np.poly1d(coef_vt)

plt.figure()
plt.scatter(tempos_mruv, velocidades_inst, color='brown', label='Dados')
plt.plot(tempos_mruv, reta_vt(tempos_mruv), color='blue', linestyle='--',
         label=f'Ajuste Linear\nv = {coef_vt[0]:.3f}t + {coef_vt[1]:.3f}')
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (m/s)')
plt.title('MRUV - Velocidade vs Tempo')
plt.legend()
plt.grid(True)
plt.show()
