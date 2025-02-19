import sqlite3

def conectar():
    return sqlite3.connect('estoque.db')

def criar_tabela_produtos():
    with conectar() as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                estoque INTEGER NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

def obter_produtos():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, estoque FROM produtos")
        produtos = cursor.fetchall()
        
    return [{'id': produto[0], 'nome': produto[1], 'estoque': produto[2]} for produto in produtos]

def atualizar_estoque(produto_id, nova_quantidade):
    with conectar() as conn:
        c = conn.cursor()
        c.execute('UPDATE produtos SET estoque = ? WHERE id = ?', (nova_quantidade, produto_id))

def obter_estoque(produto_id):
    conn = sqlite3.connect('estoque.db')  # Substitua pelo seu banco de dados correto
    cursor = conn.cursor()
    cursor.execute("SELECT estoque FROM produtos WHERE id = ?", (produto_id,))
    estoque = cursor.fetchone()
    conn.close()
    
    if estoque:
        return estoque[0]
    return 0  # Caso o produto não exista