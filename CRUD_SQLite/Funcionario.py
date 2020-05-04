#Remove as instruções do banco de dados (caso exista) e criar outras instruções
#import os
#os.remove("db.db") if os.path.exists("db.db") else None

#Importa o módulo de acesso ao SQLite
import sqlite3

#Conexão com o banco de dados
conexao = sqlite3.connect('db.db')

#Criando um cursor
inst = conexao.cursor()

# Executa a instrução SQL no cursor
#inst.execute('create table funcionario' '(id integer primary key,' 'nome varchar(20),' 'sobrenome varchar(20),' 'idade integer,' 'sexo char(1))')



class Funcionario:

    #Construtor da class
    def __init__(self):
        print('Instancia conectada')

    #Método adicionar funcionario
    def addFuncionario(self, id, nome, sobrenome, idade, sexo):

        newFuncionario=(id, nome, sobrenome, idade, sexo)

        # Inserindo a informação na tabela do db
        inst.execute('insert into funcionario values (?,?,?,?,?)', newFuncionario)

        # Grava a informação no db
        conexao.commit()

        print('\nFuncionário (Foi cadastrado com sucesso)')

    #Método editar idade de funcionário pelo id
    def editarFuncionario(self, idx, idade):
        inst.execute("update funcionario set idade =" + idade + " where id = " + idx)
        conexao.commit()

    #Método remover funcionário pelo id
    def removerFuncionario(self, idx):
        inst.execute("delete from funcionario where id = "+idx)
        conexao.commit()

    #Método listar todos os funcionários
    def listFuncionarios(self):
        inst.execute('select * from funcionario')
        funcionariosAll = inst.fetchall()
        for item in funcionariosAll:
            print('ID: %d, Nome: %s, Sobrenome: %s, Idade: %d, Sexo: %s, ' % item)

    #Método que retorna o último ID de funcionários
    def procuraIdFuncionarios(self):
        inst.execute('select max(id) from funcionario')
        x = inst.fetchall()
        lista=list(x)
        tupla=lista[0]
        if tupla[0]==None:
            return int('999')
        else:
            return tupla[0]