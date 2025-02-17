from database import obter_produtos

def listar_produtos():
    return obter_produtos()

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
