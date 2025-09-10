import random




minha_lista = [10, 20, 30, 40, 50]
print(minha_lista)



print(minha_lista[3])


print(minha_lista[-1])



nomes = [] 

while True:
    nome_digitado = input("Digite um nome (ou 'sair' para finalizar): ")
    if nome_digitado.lower() == 'sair':
        break 
nomes.append(nome_digitado)
print("\nLista de nomes:")
for nome in nomes:
    print(nome)
    
    





lista_aleatoria = [random.randint(1, 100) for _ in range(5)]

print(lista_aleatoria)




lista_original = []
while True:
    try:
        num = int(input("Digite um número inteiro (ou 0 para terminar): "))
        if num == 0:
            break
        lista_original.append(num)
    except ValueError:
        print("Por favor, insira um número inteiro válido.")
print("\nLista invertida:")
for elemento in reversed(lista_original):
    print(elemento)
    





