import sqlite3 as sql

conexao = sql.connect('MeuBanco.db')
cursor = conexao.cursor()

def Cria_banco():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Alunos (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome TEXT NOT NULL,
            Idade INTEGER,
            Email TEXT UNIQUE
        )
    """)
    conexao.commit()

def db_cadastrar(Nome, Idade, Email):
    cursor.execute(
         "INSERT INTO Alunos ( Nome, Idade, Email) VALUES ( ?, ?, ?)",
         ( Nome, Idade, Email)
    )
    conexao.commit()
    

def db_Listar():
    cursor.execute(
        "SELECT * FROM Alunos"
    )
    resultados = cursor.fetchall()

    if not resultados:
        return []          
    
    return resultados
    
def db_Editar(P, Nnome, Nidade, Nemail):
    cursor.execute(
        "UPDATE Alunos SET Nome = ?, Idade = ?, Email = ? WHERE Id = ?",
        (Nnome, Nidade, Nemail, P)
    ) 
    conexao.commit()
    print("Aluno alterado com sucesso!")
    
def db_Procurar(id):
    cursor.execute(
        "SELECT * FROM Alunos WHERE Id = ?", (id,)
    )
    resultado = cursor.fetchone()
    
    if not resultado:
        return []  
    
    return resultado
    
def db_Excluir(id_aluno):
    try:
        cursor.execute("DELETE FROM Alunos WHERE Id = ?", (id_aluno,))
        conexao.commit()

        if cursor.rowcount > 0:
            return True  
        else:
            return False  

    except Exception as i:
        print(f"Erro ao excluir: {i}")
        raise