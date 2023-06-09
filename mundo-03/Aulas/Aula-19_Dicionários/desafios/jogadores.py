from unidecode import unidecode

jogadores = []
ficha = {}
gols = []

while True:
    ficha['nome'] = str(input('Nome do Jogador: ')).strip().title()
    quantidade = int(input(f'Quantas partidas {ficha["nome"]} jogou? '))

    for c in range(0, quantidade):
        partida = int(input(f'Quantos gols na partida {c + 1}? '))
        gols.append(partida)
    ficha['gols'] = gols[:]

    total = 0
    for g in gols:
        total += g
    ficha['total de gols'] = total

    jogadores.append(ficha.copy())
    ficha.clear()
    gols.clear()

    continuar = ''
    while continuar not in ['S', 'N']:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 35)
print(f'{"Cód":<4}{"Nome":<10}{"Gols":<10}{"Total":>13}')
print('-' * 35)
for c, j in enumerate(jogadores):
    print(f'{c:>3}{j["nome"]:>8}   {str(j["gols"]):<8}{j["total de gols"]:>10}')
print('-' * 35)

while True:
    pesquisa = str(input('Mostrar dados de qual jogador? ')).strip().title()

    if pesquisa.isnumeric():
        pesquisa = int(pesquisa)

    if pesquisa == 'Para' or pesquisa == 999:
        break

    encontrado = ''
    for i, jog in enumerate(jogadores):
        if isinstance(pesquisa, str):
            if pesquisa == unidecode(jog['nome']):
                print(f'-- LEVANTAMENTO DO JOGADOR {jog["nome"]}:')
                for m, gol in enumerate(jog['gols']):
                    print(f'No jogo {m + 1} fez {gol}')
                    encontrado = True
        elif isinstance(pesquisa, int):
            if pesquisa == i:
                print(f'-- LEVANTAMENTO DO JOGADOR {jog["nome"]}:')
                for m, gol in enumerate(jog['gols']):
                    print(f'No jogo {m + 1} fez {gol}')
                    encontrado = True
    if not encontrado:
        print(f'ERRO! Não existe jogador {pesquisa}! Tente novamente')
    print('-' * 35)
print('<< VOLTE SEMPRE >>')
