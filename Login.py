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
        Usuario = valores ['usuario']
        Senha = valores ['senha']
        cursor = conexao.cursor()
        select = """SELECT * FROM Usuários"""
        cursor.execute(select)
        dados = cursor.fetchall()
        if valores ['usuario'] in dados[0] and valores ['senha'] in dados[0]:
            print('Bem vindo!')
        elif valores ['usuario'] in dados[0] and valores ['senha'] not in dados[0]:
            print('Senha incorreta.')
        elif valores ['usuario'] not in dados[0]:
            print('Usuário Incorreto/Não Cadastrado')
    if eventos == 'Cadastrar':
        cursor = conexao.cursor() 
        Usuario = valores ['usuario']
        Senha = valores ['senha']
        comando = f"""INSERT INTO Usuários(Usuário_Nome, Usuário_Senha)VALUES ('{Usuario}', '{Senha}')"""
        cursor.execute(comando)
        cursor.commit()
        print('Cadastro realizado! Efetue o Login.')