import sqlite3

def conectar():
    return sqlite3.connect('estoque.db')

def criar_tabela_produtos():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def obter_produtos():
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT nome, quantidade FROM produtos')
    produtos = c.fetchall()
    conn.close()
    return produtos

def atualizar_estoque(produto_id, nova_quantidade):
    conn = conectar()
    c = conn.cursor()
    c.execute('UPDATE produtos SET quantidade = ? WHERE id = ?', (nova_quantidade, produto_id))
    conn.commit()
    conn.close()

