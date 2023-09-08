produtos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-' * 43)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'* 43)

for pos, p in enumerate(produtos):
    if pos % 2 == 0:
        nomeProduto = p
    else:
        valor = p
        print(f'{nomeProduto:.<30} R${valor:7.2f}')

print('-' * 43)