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
        select = """SELECT * FROM Usuários"""
        cursor.execute(select)
        usuarios = [x for x, y, z in cursor.fetchall()]
        cursor.execute(select)
        codigos = [z for x, y, z in cursor.fetchall()]
        if valores ['usuario'] in usuarios and valores ['usuario'] + valores ['senha'] in codigos:
            print('Bem vindo!')
        elif valores ['usuario'] in usuarios and valores ['usuario'] + valores ['senha'] not in codigos:
            print('Senha incorreta.')
        else:
            print('Usuário Incorreto/Não Cadastrado')
    if eventos == 'Cadastrar':
        cursor = conexao.cursor() 
        Usuario = valores ['usuario']
        Senha = valores ['senha']
        Cod = valores ['usuario'] + valores ['senha']
        comando = f"""INSERT INTO Usuários(Usuário_Nome, Usuário_Senha, Usuário_Cod)VALUES ('{Usuario}', '{Senha}', '{Cod}')"""
        cursor.execute(comando)
        cursor.commit()
        print('Cadastro realizado! Efetue o Login.')