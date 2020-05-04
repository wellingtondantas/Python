#Remove as instruções do banco de dados (caso exista) e criar outras instruções
import os
os.remove("db.db") if os.path.exists("db.db") else None

#Importa o módulo de acesso ao SQLite
import sqlite3

#Conexão com o banco de dados
conexao = sqlite3.connect('db.db')

#Criando um cursor
inst = conexao.cursor()

#Linguagem SQL (Criação da Tabela funcionários)
sql='create table funcionario' '(id integer primary key,' 'nome varchar(20),' 'sobrenome varchar(20),' 'idade integer,' 'sexo char(1))'

#Executa a instrução SQL no curso
inst.execute(sql)

#Linguagem SQL (Inserção de informação manual)
sql2='insert into funcionario values (?,?,?,?,?)'

#Informação a ser inserida
funcionario1=[1000,'NATÁLIA','NOGUIERA',24,'F']
funcionario2=[1001,'RENATA','SOUSA',20,'F']
funcionario3=[1002,'PEDRO','GOMES',50,'M']
funcionario4=[1003,'MARIA','SILVA',25,'F']
funcionario5=[1004,'CARLOS','DANTAS',50,'M']

#Inserindo a informação na tabela do db
inst.execute(sql2,funcionario1)
inst.execute(sql2,funcionario2)
inst.execute(sql2,funcionario3)
inst.execute(sql2,funcionario4)
inst.execute(sql2,funcionario5)

#Grava a informação no db
conexao.commit()

#Mostra todos os funcionarios
inst.execute('select * from funcionario')
funcionariosAll = inst.fetchall()
for item in funcionariosAll:
    print('\n ID: %d, Nome: %s, Sobrenome: %s, Idade: %d, Sexo: %s, ' % item)



