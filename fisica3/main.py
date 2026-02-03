import matplotlib.pyplot as plt
import numpy as np

# Configuração do estilo dos gráficos para ficar bonito
plt.style.use('seaborn-v0_8-whitegrid')

# Definindo constantes para os experimentos (valores arbitrários para exemplo)
q_const = 1.6e-19  # Carga elementar
v_const = 2e5      # Velocidade (200.000 m/s)
B_const = 0.5      # Campo magnético (0.5 Tesla)
theta_const_rad = np.pi / 2  # 90 graus (para força máxima nos outros gráficos)

# --- Criação da figura com 4 subplots (2x2) ---
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Análise Gráfica da Força Magnética: F = |q|vBsen(θ)', fontsize=16)

# ---------------------------------------------------------
# Gráfico 1: F vs q (Força vs Carga)
# Mantendo v, B e theta constantes.
# ---------------------------------------------------------
# Criando dados para q (de 0 a 5 vezes a carga elementar)
q_data = np.linspace(0, 5 * q_const, 100)
# Calculando F (Relação linear: y = mx)
F_vs_q = q_data * v_const * B_const * np.sin(theta_const_rad)

axs[0, 0].plot(q_data, F_vs_q, color='blue', linewidth=2)
axs[0, 0].set_title('F vs. q (v, B, θ constantes)')
axs[0, 0].set_xlabel('Carga q (Coulombs)')
axs[0, 0].set_ylabel('Força Magnética F (Newtons)')
axs[0, 0].annotate('Relação Linear', xy=(q_data[50], F_vs_q[50]), 
                   xytext=(q_data[20], F_vs_q[70]),
                   arrowprops=dict(facecolor='black', shrink=0.05))


# ---------------------------------------------------------
# Gráfico 2: F vs v (Força vs Velocidade)
# Mantendo q, B e theta constantes.
# ---------------------------------------------------------
# Criando dados para velocidade v (de 0 a 1 milhão m/s)
v_data = np.linspace(0, 1e6, 100)
# Calculando F (Relação linear)
F_vs_v = q_const * v_data * B_const * np.sin(theta_const_rad)

axs[0, 1].plot(v_data, F_vs_v, color='red', linewidth=2)
axs[0, 1].set_title('F vs. v (q, B, θ constantes)')
axs[0, 1].set_xlabel('Velocidade v (m/s)')
axs[0, 1].set_ylabel('Força Magnética F (Newtons)')


# ---------------------------------------------------------
# Gráfico 3: F vs B (Força vs Campo Magnético)
# Mantendo q, v e theta constantes.
# ---------------------------------------------------------
# Criando dados para campo B (de 0 a 2 Tesla)
B_data = np.linspace(0, 2, 100)
# Calculando F (Relação linear)
F_vs_B = q_const * v_const * B_data * np.sin(theta_const_rad)

axs[1, 0].plot(B_data, F_vs_B, color='green', linewidth=2)
axs[1, 0].set_title('F vs. B (q, v, θ constantes)')
axs[1, 0].set_xlabel('Campo Magnético B (Tesla)')
axs[1, 0].set_ylabel('Força Magnética F (Newtons)')


# ---------------------------------------------------------
# Gráfico 4: F vs theta (Força vs Ângulo)
# Mantendo q, v e B constantes.
# ---------------------------------------------------------
# Criando dados para o ângulo (de 0 a 180 graus, em radianos)
theta_rad_data = np.linspace(0, np.pi, 200)
# Convertendo para graus apenas para o eixo X ficar legível
theta_deg_data = np.degrees(theta_rad_data)
# Calculando F (Relação senoidal)
F_vs_theta = q_const * v_const * B_const * np.sin(theta_rad_data)

axs[1, 1].plot(theta_deg_data, F_vs_theta, color='purple', linewidth=2)
axs[1, 1].set_title('F vs. θ (q, v, B constantes)')
axs[1, 1].set_xlabel('Ângulo θ (Graus)')
axs[1, 1].set_ylabel('Força Magnética F (Newtons)')
# Marcando o ponto máximo
max_F = np.max(F_vs_theta)
axs[1, 1].scatter([90], [max_F], color='black', zorder=5)
axs[1, 1].annotate('Máximo a 90° (senθ=1)', xy=(90, max_F), 
                   xytext=(110, max_F*0.8),
                   arrowprops=dict(facecolor='black', shrink=0.05))
axs[1, 1].set_xticks([0, 45, 90, 135, 180])


# Ajustar o layout e mostrar
plt.tight_layout()
print("Gerando gráficos... Uma janela será aberta com as imagens.")
plt.show()
