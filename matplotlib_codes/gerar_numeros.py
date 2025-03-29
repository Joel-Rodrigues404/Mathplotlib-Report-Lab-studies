from fractions import Fraction


def gerar_numeros_racionais(n):
    racionais = []
    for denominador in range(1, n + 1):
        for numerador in range(1, denominador + 1):
            fração = Fraction(numerador, denominador)
            if fração not in racionais:  # Verifica se a fração já está na lista
                racionais.append(fração)

    # Ordena a lista de frações
    racionais = sorted(racionais)
    return racionais


# Gerar números racionais até o denominador 14
numeros_racionais = gerar_numeros_racionais(50)

# Imprimir a lista de números racionais na forma de fração, separados por vírgulas
print(", ".join(str(f) for f in numeros_racionais))
