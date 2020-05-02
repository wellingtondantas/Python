#Lista com o nome dos funcionarios
listFuncionario=[]


#Função de escolha da opção [MENU]
def menu():
    print('Menu: Escolha uma opção')
    print('1 - Adicionar novo funcionário')
    print('2 - Editar funcionário')
    print('3 - Lista todos os funcionário')
    print('4 - Remover funcionário')
    print('5 - Sair')
    opcao = input('Digite a opção desejada:')
    return opcao

#Função para adicionar alunos
def addFuncionario():
    nomeFuncionario = str(input('Digite o nome do funcionário:'))
    nomeFuncionario=nomeFuncionario.upper()
    if nomeFuncionario in listFuncionario:
        print('Funcionário já cadastro')
    else:
        listFuncionario.append(nomeFuncionario)
        print('funcionário cadastro')
    pass

def editarFuncionario(nome):
    i=0;

    if nome in listFuncionario:
        print('Funcionario %s encontrado' %(nome))

        for item in range(len(listFuncionario)):
            if listFuncionario[item] == nome:
                i=item;

        atualizarNome = str(input('Digite o novo nome do funcionario:'))
        listFuncionario[i]=atualizarNome.upper()
    else:
        print('Funcionário não encontrado')
    pass

def listarFuncionario():
    if len(listFuncionario)==0:
        print('Nenhum funcionário cadastro')
    else:
        for id,item in enumerate(listFuncionario):
            print('%d - %s' %(id,item))
    pass

def removerFuncionario(nome):

    if nome in listFuncionario:
        for item in range(len(listFuncionario)):
            if listFuncionario[item] == nome:
                i=item;

        del listFuncionario[i]
        print('Funcionario %s removido' % (nome))
    else:
        print('Funcionário não encontrado')
    pass

def leiaMe():
    print("Bem-vindo ao meu primeiro programa em Python - version 1.0")

leiaMe()
opcao=menu()

while opcao != '5':
    if opcao == '1':
        print('\n-------- Adicionar funcionário --------')
        addFuncionario()
    elif opcao == '2':
        print('\n-------- Editar funcionário --------')
        nome=str(input('Digite nome do funcionário:'))
        editarFuncionario(nome.upper())

    elif opcao == '3':
        print('\n-------- Lista todos os funcionário --------')
        listarFuncionario()
    elif opcao == '4':
        print('\n-------- Excluir funcionário --------')
        nome = str(input('Digite nome do funcionário:'))
        removerFuncionario(nome.upper())

    opcao=menu()
print('\n\nVocê saiu do sistema!!!')