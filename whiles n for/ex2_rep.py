# Estrutura de Repetição - While

print(f"\nLista de números - Dinâmica \n\n") # Título

num_inicio = int(input('Número do início da lista: ')) # início
num_final = int(input('Número do fim da lista: ')) # início
num_step = int(input('De quanto em quanto irá? ')) # início

while (num_inicio <= num_final): # fim
    print(f"Contador: {num_inicio}.") # Saída
    num_inicio += num_step # step

print('Fim do Loop!')