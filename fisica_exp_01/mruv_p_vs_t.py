import matplotlib.pyplot as plt
import numpy as np

# Dados MRUV
tempos_mruv = np.array([0.441, 0.648, 0.764, 0.831])
posicoes_mruv = np.array([0.450, 0.650, 0.800, 0.900])

# Ajuste quadrático
coef_mruv = np.polyfit(tempos_mruv, posicoes_mruv, 2)
parab_mruv = np.poly1d(coef_mruv)

t_plot = np.linspace(0.4, 0.85, 100)

plt.figure()
plt.scatter(tempos_mruv, posicoes_mruv, color='green', label='Dados')
plt.plot(t_plot, parab_mruv(t_plot), color='orange', linestyle='--',
         label=f'Ajuste Quadrático\nx = {coef_mruv[0]:.3f}t² + {coef_mruv[1]:.3f}t + {coef_mruv[2]:.3f}')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.title('MRUV - Posição vs Tempo')
plt.legend()
plt.grid(True)
plt.show()
