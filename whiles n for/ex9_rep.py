# Estrutura de Repetição - For

print(f"\nTabuada Dinâmica\n") # Título
num = int(input('\nNúmero da tabuada: ')) # início
print(f"\nTabuada do número {num}")

operacao = 1
resultado = num
for operacao in range(1, 11):
    print (f"{num} x {operacao} = {resultado}")
    operacao += 1
    resultado = num * operacao
print('\nFim da Tabuada!\n')