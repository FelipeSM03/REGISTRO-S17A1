import random

numero = random.randint (0, 100)

matriz3 = [[numero for _ in range(3)]for _ in range(3)]

def EXIBIR(matriz3):
    print("  0 1 2")
    for linha in range(3):
        print(linha, end=' ')
        for coluna in range(3):
            print(matriz3[linha][coluna], end=' ')
        print()
        
EXIBIR(matriz3)    






