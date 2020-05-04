from Funcionario import Funcionario

#conexão com a classe funcionario
funcionario=Funcionario()

#Função de escolha da opção [MENU]
def menu():
    print('Menu: Escolha uma opção')
    print('1 - Adicionar novo funcionário')
    print('2 - Editar a idade do funcionário')
    print('3 - Lista todos os funcionários')
    print('4 - Remover funcionário')
    print('5 - Sair')
    opcao = input('Digite a opção desejada:')
    return opcao

def leiaMe():
    print("Bem-vindo ao meu primeiro programa em POO com SQLite em Python - version 1.0")

#Retorna alguns informações e o menu
leiaMe()
opcao=menu()

while opcao != '5':
    if opcao == '1':
        print('\n-------- Adicionar funcionário --------')
        idFuncionario=funcionario.procuraIdFuncionarios()+1
        print('Digite o id do funcionário        :%d' %(idFuncionario))
        nomeFuncionario =      input('Digite o nome do funcionário      :')
        sobrenomeFuncionario = input('Digite o sobrenome do funcionário :')
        idadeFuncionario =     input('Digite a idade do funcionário     :')
        sexoFuncionario =      input('Digite o sexo do funcionário (F/M):')
        funcionario.addFuncionario(idFuncionario, nomeFuncionario.upper(), sobrenomeFuncionario.upper(),idadeFuncionario,sexoFuncionario.upper())

    elif opcao == '2':
        print('\n-------- Editar funcionário --------')
        idFuncionario =        input('Digite o id do funcionário        :')
        idadeFuncionario =     input('Digite a nova idade do funcionário:')
        funcionario.editarFuncionario(idFuncionario, idadeFuncionario)

    elif opcao == '3':
        print('\n-------- Lista todos os funcionário --------')
        funcionario.listFuncionarios()

    elif opcao == '4':
        print('\n-------- Excluir funcionário --------')
        idFuncionario =        input('Digite o id do funcionário        :')
        funcionario.removerFuncionario(idFuncionario)

    opcao=menu()

print('\n\nVocê saiu do sistema!!!')


