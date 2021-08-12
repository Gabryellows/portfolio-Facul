import random # Módulo que contêm a função que irá randomizar o sorteio..


def anuncio(s1):  # Função criada para anúnciar de forma personalizada o sorteio.
    tam = len(s1)
    if tam:
        print('+', '-' * tam, '+')
        print('|', s1, '|')
        print('+', '-' * tam, '+')

# Uso da função criada para personalizar as boas vinda do sorteio.
anuncio('         *SEJA BEM-VINDO*        ')
anuncio('               AO                ')
anuncio('      *SORTEIO BENEFICENTE*      ')
anuncio('   * CANAL  DO  LENHADORZINHO *  ')

participantes = []  # Variável com a atribuição de lista
while True:
    participar = int(input('Digite "1" se deseja participar do sorteio ou "0" para sair: '))
    if participar == 1: # Condição que testa a entrada do usuário para participar do sorteio ou não.
        nome = input('Digite seu nome: ')
        valor = int(input('Deseja doar quanto?R$'))
        # laço de repetição que serve para verificar se o número é menor que 10, caso seja true,
        # é pedido para o usuário digitar um novo valor.
        while valor < 10:
            # função que informa o usuário do valor mínimo de doação.
            print('O valor de doação para participar do sorteio é de no mínimo R$10')
            valor = int(input('Deseja doar quanto?R$'))
        # Se a condição for satisfeita tanto de primeira quanto pelo laço,
        # é notificado para o usuário seu nome e valor doado.
        print('Parabéns {}, você doou R${}! Obrigado e boa sorte!'.format(nome, valor))
        # laço de repetição que pega o valor doado e faz uma divisão um núm. inteiro, no caso o 10.
        for i in range(valor // 10):
            # caso o valor seja igual ou maior que 10 o nome do participante entra automaticamente na lista,
            # sendo repetido conforme o valor inteiro doado.
            if valor >= 10:
                participantes.append(nome)  # manda o nome do usuário para a lista do sorteio.
    if not participar:
        random.shuffle(participantes)  # Função do próprio python para misturar a ordem da lista.
        # Mostra na tela os participantes e quantas vezes seus nomes aparecem conforme o valor doado.
        print('Participantes: ', participantes)
        ganhador = random.choice(participantes)  # Função do próprio python para sortear o ganhador de forma aleatória.
        print('E o ganhador é... {}! Parabéns e obrigado por participar.'.format(ganhador))  # Anúncia quem ganhou.
        break