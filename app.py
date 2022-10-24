import PySimpleGUI as sg

layout = [
    [sg.Text("Carga horária estoque")],
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text("Senha")],
    [sg.Input(key='senha')],
    [sg.Button('login')],
    [sg.Text('', key='mensagem')],
    [sg.Button('Não sou usuário, criar conta')],
]

layout2 = [
    [sg.Text('Criar sua conta')],
    [sg.Text('Nome completo')],
    [sg.Input(key='nome')],
    [sg.Text('Nome de Usuário')],
    [sg.Input(key='Usuario')],
    [sg.Text('Turno')],
    [sg.Input(key='turno')],
    [sg.Text('Senha')],
    [sg.Input(key='Senha')],
    [sg.Button('Criar conta')],
    [sg.Text('', key='aviso')],
]

window = sg.Window('Login',layout=layout)
window2 = sg.Window('Criar conta', layout=layout2)

while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
       break 
    elif event == 'login':
        senha_correta = 'abcde123'
        usuario_correto = 'dark.soo'
        usuario = values['usuario']
        senha = values['senha']
        if senha == senha_correta and usuario == usuario_correto:
            window['mensagem'].update('Login feito com sucesso!')
        else:
            window['mensagem'].update('Usuário ou senha incorreto!')
    elif event == 'Não sou usuário, criar conta':
        event, values = window2.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == "Criar conta":
            Nome_certo = 'Ana Clara'
            Usuario_certo = 'dark.soo'
            Turno_certo = 'Manhã'
            Senha_certa = 'abcde123'
            nome = values['nome']
            Usuario = values['Usuario']
            turno = values['turno']
            Senha = values['Senha']
            if nome == Nome_certo and Usuario == Usuario_certo and turno == Turno_certo and Senha == Senha_certa:
                window2['aviso'].update('Conta criada com sucesso!')
            else:
                window2['aviso'].update('Tente novamente!')