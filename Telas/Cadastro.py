import tkinter as tk, Database as db
from tkinter import messagebox

def telaCadastro():
    janela = tk.Toplevel()
    janela.title("Cadastrar aluno")
    janela.geometry("400x380")
    janela.resizable(False, False)
    janela.grab_set()  

    tk.Label(janela, text="Cadastro de Alunos", font=("Arial", 14, "bold")).pack(pady=15)

    tk.Label(janela, text="Nome do aluno:", font=("Arial", 11)).pack(pady=(10, 2))
    nomeE = tk.Entry(janela, width=30)
    nomeE.pack()
    nomeE.focus()

    tk.Label(janela, text="Idade do aluno:", font=("Arial", 11)).pack(pady=(10, 2))
    idadeE = tk.Entry(janela, width=30)
    idadeE.pack()

    tk.Label(janela, text="Email do aluno:", font=("Arial", 11)).pack(pady=(10, 2))
    emailE= tk.Entry(janela, width=30)
    emailE.pack()

    def finalizar_cadastro():
        nome = nomeE.get().strip()
        idade = idadeE.get().strip()
        email = emailE.get().strip()

        if not nome or not idade or not email:
            messagebox.showwarning("Aviso", "Preencha todos os campos!", parent=janela)
            return

        if not idade.isdigit():
            messagebox.showwarning("Aviso", "Idade deve ser um número!", parent=janela)
            return

        try:
            db.db_cadastrar(nome, int(idade), email)
            messagebox.showinfo(
                "Sucesso",
                f"Aluno cadastrado!\n\nNome: {nome}\nIdade: {idade}\nEmail: {email}",
                parent=janela
            )
            janela.destroy()
        except Exception as i:
            messagebox.showerror("Erro", f"Erro ao cadastrar:\n{i}", parent=janela)

    tk.Button(janela, text="Finalizar cadastro", width=25, command=finalizar_cadastro).pack(pady=15)
    tk.Button(janela, text="Fechar", width=15, command=janela.destroy).pack(pady=5)