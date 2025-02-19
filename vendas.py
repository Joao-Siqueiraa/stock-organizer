import tkinter.messagebox
from estoque import verificar_estoque

def subtrair_estoque(produto_nome, quantidade):
    estoque_atual = verificar_estoque(produto_nome)
    
    if quantidade <= 0:
        tkinter.messagebox.showwarning("Valor inválido", "A quantidade deve ser maior que 0.")
        return False

    if estoque_atual >= quantidade:
        novo_estoque = estoque_atual - quantidade
        # Aqui você colocaria o código de atualização do estoque no banco
        return novo_estoque
    else:
        tkinter.messagebox.showwarning("Erro", "Estoque insuficiente!")
        return False
