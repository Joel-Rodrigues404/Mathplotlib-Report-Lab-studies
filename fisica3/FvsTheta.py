import matplotlib.pyplot as plt
import numpy as np

# 1. Definindo as constantes (Valores fixos)
q = 1.6e-19     # Carga
v = 3e5         # Velocidade
B = 1.0         # Campo Magnético

# 2. Criando os dados do Ângulo (Eixo X)
# Variando de 0 a 180 graus
theta_graus = np.linspace(0, 180, 200)

# 3. Calculando a Força (Eixo Y)
# O numpy precisa do ângulo em radianos para calcular o seno
theta_rad = np.radians(theta_graus)
F_valores = q * v * B * np.sin(theta_rad)

# 4. Gerando o Gráfico
plt.figure(figsize=(8, 6))
plt.plot(theta_graus, F_valores, color='purple', linewidth=2.5)

# Adicionando marcadores visuais para pontos importantes
ponto_max = np.max(F_valores)
plt.scatter([0, 90, 180], [0, ponto_max, 0], color='black', zorder=5)
plt.text(90, ponto_max, ' Máximo (90°)', verticalalignment='bottom')

plt.title('Força Magnética vs. Ângulo θ', fontsize=14)
plt.xlabel('Ângulo θ (Graus)', fontsize=12)
plt.ylabel('Magnitude da Força F (Newtons)', fontsize=12)

# Definindo os "ticks" do eixo X para mostrar ângulos chave
plt.xticks([0, 30, 45, 60, 90, 120, 135, 150, 180])
plt.grid(True, linestyle='--', alpha=0.7)

plt.show()
