import tkinter as tk
from tkinter import messagebox
import Database as db

def excluirAluno():
    janela = tk.Toplevel()
    janela.title("Excluir aluno")
    janela.geometry("400x220")
    janela.resizable(False, False)
    janela.grab_set()

    tk.Label(janela, text="Excluir Aluno", font=("Arial", 14, "bold")).pack(pady=15)
    tk.Label(janela, text="Digite o ID do aluno que deseja excluir:", font=("Arial", 11)).pack(pady=(10, 2))

    id_entry = tk.Entry(janela, width=30)
    id_entry.pack()
    id_entry.focus()

    def confirmarExclusao():
        id_aluno = id_entry.get().strip()

        if not id_aluno:
            messagebox.showwarning("Aviso", "Preencha o campo!", parent=janela)
            return

        if not id_aluno.isdigit():
            messagebox.showwarning("Aviso", "O ID deve ser um número!", parent=janela)
            return

        resposta = messagebox.askyesno(
            "Confirmar exclusão",
            f"Tem certeza que deseja excluir o aluno de ID {id_aluno}?",
            parent=janela
        )

        if not resposta: 
            return

        try:
            sucesso = db.db_Excluir(id_aluno)

            if sucesso:
                messagebox.showinfo("Sucesso", "Aluno excluído com sucesso!", parent=janela)
                janela.destroy()
            else:
                messagebox.showinfo("Não encontrado", "Nenhum aluno encontrado com esse ID!", parent=janela)

        except Exception as i:
            messagebox.showerror("Erro", f"Erro ao excluir:\n{i}", parent=janela)

    tk.Button(janela, text="Excluir", width=25, command=confirmarExclusao).pack(pady=15)
    tk.Button(janela, text="Fechar", width=15, command=janela.destroy).pack(pady=5)