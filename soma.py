# soma.py
def soma(a, b, c=0):
    return a + b + c

def media(a, b, c=0):
    return soma(a, b, c) / 3  # Calcula a média

# Teste das funções
print(soma(5, 3, 2))  # Resultado da soma
print(media(5, 3, 2))  # Resultado da média
