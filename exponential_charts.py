# Bibliotecas Importadas
import matplotlib.pyplot as plt
import numpy as np

# Gerando os dados do eixo x para serem plotados
x = np.arange(0, 5, 0.1)

# Gerando os dados do eixo Y para serem plotados
y1 = x**2
y2 = x**5

# Usando o plt.subplots() para plotar varios gráficos em uma mesma figura.
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(8, 4))
plt.suptitle("Gráficos com Subplots")
plt.subplots_adjust(
    left=0.093,
    right=0.948,
    top=0.8,
    bottom=0.148,
    wspace=0.348,
    hspace=0.824
)

# Plotando os gráficos nos diferentes Axes e configurando.
ax1.plot(x, y1)
ax1.set_title("Função do Segundo Grau $x^2$")
ax1.set_xlabel("Tempo")
ax1.set_ylabel("Amplitude")
ax1.grid(True)

ax2.plot(x, y2)
ax2.set_title("Função do Terceiro Grau $x^3$")
ax2.set_xlabel("Tempo")
ax2.set_ylabel("Amplitude")
ax2.grid(True)

ax3.plot(x, y1)
ax3.set_title("Função do Quarto Grau $x^4$")
ax3.set_xlabel("Tempo")
ax3.set_ylabel("Amplitude")
ax3.grid(True)

ax4.plot(x, y2)
ax4.set_title("Função do Quinto Grau $x^5$")
ax4.set_xlabel("Tempo")
ax4.set_ylabel("Amplitude")
ax4.grid(True)

plt.show()
