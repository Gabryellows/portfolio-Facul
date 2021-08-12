# Criando a função e definindo os parâmetros.
def criar_email(name, sobrename, ru):  # Função criada com seus parâmetros dentro do parênteses.
    return (name[0] + sobrename + ru + '@algoritmos.com.br').lower().replace(' ', '')
    # lower utilizado para deixar todas as letras minúsculas e replace para substituir os espaços entre no sobrenome.
    # Usando o parâmetro de retorno para a função Email e seus respectivos que vão ser utilizados para a criação do mesmo.


# Criando as variáveis para ler do teclado para o usuário conseguir criar seu email..
nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
r_u = input('Digite os dois últimos dígitos do seu RU: ')
email = criar_email(nome, sobrenome, r_u)  # Variável com a atribuição da função criarEmail.
print('Senhor(a) {} {} seu email no domínio @algoritmos.com.br ficou: {}'.format(nome, sobrenome, email))
# Por fim a função "print" que irá conter o nome, sobrenome do usuário e seu email já formado.
