import PySimpleGUI as sg
#criar janelas e estilos (layout)

def janelaLogin():
    [sg.theme('HotDogStand')],
    #[sg.theme('Dark Ambar 5')],
    layout = [
        [sg.Text('Nome')], #label
        [sg.Input()], #input "caixa branca"
        [sg.Button('Continuar')]
    ]
    return sg.Window('Login', layout= layout, finalize= True)

def janelaPedido():
    layout = [
        [sg.Text('Sabores: ')],
        [sg.Checkbox('Pizza Calabresa',key='pizza1'),sg.Checkbox('Pizza Bacon',key='pizza2')],
        [sg.Button('voltar'), sg.Button('fazer pedido')]
    ]
    return sg.Window('Montar Pedido', layout = layout, finalize= True)

# criar janelas iniciais
janela1,janela2 = janelaLogin(), None 
#'''none para nao inicializar a segunda tela'''
# criar um loop de eventos
while True:
    window,event,values = sg.read_all_windows()
   # '''informacao qual janela esta sendo lida qual evento esta sendo disparado e quais valores estao sendo passados no momento'''
    #quando a janela login for fechada
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela2 and event == sg.WIN_CLOSED:
        break
    #quando queremos ir pra proxima janela
    if window == janela1 and event == 'Continuar':
        janela2 = janelaPedido()
        janela1.hide() 
        #'''escondeu a primeira janela do login e apareceu a segunda do pedido'''
    if window == janela2 and event == 'voltar':
        janela2.hide()
        janela1.un_hide()
        #'''esconde a janela de pedido e mostra a de login'''
    if window == janela2 and event == 'fazer pedido':
        if values['pizza1'] == True and values['pizza2'] == True:
            sg.popup('Foram solicitados uma Pizza de Calabresa e uma Pizza de Bacon')
        elif values['pizza1'] == True:
            sg.popup('Foi solicitado uma Pizza de Calabresa')
        elif values['pizza2'] == True:
            sg.popup('Foi solicitado uma Pizza de Bacon')
        #quando queremos voltar p janela anterior
    
# logica de o que deve acontecer ao clicar
# nos botoes