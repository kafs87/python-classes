# Estrutura de Repetição - For

# Lista
nomes = ['Samuel', 'Franscisco', 'Kauan', 'Lucas', 'Heloise', 'Nicole', 'Bianca', 'Arthur', 'Thales', 'João']

print(f"\nLista de nomes\n") # Título
print('-' * 20) # Cabeçalho
for i in range(len(nomes)):
    print(f'\n{i} - {nomes[i]}\n')