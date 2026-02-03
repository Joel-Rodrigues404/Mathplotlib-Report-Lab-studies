import matplotlib.pyplot as plt
import numpy as np

# 1. Definindo as constantes (Valores fixos)
q = 1.6e-19     # Carga de um próton
v = 5e5         # Velocidade: 500.000 m/s
theta = 90      # Ângulo: 90 graus

# 2. Criando os dados do Campo Magnético (Eixo X)
# Variando de 0 a 10 Tesla
B_valores = np.linspace(0, 10, 100)

# 3. Calculando a Força (Eixo Y)
# Equação: F = q * v * B * sen(theta)
theta_rad = np.radians(theta)
F_valores = q * v * B_valores * np.sin(theta_rad)

# 4. Gerando o Gráfico
plt.figure(figsize=(8, 6))
plt.plot(B_valores, F_valores, color='green', linewidth=2.5)

plt.title(f'Força Magnética vs. Campo B (q={q:.1e} C, v={v:.0e} m/s)', fontsize=14)
plt.xlabel('Campo Magnético B (Tesla)', fontsize=12)
plt.ylabel('Força Magnética F (Newtons)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

plt.show()
