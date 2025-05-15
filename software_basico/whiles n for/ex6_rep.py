# Estrutura de Repetição - For
print(f"\nLista de números - Dinâmica \n\n") # Título

ini = int(input("Início: "))
fim = int(input("Fim: "))
step = int(input("Salto: "))

for num in range(ini, fim, step):
    print(f'Contador: {num}')
else:
    print(f'Fim da Repetição!')