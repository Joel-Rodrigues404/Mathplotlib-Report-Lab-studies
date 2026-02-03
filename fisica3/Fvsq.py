import matplotlib.pyplot as plt
import numpy as np

# 1. Definindo as constantes (Valores fixos)
v = 3e5         # Velocidade: 300.000 m/s
B = 1.5         # Campo Magnético: 1.5 Tesla
theta = 90      # Ângulo: 90 graus (para sen(90) = 1, força máxima)

# 2. Criando os dados da Carga (Eixo X)
# Vamos variar a carga de 0 até 5 vezes a carga elementar (apenas como exemplo de magnitude)
q_elementar = 1.6e-19
q_valores = np.linspace(0, 5 * q_elementar, 100) 

# 3. Calculando a Força (Eixo Y)
# Equação: F = q * v * B * sen(theta)
theta_rad = np.radians(theta) # Convertendo para radianos para o cálculo
F_valores = q_valores * v * B * np.sin(theta_rad)

# 4. Gerando o Gráfico
plt.figure(figsize=(8, 6))
plt.plot(q_valores, F_valores, color='blue', linewidth=2.5)

plt.title(f'Força Magnética vs. Carga (v={v:.0e} m/s, B={B} T)', fontsize=14)
plt.xlabel('Carga Elétrica q (Coulombs)', fontsize=12)
plt.ylabel('Força Magnética F (Newtons)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# Ajuste para notação científica nos eixos ficarem legíveis
plt.ticklabel_format(style='sci', axis='both', scilimits=(0,0))

plt.show()
