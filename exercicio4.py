from operator import itemgetter
#  Lista para armazenar os itens que serão inseridos no dicionario.
armazenamentos = []
#  Dicionario com as tabelas e seus valores solicitados no enunciado.
armazem_1 = {'Código': 3, 'Estoque': 60, 'minimo': 77}
armazem_2 = {'Código': 5, 'Estoque': 75, 'minimo': 50}
armazem_3 = {'Código': 2, 'Estoque': 43, 'minimo': 45}
armazem_4 = {'Código': 3, 'Estoque': 26, 'minimo': 18}
armazem_5 = {'Código': 20, 'Estoque': 35, 'minimo': 20}

active = True
while active:
    # #variavel que pede a entrada do usuario para realizar o programa ou encerrar.
    acss_armazenamento = int(input('Digite 1 para acessar o armazenamento ou 0 para sair: '))
    if acss_armazenamento == 0 or acss_armazenamento != 1:
        active = False
    else:
        print('Entrando no sistema de verificação de estoque...')
        # variavel criada para o usuário escolher qual armazém deseja verificar.
        armazem = int(input('Digite o número do armazém que você deseja realizar a verificação (1 a 5): '))
        while armazem > 5 or armazem <= 0: #  loop que testa se a entrada é valida, caso não seja, é solicitado novamente uma nova entrada.
            print('Você digitou um número de armazém inexistente!')
            armazem2 = int(input('Por favor, digite novamente o número do armazém que deseja verificar de 1 a 5.\nCaso deseje voltar ao inicio digite 0: '))
            if armazem2 == 0: #  Condicional que caso o usuário queira voltar para o inicio do programa.
                print('Voltando...')
                break
            print('Você escolheu o armazém núm. {}'.format(armazem))
        if armazem == 1: #  Condição em que conforme a entrada, irá adicionar o dicionario dentro da lista "armazenamentos".
            armazenamentos.append(armazem_1)
            continue
        elif armazem == 2:
            armazenamentos.append(armazem_2)
            continue
        elif armazem == 3:
            armazenamentos.append(armazem_3)
            continue
        elif armazem == 4:
            armazenamentos.append(armazem_4)
            continue
        elif armazem == 5:
            armazenamentos.append(armazem_5)
            continue
#  função para ordenar a lista de armazenamento.
listaOrdenada = sorted(armazenamentos, key=itemgetter('Código'))
print('Armazenamentos:', listaOrdenada) #  Função "print" com as saidas do "armazém" solicitidado pelo usuário.
print('Encerrando a verificação...') #  Encerra o programa.