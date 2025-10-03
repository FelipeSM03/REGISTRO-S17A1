matriz2 = [['x' for _ in range(3)] for _ in range(3)]

def EXIBIR(matriz2):
    print("  0 1 2")
    for linha in range(3):
        print(linha, end=' ')
        for coluna in range(3):
            print(matriz2[linha][coluna], end=' ')
        print()
        
EXIBIR(matriz2)    
     













