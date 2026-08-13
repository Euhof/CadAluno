import tkinter as tk
from tkinter import messagebox
import Database as db

def editarAluno():
    janela = tk.Toplevel()
    janela.title("Editar aluno")
    janela.geometry("400x220")
    janela.resizable(False, False)
    janela.grab_set()

    tk.Label(janela, text="Editar Aluno", font=("Arial", 14, "bold")).pack(pady=15)
    tk.Label(janela, text="Digite o ID do aluno que deseja editar:", font=("Arial", 11)).pack(pady=(10, 2))

    Procura = tk.Entry(janela, width=30)
    Procura.pack()
    Procura.focus()

    def buscar_aluno():
        id_aluno = Procura.get().strip()

        if not id_aluno:
            messagebox.showwarning("Aviso", "Preencha o campo!", parent=janela)
            return

        if not id_aluno.isdigit():
            messagebox.showwarning("Aviso", "O ID deve ser um número!", parent=janela)
            return

        try:
            resultado = db.db_Procurar(id_aluno)

            if not resultado:
                messagebox.showinfo("Não encontrado", "O aluno não foi encontrado!", parent=janela)
                return

            janela.destroy()
            abrirTelaEdicao(resultado)

        except Exception as i:
            messagebox.showerror("Erro", f"Erro ao procurar:\n{i}", parent=janela)

    tk.Button(janela, text="Buscar", width=25, command=buscar_aluno).pack(pady=15)
    tk.Button(janela, text="Fechar", width=15, command=janela.destroy).pack(pady=5)


def abrirTelaEdicao(aluno):
    id_aluno, nome_atual, idade_atual, email_atual = aluno

    janela = tk.Toplevel()
    janela.title("Editando aluno")
    janela.geometry("400x380")
    janela.resizable(False, False)
    janela.grab_set()

    tk.Label(janela, text=f"Editando aluno ID: {id_aluno}", font=("Arial", 14, "bold")).pack(pady=15)

    tk.Label(janela, text="Nome:", font=("Arial", 11)).pack(pady=(8, 2))
    nome_entry = tk.Entry(janela, width=30)
    nome_entry.insert(0, nome_atual)   
    nome_entry.pack()

    tk.Label(janela, text="Idade:", font=("Arial", 11)).pack(pady=(8, 2))
    idade_entry = tk.Entry(janela, width=30)
    idade_entry.insert(0, idade_atual)
    idade_entry.pack()

    tk.Label(janela, text="Email:", font=("Arial", 11)).pack(pady=(8, 2))
    email_entry = tk.Entry(janela, width=30)
    email_entry.insert(0, email_atual)
    email_entry.pack()

    def salvar_edicao():
        nome = nome_entry.get().strip()
        idade = idade_entry.get().strip()
        email = email_entry.get().strip()
    
        if not nome or not idade or not email:
            messagebox.showwarning("Aviso", "Preencha todos os campos!", parent=janela)
            return
    
        if not idade.isdigit():
            messagebox.showwarning("Aviso", "Idade deve ser um número!", parent=janela)
            return
    
        try:
            db.db_Editar(id_aluno, nome, int(idade), email)
            messagebox.showinfo("Sucesso", "Aluno alterado com sucesso!", parent=janela)
            janela.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao editar:\n{e}", parent=janela)
    
    tk.Button(janela, text="Salvar alterações", width=25, command=salvar_edicao).pack(pady=20)
    tk.Button(janela, text="Cancelar", width=15, command=janela.destroy).pack(pady=5)