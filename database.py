import sqlite3

def init_db():
    """
    Inicializa o banco de dados e cria as tabelas necessárias.
    """
    conn = sqlite3.connect('presentes.db')
    cursor = conn.cursor()

    # Criação da tabela de presentes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS presentes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            marca TEXT NOT NULL,
            cor TEXT NOT NULL,
            imageUrl TEXT NOT NULL
        )
    ''')

    # Criação da tabela de convidados
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS convidados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            email TEXT NOT NULL,
            presente_id INTEGER NOT NULL,
            FOREIGN KEY (presente_id) REFERENCES presentes(id)
        )
    ''')

    conn.commit()
    conn.close()

def adicionar_presente(nome, marca, cor, imageUrl):
    """
    Adiciona um novo presente ao banco de dados.
    """
    conn = sqlite3.connect('presentes.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO presentes (nome, marca, cor, imageUrl) 
        VALUES (?, ?, ?, ?)
    ''', (nome, marca, cor, imageUrl))
    conn.commit()
    conn.close()

def listar_presentes():
    """
    Retorna todos os presentes do banco de dados.
    """
    conn = sqlite3.connect('presentes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM presentes')
    presentes = cursor.fetchall()
    conn.close()
    
    return [{"id": p[0], "nome": p[1], "marca": p[2], "cor": p[3], "imageUrl": p[4]} for p in presentes]

def adicionar_convidado(nome, telefone, email, presente_id):
    """
    Adiciona um novo convidado que escolheu um presente ao banco de dados.
    """
    conn = sqlite3.connect('presentes.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO convidados (nome, telefone, email, presente_id) 
        VALUES (?, ?, ?, ?)
    ''', (nome, telefone, email, presente_id))
    conn.commit()
    conn.close()
    
def deletar_presente(presente_id):
    """
    Deleta um presente do banco de dados com base no ID fornecido.
    """
    conn = sqlite3.connect('presentes.db')  # Altere para o seu banco de dados
    cursor = conn.cursor()
    cursor.execute("DELETE FROM presentes WHERE id = ?", (presente_id,))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()  # Inicializa o banco de dados ao executar este arquivo
