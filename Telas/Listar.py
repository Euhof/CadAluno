import tkinter as tk
from tkinter import ttk, messagebox
import Database as db

def listarAlunos():
    Colunas = ("ID", "Nome", "Idade", "Email")

    janela = tk.Toplevel()
    janela.title("Lista de Alunos")
    janela.geometry("650x400")
    janela.resizable(False, False)

    tk.Label(janela, text="Alunos Cadastrados", font=("Arial", 14, "bold")).pack(pady=10)

    frameTabela = tk.Frame(janela)
    frameTabela.pack(fill="both", expand=True, padx=10, pady=5)
    tabela = ttk.Treeview(frameTabela, columns=Colunas, show="headings")

    for col in Colunas:
        tabela.heading(col, text=col)
        tabela.column(col, width=150, anchor="center")

    try:
        Resultados = db.db_Listar()
        if not Resultados:
            messagebox.showinfo("Aviso", "Nenhum aluno encontrado!", parent=janela)
        else:
            for aluno in Resultados:
                tabela.insert("", tk.END, values=aluno)

    except Exception as i:
        messagebox.showerror("Erro", f"Erro ao buscar alunos:\n{i}", parent=janela)

    scrollbar = ttk.Scrollbar(frameTabela, orient="vertical", command=tabela.yview)
    tabela.configure(yscrollcommand=scrollbar.set)

    tabela.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    tk.Button(janela, text="Fechar", width=15, command=janela.destroy).pack(pady=10)