import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import time

# Dados da elipse
theta = np.linspace(0, 2*np.pi, 400)
x = 2 * np.sqrt(2) * np.cos(theta)
y = np.sqrt(2) * np.sin(theta)

# Função do gradiente
def gradiente(x, y):
    return np.array([x/2, 2*y])

# Pontos para a animação
theta_points = np.linspace(0, 2*np.pi, 40)
x_pontos = 2 * np.sqrt(2) * np.cos(theta_points)
y_pontos = np.sqrt(2) * np.sin(theta_points)

# Configuração da figura
fig, ax = plt.subplots(figsize=(6,6))
ax.plot(x, y, color="blue", label="Elipse $x^2/4 + y^2 = 2$")
ax.set_aspect('equal')
ax.set_xlim(-4, 4)
ax.set_ylim(-3, 3)
ax.grid(True, linestyle="--", alpha=0.5)
ax.legend()
ponto, = ax.plot([], [], 'ro')
vetor, = ax.plot([], [], 'g-', lw=2)
titulo = ax.text(-3.5, 2.6, "", fontsize=10, color="black")

# Função de atualização do quadro
def update(frame):
    xp, yp = x_pontos[frame], y_pontos[frame]
    g = gradiente(xp, yp)
    ponto.set_data([xp], [yp])
    vetor.set_data([xp, xp + 0.8*g[0]], [yp, yp + 0.8*g[1]])
    titulo.set_text(f"Ponto ({xp:.2f}, {yp:.2f}) | ∇F = ({g[0]:.2f}, {g[1]:.2f})")
    return ponto, vetor, titulo

ani = animation.FuncAnimation(fig, update, frames=len(theta_points), interval=300, blit=True)
plt.show()
time.sleep(10)
plt.close(fig)
