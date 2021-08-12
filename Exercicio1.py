while True: #Realiza o comando de laço de repetição até atingir o comando "Break", ou seja, até usuário decidir encerrar o programa..
    valor = int(input('Digite "1" para inserir seus dados ou "0" para sair: '))
    if valor == 1: #Condição que testa a entrada do usuario para realizar o programa ou encerrar.
        print('Você escolheu inserir seus dados')
        dados = input('Nome completo do aluno: ')
        nota = float(input('Nota: '))
        if nota >= 0 and nota <= 10: #Condição que ira verificar se a nota é válida.
            if nota <= 2.9:
                print('O aluno {} tirou a nota {} equivalente ao conceito E!'.format(dados, nota))
            elif nota <= 4.9:
                print('O aluno {} tirou a nota {} equivalente ao conceito D!'.format(dados, nota))
            elif nota <= 6.9:
                print('O aluno {} tirou a nota {} equivalente ao conceito C!'.format(dados, nota))
            elif nota <= 8.9:
                print('O aluno {} tirou a nota {} equivalente ao conceito B!'.format(dados, nota))
            else:
                print('O aluno {} tirou a nota {} equivalente ao conceito A!'.format(dados, nota))
        else: #Fimse que informa a nota for inválida.
            print('A nota {} é inválida.'.format(nota))
    if not valor: # Condição Falsey que faz somente aceitar 1 ou 0 na condição "valor == 1",
        # sendo assim, quando o usuário digitar um valor > 1 ou valor < 0. Ele fica repetindo até o usuário por 0 ou 1.
        print('Você escolheu sair do programa.')
        print('Encerrando programa...')
        break
