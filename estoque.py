from database import obter_produtos, atualizar_estoque

def verificar_estoque(produto_id):
    produtos = obter_produtos()
    for produto in produtos:
        if produto['id'] == produto_id:
            return produto['estoque']
    return 0

def atualizar_produto(produto_id, quantidade_vendida):
    estoque_atual = verificar_estoque(produto_id)
    if estoque_atual >= quantidade_vendida:
        nova_quantidade = estoque_atual - quantidade_vendida
        atualizar_estoque(produto_id, nova_quantidade)
        return True
    return False
