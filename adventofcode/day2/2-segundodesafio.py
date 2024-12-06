arquivo = '/home/pintermaciel/code/adventofcode/adventofcode/day2/input.txt'

with open(arquivo, "r") as file:
    data = [
        line.split() for line in file if line.strip()
        ]

def relatorio_seguro(nivel):
    crescente = all(1 <= nivel[i+1] - nivel[i] <= 3 for i in range(len(nivel)-1))
    decrescente = all(1 <= nivel[i] - nivel[i+1] <= 3 for i in range(len(nivel)-1))
    return crescente or decrescente

def contagem_segura(nivel):
    contador = 0
    for relatorio in data:
        nivel = list(map(int, relatorio))
        if relatorio_seguro(nivel) or remove_nivel(nivel):
            contador += 1
    return contador

def remove_nivel(nivel):
    for i in range(len(nivel)):
        novo_nivel = nivel[:i] + nivel[i+1:]
        if relatorio_seguro(novo_nivel):
            return True
    return False

print(
    f"Numero de relatorios seguros: {contagem_segura(data)}"
    )