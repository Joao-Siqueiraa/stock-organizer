import tkinter as tk
from tkinter import messagebox
import sqlite3

# Função para conectar ao banco de dados
def conectar_db():
    return sqlite3.connect('estoque.db')

# Função para exibir os itens no estoque
def exibir_estoque():
    # Limpar a tela antes de exibir os dados
    for widget in frame_estoque.winfo_children():
        widget.destroy()

    # Conectar ao banco de dados
    conn = conectar_db()
    cursor = conn.cursor()

    # Buscar todos os produtos
    cursor.execute("SELECT * FROM ESTOQUE")
    produtos = cursor.fetchall()

    # Cabeçalhos
    tk.Label(frame_estoque, text="Produto", bg="blue", fg="white").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(frame_estoque, text="Vender", bg="blue", fg="white").grid(row=0, column=1, padx=10, pady=5)
    tk.Label(frame_estoque, text="Total Estoque", bg="blue", fg="white").grid(row=0, column=2, padx=10, pady=5)

    # Exibir os itens na tabela
    for i, produto in enumerate(produtos, start=1):
        nome, quantidade = produto[1], produto[2]

        # Nome do item
        tk.Label(frame_estoque, text=nome, bg="blue", fg="white").grid(row=i, column=0, padx=10, pady=5)

        # Campo Entry para quantidade a ser vendida
        quantidade_entry = tk.Entry(frame_estoque)
        quantidade_entry.grid(row=i, column=1, padx=10, pady=5)

        # Botão "Go" para confirmar a venda
        def confirmar_venda(nome_produto=nome, quantidade_produto=quantidade, entry=quantidade_entry):
            try:
                quantidade_vender = int(entry.get())  # Obter valor da Entry como inteiro
                if quantidade_vender <= 0:
                    raise ValueError("Quantidade deve ser positiva.")

                # Exibir a mensagem de confirmação
                resposta = messagebox.askyesno("Confirmar", f"Deseja vender {quantidade_vender} unidades de {nome_produto}?")
                if resposta:
                    nova_quantidade = quantidade_produto - quantidade_vender
                    conn = conectar_db()
                    cursor = conn.cursor()
                    cursor.execute("UPDATE ESTOQUE SET Quantidade = ? WHERE Nome = ?", (nova_quantidade, nome_produto))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Sucesso", f"Estoque de {nome_produto} atualizado!")
                    exibir_estoque()  # Atualizar a tabela
            except ValueError:
                messagebox.showerror("Erro", "Por favor, insira um valor válido para a quantidade.")

        tk.Button(frame_estoque, text="Go", command=confirmar_venda).grid(row=i, column=2, padx=10, pady=5)

        # Exibir o total do estoque
        tk.Label(frame_estoque, text=quantidade, bg="blue", fg="white").grid(row=i, column=3, padx=10, pady=5)

    conn.close()

# Função para adicionar novos itens ao estoque
def adicionar_item():
    def salvar_item():
        nome = nome_entry.get()
        quantidade = quantidade_entry.get()

        if nome and quantidade.isdigit() and int(quantidade) > 0:
            conn = conectar_db()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO ESTOQUE (Nome, Quantidade) VALUES (?, ?)", (nome, int(quantidade)))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Item adicionado com sucesso!")
            tela_add_item.destroy()
            exibir_estoque()  # Atualizar o estoque
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos corretamente.")

    # Criar a janela para adicionar item
    tela_add_item = tk.Toplevel(tela)
    tela_add_item.title("Adicionar Novo Item")
    tela_add_item.geometry("300x200")

    # Campos para nome e quantidade do item
    tk.Label(tela_add_item, text="Nome do Produto:").pack(pady=5)
    nome_entry = tk.Entry(tela_add_item)
    nome_entry.pack(pady=5)

    tk.Label(tela_add_item, text="Quantidade:").pack(pady=5)
    quantidade_entry = tk.Entry(tela_add_item)
    quantidade_entry.pack(pady=5)

    # Botão para salvar o item
    tk.Button(tela_add_item, text="Salvar", command=salvar_item).pack(pady=10)

# Criar a janela principal
tela = tk.Tk()
tela.title("Programa de Estoque")
tela.geometry("800x400")
tela.configure(bg="blue")
tela.iconbitmap(default="assets/icone.ico")

# Frame para o menu lateral (sempre visível)
menu_lateral = tk.Frame(tela, bg="blue", width=200)
menu_lateral.place(x=0, y=0, relheight=1)  # Fixa o menu lateral à esquerda da tela

# Botões do menu lateral
tk.Button(menu_lateral, text="Exibir Estoque", width=20, command=exibir_estoque).pack(pady=10)
tk.Button(menu_lateral, text="Adicionar Item", width=20, command=adicionar_item).pack(pady=10)

# Frame para exibição do estoque
frame_estoque = tk.Frame(tela, bg="blue")
frame_estoque.place(x=200, y=0, relwidth=1, relheight=1)  # Exibir o estoque à direita

# Iniciar a interface
exibir_estoque()  # Mostrar o estoque ao iniciar
tela.mainloop()
