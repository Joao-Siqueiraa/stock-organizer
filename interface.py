import tkinter as tk
from produtos import adicionar_produto_janela, atualizar_lista_produtos, buscar_produtos_gui


def criar_interface():
    root = tk.Tk()
    root.title("Programa de Estoque")
    root.geometry("800x600")
    root.configure(bg="white")
    root.iconbitmap(default="assets/icone.ico")

    # Frame azul da esquerda
    leftframe = tk.Frame(root, width=205, height=600, bg="MIDNIGHTBLUE", relief="raised")
    leftframe.pack(side="left")

    # Frame azul da direita
    rightframe = tk.Frame(root, width=590, height=600, bg="MIDNIGHTBLUE", relief="raised")
    rightframe.pack(side="right")

    # Labels para o cabeçalho
    itemlabel = tk.Label(rightframe, text="Item", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    itemlabel.place(x=50, y=10)
    vendalabel = tk.Label(rightframe, text="Venda", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    vendalabel.place(x=220, y=10)
    estoquelabel = tk.Label(rightframe, text="Estoque", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    estoquelabel.place(x=420, y=10)

    # Caixa de pesquisa
    tk.Label(root, text='Pesquisar produto', font=("Century Gothic", 12), bg="MIDNIGHTBLUE", fg="white").place(x=10, y=60)
    pesquisa_entry = tk.Entry(root, font=("Century Gothic", 12))
    pesquisa_entry.place(x=10, y=100)

    # Botão de busca
    pesquisa_button = tk.Button(root, text="Buscar", font=("Century Gothic", 12), command=lambda: buscar_produtos_gui(pesquisa_entry, rightframe))
    pesquisa_button.place(x=10, y=130)

    # Função para atualizar a lista de produtos
    def atualizar_pagina():
        atualizar_lista_produtos(rightframe)  # Atualiza a lista de produtos

    # Botão para atualizar a página
    atualizar_button = tk.Button(root, text="Atualizar Página", font=("Century Gothic", 12), command=atualizar_pagina)
    atualizar_button.place(x=10, y=180)

    # Atualizar a lista de produtos inicialmente
    atualizar_lista_produtos(rightframe)

    # Botão para adicionar um novo produto
    botaoadd = tk.Button(leftframe, text='Adicionar Item', width=20, command=adicionar_produto_janela)
    botaoadd.place(x=30, y=20)

    root.mainloop()
