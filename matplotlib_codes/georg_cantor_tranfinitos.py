import matplotlib.pyplot as plt

# Números naturais
naturais = list(range(1, 101))  # Números naturais de 1 a 100

# Números racionais (definidos explicitamente de acordo com a sequência de Cantor)
racionais = [
    1/1, 1/2, 2/1, 1/3, 3/1, 2/3, 1/4, 4/1, 3/2, 1/5,
    5/1, 2/5, 1/6, 6/1, 5/4, 3/4, 2/7, 1/7, 7/1, 4/3,
    3/5, 5/2, 2/6, 1/8, 8/1, 7/2, 4/5, 3/3, 2/8, 1/9,
    9/1, 8/3, 7/3, 5/3, 4/2, 3/6, 2/9, 1/10, 10/1, 9/2,
    8/5, 7/4, 6/5, 5/5, 4/4, 3/8, 2/10, 1/11, 11/1, 10/2,
    9/3, 8/4, 7/5, 6/6, 5/6, 4/6, 3/9, 2/11, 1/12, 12/1,
    11/2, 10/3, 9/4, 8/5, 7/6, 6/7, 5/7, 4/7, 3/10, 2/12,
    1/13, 13/1, 12/2, 11/3, 10/4, 9/5, 8/6, 7/7, 6/8, 5/8,
    4/8, 3/11, 2/13, 1/14, 14/1, 13/2, 12/3, 11/4, 10/5, 9/6,
    8/7, 7/8, 6/9, 5/9, 4/9, 3/12, 2/14, 1/15, 15/1, 14/2
]

# Ajustando para ter 100 elementos
while len(racionais) < 100:
    racionais.append(float('nan'))  # Preencher com NaN para manter a dimensão

# Criando o gráfico
plt.figure(figsize=(10, 5))
plt.plot(naturais, racionais, marker='o', linestyle='-', color='b')

# Adicionando título e rótulos
plt.title('Números Naturais vs Números Racionais')
plt.xlabel('Números Naturais')
plt.ylabel('Números Racionais')

# Mostrando a grade
plt.grid()

# Exibindo o gráfico
plt.show()
