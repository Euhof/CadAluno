from tkinter import messagebox
from Menu import main

if __name__ == "__main__":
    try:
        main()
    except Exception as i:
        messagebox.showerror("Erro", f"Ocorreu um erro: {i}")