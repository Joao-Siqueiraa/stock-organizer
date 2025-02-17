import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('estoque.db')
cursor = conn.cursor()

# Criar a tabela ESTOQUE, se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS ESTOQUE (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Quantidade INTEGER NOT NULL DEFAULT 0
);
""")

# Confirmar as mudanças e fechar a conexão
conn.commit()

# Verificar se a tabela foi criada corretamente
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='ESTOQUE';")
tabela = cursor.fetchone()
if tabela:
    print("Tabela ESTOQUE criada com sucesso!")
else:
    print("Erro ao criar a tabela ESTOQUE.")

conn.close()
