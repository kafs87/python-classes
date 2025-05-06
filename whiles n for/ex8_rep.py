# Estrutura de Repetição - For

# Lista
cidades_SP = ['Arujá', 'Biritiba Mirim', 'Ferraz de Vasconcelos', 'Guararema', 'Guarulhos', 'Itaquaquecetuba', 'Mogi das Cruzes', 'Poá', 'Salesópolis', 'Santa Isabel',  'Suzano']

cidades_SP.sort(reverse=True) # sort -> Ordena a lista, reverse -> Deixa a lista ao contrário

print(f"\nCidades do Alto Tietê\n") # Título

print('-' * 20) # Cabeçalho
for cidade in cidades_SP: # cidade -> contador
    print(f' - {cidade}')