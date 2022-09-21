import pyodbc
from PySimpleGUI import PySimpleGUI as sg

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-6UP649V;"
    "Database=Login;"
)
conexao = pyodbc.connect(dados_conexao)

#Layout
sg.theme('Material2')
layout = [
    [sg.Text('Usuário'),sg.Input(key='usuario')],
    [sg.Text('Senha'),sg.Input(key='senha',password_char='*')],
    [sg.Button('Entrar')], 
    [sg.Button('Cadastrar')]
]
#Janela
janela = sg.Window('Tela de Login', layout)
#Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        cursor = conexao.cursor()
        Usuario = valores ['usuario']
        cusuario = f"""SELECT Usuário_Nome FROM Usuários WHERE Usuário_Nome = '{Usuario}'"""
        cursor.execute(cusuario)
        cusuario = cusuario[56:-1]
        if valores ['usuario'] == cusuario:
            cursos = conexao.cursor()
            Senha = valores ['senha']
            csenha = f"""SELECT Usuário_Senha FROM Usuários WHERE Usuário_Senha = '{Senha}'"""
            cursor.execute(csenha)
            csenha = csenha[58:-1]
            if valores ['senha'] == csenha:
                print('Bem vindo!')
        elif valores ['usuario'] == cusuario and valores ['senha'] != csenha:
            print('Senha incorreta.')
        elif valores ['usuario'] != cusuario:
            print('Usuário Incorreto/Não Cadastrado')
    if eventos == 'Cadastrar':
        cursor = conexao.cursor() 
        Usuario = valores ['usuario']
        Senha = valores ['senha']
        comando = f"""INSERT INTO Usuários(Usuário_Nome, Usuário_Senha)VALUES ('{Usuario}', '{Senha}')"""
        cursor.execute(comando)
        cursor.commit()
        print('Cadastro realizado! Efetue o Login.')