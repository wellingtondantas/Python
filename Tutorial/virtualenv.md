# Tutorial para criação de ambiente virtual - virtualenv no Windows

Este tutorial pode ajuda a criar um ambiente virtual em seu computador que NÃO tem anaconda. 

- 1º criar uma virtualenv com o Python genérico
- 2° criar uma virtualenv com outra versão do Python 


### O que eu preciso?
- Um computador

- Tempo e paciência

### O que eu vou ganhar?

- Conhecimento!

- O ambiente virtual modelo Python.


## 1º criar uma virtualenv com o Python genérico

1. Crie a pasta do seu projeto exemplo: DiabetesML
   A pasta está no endereço: C:\Users\User\Documents\Python\DiabetesML

2. Acesse o cmd do windows ou terminal do seu editor, exemplo: vscode
```
C:\Users\User> 
```

3.  Informe o local da pasta do seu projeto
```
C:\Users\User>  cd C:\Users\User\Documents\Python\DiabetesML
```

4. Crie o ambiente virtual na pasta do seu projeto: exemplo: virtualenv + (nome do ambiente)
```
C:\Users\User\Documents\Python\DiabetesML> virtualenv ambiente01
```

5. Acesse o ambiente virtual (nome do ambiente)\Scripts\activate
```
C:\Users\User\Documents\Python\DiabetesML> ambiente01\Scripts\activate
```

vai aparecer assim:
```
(ambiente01) C:\Users\User\Documents\Python\DiabetesML> 
```

OBS: Se não aparecer o (ambiente02) não deu certo a criação do ambiente virtual.


6. Para sair do ambiente virtual:

```
(ambiente01) C:\Users\User\Documents\Python\DiabetesML> deactivate
```

Se não aparecer o (ambiente01) não deu certo a criação do ambiente virtual.

## 2º criar uma virtualenv com o Python indicado. Exemplo: python3.6

1. Crie a pasta do seu projeto exemplo: DiabetesML
   A pasta está no endereço: C:\Users\User\Documents\Python\DiabetesML

2. Acesse o cmd do windows ou terminal do seu editor, exemplo: vscode
```
C:\Users\User> 
```

3.  Informe o local da pasta do seu projeto
```
C:\Users\User>  cd C:\Users\User\Documents\Python\DiabetesML
```

4. Crie o ambiente virtual na pasta do seu projeto com python indicado: exemplo: virtualenv -p diretorio-da-versao-do-python(nome do ambiente)
```
C:\Users\User\Documents\Python\DiabetesML> virtualenv -p C:\Users\User\AppData\Local\Programs\Python\Python36\python.exe ambiente02
```

5. Acesse o ambiente virtual (nome do ambiente)\Scripts\activate
```
C:\Users\User\Documents\Python\DiabetesML> ambiente02\Scripts\activate
```

vai aparecer assim:
```
(ambiente02) C:\Users\User\Documents\Python\DiabetesML> 
```

OBS: Se não aparecer o (ambiente02) não deu certo a criação do ambiente virtual.

6. Para sair do ambiente virtual:

```
(ambiente02) C:\Users\User\Documents\Python\DiabetesML> deactivate
```













