# Estrutura de Repetição - While

print(f"\nTabuada Dinâmica\n") # Título
num = int(input('\nNúmero da tabuada: ')) # início
print(f"\nTabuada do número {num}")

i = 1
result = num
while(i <= 10):
    print (f"{num} x {i} = {result}")
    i += 1
    result = num * i
print('\nFim da Tabuada!\n')