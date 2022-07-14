import base64
import os
from tkinter import *
from tkinter import ttk

#pega o ícone (que está convertido em base64) num arquivo txt que está no
#mesmo repositório do programa principal e lê
icone = "icone.txt"
icon = open(icone, 'rt')
icon = icon.read()

#lê o arquivo convertido em bas64
icondata = base64.b64decode(icon)
tempFile = "icon.ico"
iconfile = open(tempFile, "wb")
iconfile.write((icondata))
iconfile.close()


cores = {'azulcla': '#127b9e', 'pretofor': '#262323', 'branco': '#f9f9f9', 'pretofra': '#2d2928', 'vermelho': '#d34d43'}

jan = Tk()

jan.title('')
jan.geometry('300x440')
jan.resizable(False, False)
jan.config(bg=cores['pretofor'])

jan.wm_iconbitmap(tempFile)
os.remove(tempFile)

estilo_da_janela = ttk.Style(jan)
estilo_da_janela.theme_use('alt')

frame_cima = Frame(jan, width=276, height=120, bg=cores['pretofra'], relief=SOLID)
frame_cima.grid(row=0, column=0, pady=12, padx=12)

frame_baixo = Frame(jan, width=234, height=204, bg=cores['branco'], relief=SOLID)
frame_baixo.place(x=2000)

label_x = Label(frame_cima, text='X', fg=cores['vermelho'], bg=cores['pretofra'], font=('Ivy 50 bold'))
label_x.place(x=28, y=7)

label_o = Label(frame_cima, text='O', fg=cores['azulcla'], bg=cores['pretofra'], font=('Ivy 50 bold'))
label_o.place(x=195, y=7)

label_jogador1 = Label(frame_cima, text='Jogador 1', fg=cores['branco'], bg=cores['pretofra'], font=('Arial 10 bold'))
label_jogador1.place(x=20, y=82)

label_jogador2 = Label(frame_cima, text='Jogador 2', fg=cores['branco'], bg=cores['pretofra'], font=('Arial 10 bold'))
label_jogador2.place(x=188, y=82)

# variáveis que armazenam os pontos dos jogadores
ponto_do_jogador1, ponto_do_jogador2 = 0, 0

# labels que exibem os pontos dos jogadores
exibe_ponto_do_jogador1 = Label(frame_cima, text=ponto_do_jogador1, fg=cores['branco'], bg=cores['pretofra'], font=('Times 38 bold'))
exibe_ponto_do_jogador1.place(x=90, y=17)

label_2_pontinhos = Label(frame_cima, text=':', fg=cores['branco'], bg=cores['pretofra'], font=('Times 38 bold'))
label_2_pontinhos.place(x=127, y=14)

exibe_ponto_do_jogador2 = Label(frame_cima, text=ponto_do_jogador2, fg=cores['branco'], bg=cores['pretofra'], font=('Times 38 bold'))
exibe_ponto_do_jogador2.place(x=155, y=17)

contador = 0
limite = 0

# criando variável que será rastreada pela método trace_add para que as letras "X" e "O" sejam exibidas
var = StringVar()

# definindo função começar jogo
def comecar_jogo():
    label_titulo.destroy()
    botao_comecar.destroy()

    frame_baixo.grid(row=1, column=0, pady=25, padx=5)

    # definindo funções que exibem X ou O nos botões
    def botao_1():
        global contador
        if contador % 2 == 0:
            label_o_ou_x1.place(x=0, y=0)
            label_o_ou_x1['text'] = 'X'
            label_o_ou_x1['fg'] = cores['vermelho']

        else:
            label_o_ou_x1.place(x=0, y=0)
            label_o_ou_x1['text'] = 'O'
            label_o_ou_x1['fg'] = cores['azulcla']

        contador = contador + 1
        var.set('')

    def botao_2():
        global contador
        if contador % 2 == 0:
            label_o_ou_x2.place(x=80, y=0)
            label_o_ou_x2['text'] = 'X'
            label_o_ou_x2['fg'] = cores['vermelho']
        else:
            label_o_ou_x2.place(x=80, y=0)
            label_o_ou_x2['text'] = 'O'
            label_o_ou_x2['fg'] = cores['azulcla']
        contador = contador + 1
        var.set('')

    def botao_3():
        global contador
        if contador % 2 == 0:
            label_o_ou_x3.place(x=160, y=0)
            label_o_ou_x3['text'] = 'X'
            label_o_ou_x3['fg'] = cores['vermelho']
        else:
            label_o_ou_x3.place(x=160, y=0)
            label_o_ou_x3['text'] = 'O'
            label_o_ou_x3['fg'] = cores['azulcla']
        contador = contador + 1
        var.set('')

    def botao_4():
        global contador
        if contador % 2 == 0:
            label_o_ou_x4.place(x=0, y=70)
            label_o_ou_x4['text'] = 'X'
            label_o_ou_x4['fg'] = cores['vermelho']
        else:
            label_o_ou_x4.place(x=0, y=70)
            label_o_ou_x4['text'] = 'O'
            label_o_ou_x4['fg'] = cores['azulcla']
        contador = contador + 1
        var.set('')

    def botao_5():
        global contador
        if contador % 2 == 0:
            label_o_ou_x5.place(x=80, y=70)
            label_o_ou_x5['text'] = 'X'
            label_o_ou_x5['fg'] = cores['vermelho']
        else:
            label_o_ou_x5.place(x=80, y=70)
            label_o_ou_x5['text'] = 'O'
            label_o_ou_x5['fg'] = cores['azulcla']
        contador = contador + 1
        var.set('')

    def botao_6():
        global contador
        if contador % 2 == 0:
            label_o_ou_x6.place(x=160, y=70)
            label_o_ou_x6['text'] = 'X'
            label_o_ou_x6['fg'] = cores['vermelho']
        else:
            label_o_ou_x6.place(x=160, y=70)
            label_o_ou_x6['text'] = 'O'
            label_o_ou_x6['fg'] = cores['azulcla']
        contador = contador + 1
        var.set('')

    def botao_7():
        global contador
        if contador % 2 == 0:
            label_o_ou_x7.place(x=0, y=140)
            label_o_ou_x7['text'] = 'X'
            label_o_ou_x7['fg'] = cores['vermelho']
        else:
            label_o_ou_x7.place(x=0, y=140)
            label_o_ou_x7['text'] = 'O'
            label_o_ou_x7['fg'] = cores['azulcla']
        contador = contador + 1
        var.set('')

    def botao_8():
        global contador
        if contador % 2 == 0:
            label_o_ou_x8.place(x=80, y=140)
            label_o_ou_x8['text'] = 'X'
            label_o_ou_x8['fg'] = cores['vermelho']
        else:
            label_o_ou_x8.place(x=80, y=140)
            label_o_ou_x8['text'] = 'O'
            label_o_ou_x8['fg'] = cores['azulcla']
        contador = contador + 1
        var.set('')

    def botao_9():
        global contador
        if contador % 2 == 0:
            label_o_ou_x9.place(x=160, y=140)
            label_o_ou_x9['text'] = 'X'
            label_o_ou_x9['fg'] = cores['vermelho']
        else:
            label_o_ou_x9.place(x=160, y=140)
            label_o_ou_x9['text'] = 'O'
            label_o_ou_x9['fg'] = cores['azulcla']
        contador = contador + 1
        var.set('')

    # essas Funções serão executada apenas quando um dos jogadores vencer ou o jogo empatar
    def desativa_frame():
        for ferramenta in frame_baixo.winfo_children():
            ferramenta.configure(state='disable')
        botao_iniciar_novo_jogo['state'] = 'active'

    def ativa_frame():
        for ferramenta in frame_baixo.winfo_children():
            ferramenta.configure(state='normal')
            label_venceu1.place(x=4000), label_venceu2.place(x=4000), label_empate.place(x=4000)
            botao_iniciar_novo_jogo.place(x=3000)

    # esse Botão aparecerá apenas quando um dos jogadores vencer ou o jogo empatar
    botao_iniciar_novo_jogo = Button(jan, text='Iniciar novo jogo', font=('Arial 12'),bg=cores['pretofor'],
                                     fg=cores['branco'], relief=RAISED, overrelief=RIDGE, command=ativa_frame)


    def rastreia_digitacao(*args):
        global contador, limite, ponto_do_jogador1, ponto_do_jogador2

        limite = limite + 1

        labels = [label_o_ou_x1, label_o_ou_x2, label_o_ou_x3, label_o_ou_x4, label_o_ou_x5,
                  label_o_ou_x6, label_o_ou_x7, label_o_ou_x8, label_o_ou_x9]

        # possibilidades de vitória do JOGADOR 1(X)
        if label_o_ou_x1['text'] == 'X' and label_o_ou_x2['text'] == 'X' and label_o_ou_x3['text'] == 'X':
            exibe_ponto_do_jogador1['text'] = ponto_do_jogador1 = ponto_do_jogador1 + 1
            label_venceu1.place(x=30, y=90)
            botao_iniciar_novo_jogo.grid(row=3, column=0)
            desativa_frame()
            for label in labels:
                label['text'] = ''
                label.place(x=4000)
            label_o_ou_x1.place(x=9000), label_o_ou_x2.place(x=8000), label_o_ou_x3.place(x=9000)
            contador, limite = 0, 0

        elif label_o_ou_x4['text'] == 'X' and label_o_ou_x5['text'] == 'X' and label_o_ou_x6['text'] == 'X':
            exibe_ponto_do_jogador1['text'] = ponto_do_jogador1 = ponto_do_jogador1 + 1
            label_venceu1.place(x=30, y=90)
            botao_iniciar_novo_jogo.grid(row=3, column=0)
            desativa_frame()
            for label in labels:
                label['text'] = ''
                label.place(x=4000)
            label_o_ou_x4.place(x=9000), label_o_ou_x5.place(x=8000), label_o_ou_x6.place(x=9000)
            contador, limite = 0, 0

        elif label_o_ou_x7['text'] == 'X' and label_o_ou_x8['text'] == 'X' and label_o_ou_x9['text'] == 'X':
            exibe_ponto_do_jogador1['text'] = ponto_do_jogador1 = ponto_do_jogador1 + 1
            label_venceu1.place(x=30, y=90)
            botao_iniciar_novo_jogo.grid(row=3, column=0)
            desativa_frame()
            for label in labels:
                label['text'] = ''
                label.place(x=4000)
            label_o_ou_x7.place(x=9000), label_o_ou_x8.place(x=8000), label_o_ou_x9.place(x=9000)
            contador, limite = 0, 0

        elif label_o_ou_x1['text'] == 'X' and label_o_ou_x4['text'] == 'X' and label_o_ou_x7['text'] == 'X':
            exibe_ponto_do_jogador1['text'] = ponto_do_jogador1 = ponto_do_jogador1 + 1
            label_venceu1.place(x=30, y=90)
            botao_iniciar_novo_jogo.grid(row=3, column=0)
            desativa_frame()
            for label in labels:
                label['text'] = ''
                label.place(x=4000)
            label_o_ou_x1.place(x=9000), label_o_ou_x4.place(x=8000), label_o_ou_x7.place(x=9000)
            contador, limite = 0, 0

        elif label_o_ou_x2['text'] == 'X' and label_o_ou_x5['text'] == 'X' and label_o_ou_x8['text'] == 'X':
            exibe_ponto_do_jogador1['text'] = ponto_do_jogador1 = ponto_do_jogador1 + 1
            label_venceu1.place(x=30, y=90)
            botao_iniciar_novo_jogo.grid(row=3, column=0)
            desativa_frame()
            for label in labels:
                label['text'] = ''
                label.place(x=4000)
            label_o_ou_x2.place(x=9000), label_o_ou_x5.place(x=8000), label_o_ou_x8.place(x=9000)
            contador, limite = 0, 0

        elif label_o_ou_x3['text'] == 'X' and label_o_ou_x6['text'] == 'X' and label_o_ou_x9['text'] == 'X':
            exibe_ponto_do_jogador1['text'] = ponto_do_jogador1 = ponto_do_jogador1 + 1
            label_venceu1.place(x=30, y=90)
            botao_iniciar_novo_jogo.grid(row=3, column=0)
            desativa_frame()
            for label in labels:
                label['text'] = ''
                label.place(x=4000)
            label_o_ou_x3.place(x=9000), label_o_ou_x6.place(x=8000), label_o_ou_x9.place(x=9000)
            contador, limite = 0, 0

        elif label_o_ou_x1['text'] == 'X' and label_o_ou_x5['text'] == 'X' and label_o_ou_x9['text'] == 'X':
            exibe_ponto_do_jogador1['text'] = ponto_do_jogador1 = ponto_do_jogador1 + 1
            label_venceu1.place(x=30, y=90)
            botao_iniciar_novo_jogo.grid(row=3, column=0)
            desativa_frame()
            for label in labels:
                label['text'] = ''
                label.place(x=4000)
            label_o_ou_x1.place(x=9000), label_o_ou_x5.place(x=8000), label_o_ou_x9.place(x=9000)
            contador, limite = 0, 0

        elif label_o_ou_x7['text'] == 'X' and label_o_ou_x5['text'] == 'X' and label_o_ou_x3['text'] == 'X':
            exibe_ponto_do_jogador1['text'] = ponto_do_jogador1 = ponto_do_jogador1 + 1
            label_venceu1.place(x=30, y=90)
            botao_iniciar_novo_jogo.grid(row=3, column=0)
            desativa_frame()
            for label in labels:
                label['text'] = ''
                label.place(x=4000)
            label_o_ou_x7.place(x=9000), label_o_ou_x5.place(x=8000), label_o_ou_x3.place(x=9000)
            contador, limite = 0, 0

        # possibilidades de vitória do JOGADOR 2(O)
        elif label_o_ou_x1['text'] == 'O' and label_o_ou_x2['text'] == 'O' and label_o_ou_x3['text'] == 'O':
            exibe_ponto_do_jogador2['text'] = ponto_do_jogador2 = ponto_do_jogador2 + 1
            label_venceu2.place(x=30, y=90)
            botao_iniciar_novo_jogo.grid(row=3, column=0)
            desativa_frame()
            for label in labels:
                label['text'] = ''
                label.place(x=4000)
            label_o_ou_x1.place(x=9000), label_o_ou_x2.place(x=8000), label_o_ou_x3.place(x=9000)
            contador, limite = 1, 0

        elif label_o_ou_x4['text'] == 'O' and label_o_ou_x5['text'] == 'O' and label_o_ou_x6['text'] == 'O':
            exibe_ponto_do_jogador2['text'] = ponto_do_jogador2 = ponto_do_jogador2 + 1
            label_venceu2.place(x=30, y=90)
            botao_iniciar_novo_jogo.grid(row=3, column=0)
            desativa_frame()
            for label in labels:
                label['text'] = ''
                label.place(x=4000)
            label_o_ou_x4.place(x=9000), label_o_ou_x5.place(x=8000), label_o_ou_x6.place(x=9000)
            contador, limite = 1, 0

        elif label_o_ou_x7['text'] == 'O' and label_o_ou_x8['text'] == 'O' and label_o_ou_x9['text'] == 'O':
            exibe_ponto_do_jogador2['text'] = ponto_do_jogador2 = ponto_do_jogador2 + 1
            label_venceu2.place(x=30, y=90)
            botao_iniciar_novo_jogo.grid(row=3, column=0)
            desativa_frame()
            for label in labels:
                label['text'] = ''
                label.place(x=4000)
            label_o_ou_x7.place(x=9000), label_o_ou_x8.place(x=8000), label_o_ou_x9.place(x=9000)
            contador, limite = 1, 0

        elif label_o_ou_x1['text'] == 'O' and label_o_ou_x4['text'] == 'O' and label_o_ou_x7['text'] == 'O':
            exibe_ponto_do_jogador2['text'] = ponto_do_jogador2 = ponto_do_jogador2 + 1
            label_venceu2.place(x=30, y=90)
            botao_iniciar_novo_jogo.grid(row=3, column=0)
            desativa_frame()
            for label in labels:
                label['text'] = ''
                label.place(x=4000)
            label_o_ou_x1.place(x=9000), label_o_ou_x4.place(x=8000), label_o_ou_x7.place(x=9000)
            contador, limite = 1, 0

        elif label_o_ou_x2['text'] == 'O' and label_o_ou_x5['text'] == 'O' and label_o_ou_x8['text'] == 'O':
            exibe_ponto_do_jogador2['text'] = ponto_do_jogador2 = ponto_do_jogador2 + 1
            label_venceu2.place(x=30, y=90)
            botao_iniciar_novo_jogo.grid(row=3, column=0)
            desativa_frame()
            for label in labels:
                label['text'] = ''
                label.place(x=4000)
            label_o_ou_x2.place(x=9000), label_o_ou_x5.place(x=8000), label_o_ou_x8.place(x=9000)
            contador, limite = 1, 0

        elif label_o_ou_x3['text'] == 'O' and label_o_ou_x6['text'] == 'O' and label_o_ou_x9['text'] == 'O':
            exibe_ponto_do_jogador2['text'] = ponto_do_jogador2 = ponto_do_jogador2 + 1
            label_venceu2.place(x=30, y=90)
            botao_iniciar_novo_jogo.grid(row=3, column=0)
            desativa_frame()
            for label in labels:
                label['text'] = ''
                label.place(x=4000)
            label_o_ou_x3.place(x=9000), label_o_ou_x6.place(x=8000), label_o_ou_x9.place(x=9000)
            contador, limite = 1, 0

        elif label_o_ou_x1['text'] == 'O' and label_o_ou_x5['text'] == 'O' and label_o_ou_x9['text'] == 'O':
            exibe_ponto_do_jogador2['text'] = ponto_do_jogador2 = ponto_do_jogador2 + 1
            label_venceu2.place(x=30, y=90)
            botao_iniciar_novo_jogo.grid(row=3, column=0)
            desativa_frame()
            for label in labels:
                label['text'] = ''
                label.place(x=4000)
            label_o_ou_x1.place(x=9000), label_o_ou_x5.place(x=8000), label_o_ou_x9.place(x=9000)
            contador, limite = 1, 0

        elif label_o_ou_x7['text'] == 'O' and label_o_ou_x5['text'] == 'O' and label_o_ou_x3['text'] == 'O':
            exibe_ponto_do_jogador2['text'] = ponto_do_jogador2 = ponto_do_jogador2 + 1
            label_venceu2.place(x=30, y=90)
            botao_iniciar_novo_jogo.grid(row=3, column=0)
            desativa_frame()
            for label in labels:
                label['text'] = ''
                label.place(x=4000)
            contador, limite = 1, 0

        if limite == 9:
            contador, limite = 0, 0
            label_empate.place(x=30, y=90)
            botao_iniciar_novo_jogo.grid(row=3, column=0)
            desativa_frame()
            for label in labels:
                label['text'] = ''
                label.place(x=4000)

    # rastreia digitação e executa a função rastreia_digitacao
    var.trace_add('write', rastreia_digitacao)

    # criando os campos que exibirão "O" ou "X"
    botao_1 = Button(frame_baixo, command=botao_1,  pady=3, padx=6, bg=cores['pretofor'],
                     fg=cores['azulcla'], width=3, font=('Arial 22 bold'), relief=FLAT, overrelief=RIDGE)
    botao_1.place(x=0, y=0)

    botao_2 = Button(frame_baixo, command=botao_2, pady=3, padx=6, bg=cores['pretofor'],
                     fg=cores['azulcla'], width=3, font=('Arial 22 bold'), relief=FLAT, overrelief=RIDGE)
    botao_2.place(x=80, y=0)

    botao_3 = Button(frame_baixo, command=botao_3, pady=3, padx=6, bg=cores['pretofor'],
                     fg=cores['azulcla'], width=3, font=('Arial 22 bold'), relief=FLAT, overrelief=RIDGE)
    botao_3.place(x=160, y=0)


    botao_4 = Button(frame_baixo, command=botao_4, pady=3, padx=6, bg=cores['pretofor'],
                     fg=cores['azulcla'], width=3, font=('Arial 22 bold'), relief=FLAT, overrelief=RIDGE)
    botao_4.place(x=0, y=70)

    botao_5 = Button(frame_baixo, command=botao_5, pady=3, padx=6, bg=cores['pretofor'],
                     fg=cores['azulcla'], width=3, font=('Arial 22 bold'), relief=FLAT, overrelief=RIDGE)
    botao_5.place(x=80, y=70)

    botao_6 = Button(frame_baixo, command=botao_6, pady=3, padx=6, bg=cores['pretofor'],
                     fg=cores['azulcla'], width=3, font=('Arial 22 bold'), relief=FLAT, overrelief=RIDGE)
    botao_6.place(x=160, y=70)


    botao_7 = Button(frame_baixo, command=botao_7, pady=3, padx=6, bg=cores['pretofor'],
                     fg=cores['azulcla'], width=3, font=('Arial 22 bold'), relief=FLAT, overrelief=RIDGE)
    botao_7.place(x=0, y=140)

    botao_8 = Button(frame_baixo, command=botao_8, pady=3, padx=6, bg=cores['pretofor'],
                     fg=cores['azulcla'], width=3, font=('Arial 22 bold'), relief=FLAT, overrelief=RIDGE)
    botao_8.place(x=80, y=140)

    botao_9 = Button(frame_baixo, command=botao_9, pady=3, padx=6, bg=cores['pretofor'],
                     fg=cores['azulcla'], width=3, font=('Arial 22 bold'), relief=FLAT, overrelief=RIDGE)
    botao_9.place(x=160, y=140)

    # criando label "JogadorX venceu"
    # essas Labels aparecerão apenas quando um dos jogadores vencer ou o jogo empatar
    label_venceu1 = Label(frame_baixo, text='Jogador1 VENCEU!', relief=RAISED, fg=cores['branco'], bg=cores['pretofor'], font=('Arial 15'))
    label_venceu2 = Label(frame_baixo, text='Jogador2 VENCEU!', relief=RAISED, fg=cores['branco'], bg=cores['pretofor'], font=('Arial 15'))
    label_empate = Label(frame_baixo, text='O jogo EMPATOU', relief=RAISED, fg=cores['branco'], bg=cores['pretofor'], font=('Arial 15'))

    # criando labels que exibirão "X" ou "O"
    label_o_ou_x1 = Label(frame_baixo, width=3, height=1, padx=5, pady=11,
                           bg=cores['pretofor'], fg=cores['azulcla'], font=('Arial 25 bold'))
    label_o_ou_x1.place(x=5000)

    label_o_ou_x2 = Label(frame_baixo, width=3, height=1, padx=5, pady=11,
                            bg=cores['pretofor'], fg=cores['azulcla'], font=('Arial 25 bold'))
    label_o_ou_x2.place(x=5000)

    label_o_ou_x3 = Label(frame_baixo, width=3, height=1, padx=5, pady=11,
                            bg=cores['pretofor'], fg=cores['azulcla'], font=('Arial 25 bold'))
    label_o_ou_x3.place(x=5000)


    label_o_ou_x4 = Label(frame_baixo, width=3, height=1, padx=5, pady=11,
                            bg=cores['pretofor'], fg=cores['azulcla'], font=('Arial 25 bold'))
    label_o_ou_x4.place(x=5000)

    label_o_ou_x5 = Label(frame_baixo, width=3, height=1, padx=5, pady=11,
                            bg=cores['pretofor'], fg=cores['azulcla'], font=('Arial 25 bold'))
    label_o_ou_x5.place(x=5000)

    label_o_ou_x6 = Label(frame_baixo, width=3, height=1, padx=5, pady=11,
                            bg=cores['pretofor'], fg=cores['azulcla'], font=('Arial 25 bold'))
    label_o_ou_x6.place(x=5000)


    label_o_ou_x7 = Label(frame_baixo, width=3, height=1, padx=5, pady=11,
                            bg=cores['pretofor'], fg=cores['azulcla'], font=('Arial 25 bold'))
    label_o_ou_x7.place(x=5000)

    label_o_ou_x8 = Label(frame_baixo, width=3, height=1, padx=5, pady=11,
                            bg=cores['pretofor'], fg=cores['azulcla'], font=('Arial 25 bold'))
    label_o_ou_x8.place(x=5000)

    label_o_ou_x9 = Label(frame_baixo, width=3, height=1, padx=5, pady=11,
                            bg=cores['pretofor'], fg=cores['azulcla'], font=('Arial 25 bold'))
    label_o_ou_x9.place(x=5000)


label_titulo = Label(jan, text='JOGO DA\nVELHA #', font=('Arial 40 bold'), fg=cores['branco'], bg=cores['pretofor'])
label_titulo.grid(row=2, column=0)

botao_comecar = Button(jan, text='Iniciar jogo', command=comecar_jogo, bg=cores['pretofor'],fg=cores['branco'], font=('Arial 14'), relief=RAISED, borderwidth=1, overrelief=RIDGE)
botao_comecar.grid(row=3, column=0, pady=10)

jan.mainloop()
