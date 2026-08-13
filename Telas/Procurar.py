import tkinter as tk
from tkinter import messagebox
import Database as db

def procurarAluno():
    janela = tk.Toplevel()
    janela.title("Procurar aluno")
    janela.geometry("400x250")
    janela.resizable(False, False)
    janela.grab_set()
    
    tk.Label(janela, text="Digite o ID do aluno para procurar:", font=("Arial", 11)).pack(pady=(10, 2))
    Procura = tk.Entry(janela, width=30)
    Procura.pack()
    Procura.focus()
    
    def Encontrar():
        Id = Procura.get().strip()
    
        if not Id:
            messagebox.showwarning("Aviso", "Preencha o campo!", parent=janela)
            return
        
        if not Id.isdigit():
            messagebox.showwarning("Aviso", "O Id deve ser um número!", parent=janela)
            return
        try:
            Resultado = db.db_Procurar(Id)
            if Resultado:
                messagebox.showinfo("Aluno encontrado!", 
                f"ID:{Resultado[0]}\nNome:{Resultado[1]}\nIdade:{Resultado[2]}\nEmail:{Resultado[3]}",
                parent=janela)
                janela.destroy()
            else:
                messagebox.showinfo("Não encontrado", "O aluno não foi encontrado!", parent=janela)
                janela.destroy()
        except Exception as i:
            messagebox.showerror("Erro", f"Erro ao procurar:\n{i}", parent=janela)
        
    tk.Button(janela, text="Procurar", width=25, command=Encontrar).pack(pady=15)
    tk.Button(janela, text="Fechar", width=15, command=janela.destroy).pack(pady=5)
