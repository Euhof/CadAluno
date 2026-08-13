import tkinter as tk
from Telas.Cadastro import telaCadastro
from Telas.Listar import listarAlunos
from Telas.Editar import editarAluno
from Telas.Procurar import procurarAluno
from Telas.Excluir import excluirAluno
import Database as db

def main():
    db.Cria_banco()

    root = tk.Tk()
    root.title("Menu - Sistema de Alunos")
    root.geometry("400x400")
    root.resizable(False, False)

    tk.Label(root, text="Sistema de Gerenciamento de Alunos", font=("Arial", 14, "bold")).pack(pady=20)

    tk.Button(root, text="Cadastrar aluno", width=25, command=telaCadastro).pack(pady=8)
    tk.Button(root, text="Listar alunos", width=25, command=listarAlunos).pack(pady=8)
    tk.Button(root, text="Procurar aluno por ID", width=25, command=procurarAluno).pack(pady=8)
    tk.Button(root, text="Editar dados de um aluno", width=25, command=editarAluno).pack(pady=8)
    tk.Button(root, text="Excluir aluno", width=25, command=excluirAluno).pack(pady=8)

    tk.Button(root, text="Sair", width=25, command=root.destroy, bg="#ffcccc").pack(pady=20)

    root.mainloop()