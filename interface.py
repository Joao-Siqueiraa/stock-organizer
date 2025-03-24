import tkinter as tk
from tkinter import Scrollbar
from produtos import adicionar_produto_janela, buscar_produtos_gui, reduzir_estoque, somar_estoque, resetar_estoque,apagar_produto
from database import obter_produtos, criar_tabela_produtos

def criar_interface():
    root = tk.Tk()
    root.title("Programa de Estoque")
    root.geometry("800x600")
    root.configure(bg="white")
    root.iconbitmap(default="assets/icone.ico")
        
    # Frame azul da esquerda (MENU)
    leftframe = tk.Frame(root, width=205, height=600, bg="MIDNIGHTBLUE", relief="raised")
    leftframe.place(x=0, y=1, relheight=1)

    # Frame azul da direita (CONTEÚDO)
    rightframe = tk.Frame(root, width=600, height=600, bg="MIDNIGHTBLUE", relief="raised")
    rightframe.place(x=210, y=1, relwidth=1, relheight=1)

    # Criando Canvas e Scrollbar dentro do rightframe
    canvas = tk.Canvas(rightframe, bg="MIDNIGHTBLUE")
    scrollbar = Scrollbar(rightframe, orient=tk.VERTICAL, command=canvas.yview)
    
    # Criando um Frame dentro do Canvas
    scrollable_frame = tk.Frame(canvas, bg="MIDNIGHTBLUE")

    # Configurar a barra de rolagem
    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    
    # Criar uma janela no Canvas que contém o Frame rolável
    canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Posicionar Canvas e Scrollbar corretamente
    canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.configure(yscrollcommand=scrollbar.set)
    
    def atualizar_lista_produtos(frame, canvas):
        produtos = obter_produtos()

        # Limpa a área antes de atualizar
        for widget in frame.winfo_children(): 
            widget.destroy()

        for item in produtos:
            frame_produto = tk.Frame(frame, bg="MIDNIGHTBLUE")
            frame_produto.pack(fill="x", padx=5, pady=5)

            item_id = item["id"]
            nome_produto = item["nome"]
            estoque = item["estoque"]

            label = tk.Label(frame_produto, text=f"{nome_produto}, Estoque: {estoque}", font=("Century Gothic", 12), bg="MIDNIGHTBLUE", fg="white")
            label.pack(padx=5, pady=5)

            frame_entry_button = tk.Frame(frame_produto, bg="MIDNIGHTBLUE")
            frame_entry_button.pack(pady=5)

            reduzir_entry = tk.Entry(frame_entry_button, width=5)
            reduzir_entry.pack(side=tk.LEFT, padx=2)

            reduzir_button = tk.Button(frame_entry_button, text="-", font=("Century Gothic", 10), width=2, height=0, command=lambda id=item_id, entry=reduzir_entry: reduzir_estoque(id, entry))
            reduzir_button.pack(side=tk.LEFT, padx=2)

            somar_button = tk.Button(frame_entry_button, text="+", font=("Century Gothic", 10), width=2, height=0, command=lambda id=item_id, entry=reduzir_entry: somar_estoque(id, entry))
            somar_button.pack(side=tk.LEFT, padx=2)

            apagar_button = tk.Button(frame_entry_button, text="Apagar", font=("Century Gothic", 10), command=lambda id=item_id: apagar_produto(id))
            apagar_button.pack(side=tk.LEFT, padx=5)

    # Botão de adicionar produto
    botaoadd = tk.Button(leftframe, text="Add item", width=20, command=adicionar_produto_janela)
    botaoadd.place(x=10, y=10)

    # Caixa de pesquisa
    tk.Label(leftframe, text='Pesquisar produto', font=("Century Gothic", 12), bg="MIDNIGHTBLUE", fg="white").place(x=10, y=60)
    pesquisa_entry = tk.Entry(leftframe, font=("Century Gothic", 12))
    pesquisa_entry.place(x=10, y=100)

    # Botão de busca
    pesquisa_button = tk.Button(leftframe, text="Buscar", font=("Century Gothic", 12), command=lambda: buscar_produtos_gui(pesquisa_entry, scrollable_frame))
    pesquisa_button.place(x=10, y=130)

    # Botão para atualizar a página
    atualizar_button = tk.Button(leftframe, text="Atualizar Página", font=("Century Gothic", 12), command=lambda: atualizar_lista_produtos(scrollable_frame, canvas))
    atualizar_button.place(x=10, y=180)

    # Atualizar a lista de produtos inicialmente
    atualizar_lista_produtos(scrollable_frame, canvas)

    root.mainloop()
