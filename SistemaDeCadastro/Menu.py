class Menu:
    opcao=0
    def __init__(self):
        print('Menu: Escolha uma opção')
        print('1 - Matricular aluno')
        print('2 - Remover aluno')
        print('3 - Lista todos os alunos')
        print('4 - Editar aluno')
        print('5 - Sair')
        self.opcao=int(input('Digte a opção desejada:'))

    def opcaoescolhida(self):
        return self.opcao