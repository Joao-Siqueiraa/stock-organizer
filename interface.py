import tkinter as tk
from tkinter import messagebox
from produtos import listar_produtos, adicionar_produto
from vendas import registrar_venda

def criar_interface():
    root = tk.Tk()
    root.title("Programa de Estoque")
    root.geometry("800x600")
    root.configure(bg="white")
    root.iconbitmap(default="assets/icone.ico")

    #frameazul da esquerda
    leftframe = tk.Frame(root, width=205,height=600,bg="MIDNIGHTBLUE",relief="raised")
    #posiçao do frame
    leftframe.pack(side="left")
    #frameazuldireita
    rightframe = tk.Frame(root, width=590,height=600,bg="MIDNIGHTBLUE",relief="raised")
    rightframe.pack(side="right")
    #label item
    itemlabel = tk.Label(rightframe, text="Item", font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="white")
    #posiçao item
    itemlabel.place(x=50,y=10)
    #vendalabel
    vendalabel = tk.Label(rightframe, text="Venda", font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="white")
    vendalabel.place(x=220,y=10)
    #estoquelabel
    estoquelabel = tk.Label(rightframe, text="Estoque", font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="white")
    estoquelabel.place(x=420,y=10)
    root.mainloop()
