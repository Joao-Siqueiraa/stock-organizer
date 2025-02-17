from tkinter import messagebox
from estoque import atualizar_produto

def registrar_venda(produto_id, quantidade_vendida):
    if atualizar_produto(produto_id, quantidade_vendida):
        messagebox.showinfo('Venda Confirmada', f'{quantidade_vendida} unidades vendidas com sucesso!')
        return True
    else:
        messagebox.showwarning('Estoque Insuficiente', 'Quantidade vendida maior que o estoque disponível.')
        return False
