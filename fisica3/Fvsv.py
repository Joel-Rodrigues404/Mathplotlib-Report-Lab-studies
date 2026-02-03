import matplotlib.pyplot as plt
import numpy as np

# 1. Definindo as constantes (Valores fixos)
q = 1.6e-19     # Carga de um próton
B = 2.0         # Campo Magnético: 2.0 Tesla
theta = 90      # Ângulo: 90 graus

# 2. Criando os dados da Velocidade (Eixo X)
# Variando de 0 a 1 milhão de m/s
v_valores = np.linspace(0, 1e6, 100)

# 3. Calculando a Força (Eixo Y)
# Equação: F = q * v * B * sen(theta)
theta_rad = np.radians(theta)
F_valores = q * v_valores * B * np.sin(theta_rad)

# 4. Gerando o Gráfico
plt.figure(figsize=(8, 6))
plt.plot(v_valores, F_valores, color='red', linewidth=2.5)

plt.title(f'Força Magnética vs. Velocidade (q={q:.1e} C, B={B} T)', fontsize=14)
plt.xlabel('Velocidade v (m/s)', fontsize=12)
plt.ylabel('Força Magnética F (Newtons)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

plt.show()
