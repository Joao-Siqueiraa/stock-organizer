import sqlite3
from tkinter import messagebox
import tkinter as tk


def buscar_produtos(busca=None):
    produtos = listar_produtos(busca)
    return produtos


def listar_produtos(busca=None):
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()

    if busca:
        # Usar a cláusula LIKE com parâmetro correto para a consulta
        cursor.execute("SELECT nome, quantidade FROM produtos WHERE nome LIKE ?", ('%' + busca + '%',))
    else:
        cursor.execute("SELECT nome, quantidade FROM produtos")
    
    produtos = cursor.fetchall()
    conn.close()
    return produtos


def adicionar_produto(nome, quantidade):
    try:
        conn = sqlite3.connect('estoque.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO produtos (nome, quantidade) VALUES (?, ?)", (nome, quantidade))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao adicionar produto: {e}")
        return False


def adicionar_produto_janela():
    # Janela de Adicionar Produto
    tl = tk.Toplevel()
    tl.title("Adicionar Produto")
    tl.geometry("300x200")
    tl.configure(bg='lightgray')

    # Label e Entry para o nome do produto
    tk.Label(tl, text="Nome", font=("Century Gothic", 12), bg='lightgray').pack(pady=5)
    nome_produto = tk.Entry(tl, font=("Century Gothic", 12))
    nome_produto.pack(pady=5)

    # Label e Entry para a quantidade do produto
    tk.Label(tl, text="Quantidade:", font=("Century Gothic", 12), bg="lightgray").pack(pady=5)
    quantidade_produto = tk.Entry(tl, font=("Century Gothic", 12))
    quantidade_produto.pack(pady=5)

    def salvar_produto():
        # Pega o nome e a quantidade do produto
        nome = nome_produto.get().strip()
        quantidade = quantidade_produto.get().strip()

        if not nome or not quantidade.isdigit():
            messagebox.showerror("Erro", "Nome inválido ou quantidade não numérica")
            return  # Sai da função sem salvar o produto errado

        adicionar_produto(nome, int(quantidade))
        messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
        tl.destroy()

    tk.Button(tl, text="Salvar", font=("Century Gothic", 12), command=salvar_produto).pack(pady=10)
    tl.mainloop()


def atualizar_lista_produtos(rightframe, busca=None):
    produtos = buscar_produtos(busca)
    
    # Limpa a lista de produtos exibida
    for widget in rightframe.winfo_children():
        widget.destroy()

    # Adiciona o cabeçalho
    itemlabel = tk.Label(rightframe, text="Item", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    itemlabel.place(x=50, y=10)
    vendalabel = tk.Label(rightframe, text="Venda", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    vendalabel.place(x=220, y=10)
    estoquelabel = tk.Label(rightframe, text="Estoque", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    estoquelabel.place(x=420, y=10)

    # Recupera os produtos da função listar_produtos
    y_offset = 50  # Posição inicial para os produtos na tela
    for nome, quantidade in produtos:
        tk.Label(rightframe, text=nome, font=("Century Gothic", 14), bg="MIDNIGHTBLUE", fg="white").place(x=50, y=y_offset)
        tk.Label(rightframe, text=str(quantidade), font=("Century Gothic", 14), bg="MIDNIGHTBLUE", fg="white").place(x=420, y=y_offset)
        y_offset += 30  # Move os próximos produtos para baixo


def buscar_produtos_gui(pesquisa_entry, rightframe):
    busca = pesquisa_entry.get().strip()  # Pega o texto da entrada de pesquisa
    atualizar_lista_produtos(rightframe, busca)  # Atualiza a lista com o nome buscado
