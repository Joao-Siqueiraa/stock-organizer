import tkinter as tk
from tkinter import messagebox
from produtos import adicionar_produto_janela, atualizar_lista_produtos, buscar_produtos_gui
from vendas import subtrair_estoque

def criar_interface():
    root = tk.Tk()
    root.title("Programa de Estoque")
    root.geometry("800x600")
    root.configure(bg="white")
    root.iconbitmap(default="assets/icone.ico")

    # Frame azul da esquerda
    leftframe = tk.Frame(root, width=205, height=600, bg="MIDNIGHTBLUE", relief="raised")
    leftframe.place(x=0,y=1,relheight=1)

    # Frame azul da direita
    rightframe = tk.Frame(root, width=600, height=600, bg="MIDNIGHTBLUE", relief="raised")
    rightframe.place(x=210,y=1, relwidth=1, relheight=1)

    botaoadd = tk.Button(leftframe, text="Add item", width=20, command=adicionar_produto_janela)
    botaoadd.place(x=10, y=10)

    # Caixa de pesquisa
    tk.Label(root, text='Pesquisar produto', font=("Century Gothic", 12), bg="MIDNIGHTBLUE", fg="white").place(x=10, y=60)
    pesquisa_entry = tk.Entry(root, font=("Century Gothic", 12))
    pesquisa_entry.place(x=10, y=100)

    # Botão de busca
    pesquisa_button = tk.Button(root, text="Buscar", font=("Century Gothic", 12), command=lambda: buscar_produtos_gui(pesquisa_entry, rightframe))
    pesquisa_button.place(x=10, y=130)

    # Botão para atualizar a página
    atualizar_button = tk.Button(root, text="Atualizar Página", font=("Century Gothic", 12), command=lambda: atualizar_lista_produtos(rightframe))
    atualizar_button.place(x=10, y=180)

    # Atualizar a lista de produtos inicialmente
    atualizar_lista_produtos(rightframe)

    

    root.mainloop()
