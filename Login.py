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
        if valores ['usuario'] == 'teste' and valores ['senha'] == '123456':
            print('Bem vindo!')
        elif valores ['usuario'] == 'teste' and valores ['senha'] != '123456':
            print('Senha incorreta.')
        elif valores ['usuario'] != 'teste':
            print('Usuário Incorreto/Não Cadastrado')
    