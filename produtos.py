import sqlite3
from tkinter import messagebox
import tkinter as tk
from database import obter_produtos, obter_estoque,conectar
from vendas import subtrair_estoque

# Função para adicionar produto ao banco de dados
def adicionar_produto(nome, estoque):
    try:
        # Conectando ao banco de dados
        conn = sqlite3.connect('estoque.db')  # AQUI O BANCO CORRETO
        c = conn.cursor()
        
        # Criando a tabela, caso não exista
        c.execute('''CREATE TABLE IF NOT EXISTS produtos
                     (id INTEGER PRIMARY KEY, nome TEXT, estoque INTEGER)''')
        
        # Inserindo o produto na tabela correta
        c.execute("INSERT INTO produtos (nome, estoque) VALUES (?, ?)", (nome, estoque))  # CORRIGIDO PARA produtos
        
        # Salvando e fechando a conexão
        conn.commit()
        conn.close()
        
        print("Produto salvo com sucesso!")  # Depuração

    except Exception as e:
        print(f"Erro ao salvar produto: {e}")  # Depuração


# Função para adicionar o produto com interface gráfica
def adicionar_produto_janela():
    # Janela de Adicionar Produto
    tl = tk.Toplevel()
    tl.title("Adicionar Produto")
    tl.geometry("900x800")
    tl.configure(bg='lightgray')

    # Label e Entry para o nome do produto
    tk.Label(tl, text="Nome", font=("Century Gothic", 12), bg='lightgray').pack(pady=5)
    nome_produto = tk.Entry(tl, font=("Century Gothic", 12))
    nome_produto.pack(pady=5)

    # Label e Entry para a quantidade do produto
    tk.Label(tl, text="Estoque:", font=("Century Gothic", 12), bg="lightgray").pack(pady=5)
    estoque_produto = tk.Entry(tl, font=("Century Gothic", 12))
    estoque_produto.pack(pady=5)

    def salvar_produto():
        nome = nome_produto.get().strip()
        estoque = estoque_produto.get().strip()

        if not nome or not estoque.isdigit():
            messagebox.showerror("Erro", "Nome inválido ou quantidade não numérica")
            return  # Sai da função sem salvar o produto errado

        # Chama a função para salvar o produto no banco de dados
        adicionar_produto(nome, int(estoque))
        
        # Confirmação de sucesso
        messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
        tl.destroy()

    tk.Button(tl, text="Salvar", font=("Century Gothic", 12), command=salvar_produto).pack(pady=10)

    tl.bind("<Return>", lambda event: salvar_produto())
    tl.mainloop()

def resetar_estoque(produto_id):
    with conectar() as conn:
        c = conn.cursor()
        c.execute("UPDATE produtos SET estoque = estoque_inicial WHERE id = ?", (produto_id,))
        conn.commit()


def somar_estoque(produto_id, reduzir_entry):
    try:
        quantidade = reduzir_entry.get()  # Pegando o valor da entry
        print(f"Valor da entry: {quantidade}")
        
        # Verificando se a entrada não está vazia
        if quantidade == "":
            messagebox.showerror("Erro", "Por favor, insira uma quantidade.")
            return
        
        quantidade = int(quantidade)  # Convertendo a entrada para um número inteiro
        
        # Verificando se a quantidade é maior que 0
        if quantidade <= 0:
            messagebox.showerror("Erro", "A quantidade deve ser maior que 0!")
            return
        
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido!")
        return

    # Obter o estoque atual do produto
    estoque_atual = obter_estoque(produto_id)
    
    # Verificar se há estoque suficiente
    if quantidade > estoque_atual:
        messagebox.showerror("Erro", "Estoque insuficiente!")
        return

    # Atualizar o estoque no banco de dados
    novo_estoque = estoque_atual + quantidade
    atualizar_estoque(produto_id, novo_estoque)
    
    # Exibir uma mensagem de sucesso
    messagebox.showinfo("Sucesso", f"Estoque aumentado com sucesso! Novo estoque: {novo_estoque}")



# Função para reduzir o estoque
def reduzir_estoque(produto_id, reduzir_entry):
    try:
        quantidade = reduzir_entry.get()  # Pegando o valor da entry
        print(f"Valor da entry: {quantidade}")
        
        # Verificando se a entrada não está vazia
        if quantidade == "":
            messagebox.showerror("Erro", "Por favor, insira uma quantidade.")
            return
        
        quantidade = int(quantidade)  # Convertendo a entrada para um número inteiro
        
        # Verificando se a quantidade é maior que 0
        if quantidade <= 0:
            messagebox.showerror("Erro", "A quantidade deve ser maior que 0!")
            return
        
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido!")
        return

    # Obter o estoque atual do produto
    estoque_atual = obter_estoque(produto_id)
    
    # Verificar se há estoque suficiente
    if quantidade > estoque_atual:
        messagebox.showerror("Erro", "Estoque insuficiente!")
        return

    # Atualizar o estoque no banco de dados
    novo_estoque = estoque_atual - quantidade
    atualizar_estoque(produto_id, novo_estoque)
    
    # Exibir uma mensagem de sucesso
    messagebox.showinfo("Sucesso", f"Estoque reduzido com sucesso! Novo estoque: {novo_estoque}")

# Função para buscar produtos
def buscar_produtos_gui(entry, frame):
    busca = entry.get().strip().lower()
    produtos = obter_produtos()

    # Limpar o frame antes de adicionar os produtos
    for widget in frame.winfo_children():
        widget.destroy()

    # Filtrar e mostrar os produtos que contêm a busca no nome
    for item in produtos:
        if busca in item["nome"].lower():
            frame_produto = tk.Frame(frame, bg="MIDNIGHTBLUE")
            frame_produto.pack(fill="x", padx=5, pady=5)

            item_id = item["id"]
            nome_produto = item["nome"]
            estoque = item["estoque"]

            label = tk.Label(frame_produto, text=f"{nome_produto}, Estoque: {estoque}", font=("Century Gothic", 12), bg="MIDNIGHTBLUE", fg='white')
            label.pack(padx=5,pady=12,anchor="w")
            label.lower()
            frame_entry_button = tk.Frame(frame_produto, bg="MIDNIGHTBLUE")  
            frame_entry_button.place(x=500,y=5)
        
            reduzir_entry = tk.Entry(frame_produto, width=5)
            reduzir_entry.pack(side=tk.LEFT, padx=2)
            reduzir_entry.lift()
            reduzir_button = tk.Button(frame_produto, text="-", font=("Century Gothic", 10), width=2, height=0, command=lambda id=item_id, entry=reduzir_entry: reduzir_estoque(id, entry))
            reduzir_button.pack(side=tk.LEFT,padx=2)
            somar_button = tk.Button(frame_produto,text="+",font=("Century Gothic", 10),width=2, height=0, command=lambda id=item_id, entry=reduzir_entry: somar_estoque(id, entry))
            somar_button.pack(side=tk.LEFT, padx=2)

# Função para atualizar o estoque
def atualizar_estoque(produto_id, novo_estoque):
    conn = sqlite3.connect('estoque.db')  # Substitua pelo seu banco de dados correto
    cursor = conn.cursor()
    cursor.execute("UPDATE produtos SET estoque = ? WHERE id = ?", (novo_estoque, produto_id))
    conn.commit()
    conn.close()

import sqlite3
from tkinter import messagebox

def apagar_produto(produto_id):
    confirmacao = messagebox.askyesno("Confirmação", "Tem certeza que deseja apagar este produto?")
    
    if confirmacao:
        conexao = sqlite3.connect('estoque.db')
        cursor = conexao.cursor()

        try:
            cursor.execute("DELETE FROM produtos WHERE id = ?", (produto_id,))
            conexao.commit()
            messagebox.showinfo("Sucesso", "Produto apagado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível apagar o produto: {e}")
        finally:
            conexao.close()
