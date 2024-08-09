perguntas = [{
    'pergunta': 'Quanto é 2+2?',
    'opções': ['1', '2', '3', '4'],
    'resposta': '4',
},
{
    'pergunta': 'Qual é o nome do pai do Isaac Newton?',
    'opções': ['Albert Einstein', 'Galileo Galilei', 'Copernicus'],
    'resposta': 'Copernicus',
},
{
    'pergunta': 'Quanto é 10/2?',
    'opções': ['5', '10', '20', '40'],
    'resposta': '5',
}]

# FUNÇÃO PARA USAR O DICIONÁRIO
qtd_acertos = 0

for pergunta in perguntas:
    print('Pergunta:', pergunta['pergunta'])
    print()
    
    for i, opcao in enumerate(pergunta['opções']):
        print(f'{i}) {opcao}')
    
    escolha = input('Escolha uma opção: ')
    acertou = False

    if escolha.isdigit():
        escolha_int = int(escolha)
        qtd_opcoes = len(pergunta['opções'])

        if escolha_int < qtd_opcoes and pergunta['opções'][escolha_int] == pergunta['resposta']:
            print('Você acertou!')
            qtd_acertos += 1
            acertou = True
        else:
            print('Você errou!')
    else:
        print('Você não digitou um número válido. Tente novamente.')

    print('Resposta correta:', pergunta['resposta'])
    print()
    input('Pressione Enter para continuar...')
    print('-----------------------------------')
    print()

print(f'Você acertou {qtd_acertos} de {len(perguntas)} perguntas.')
