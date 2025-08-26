# Atividade – Validador de Senha
# Objetivo:
#  Criar um programa em Python que verifique se uma senha digitada pelo usuário é válida, utilizando estruturas condicionais (if e else).
# Descrição do problema:
#  Você deve desenvolver um programa que peça ao usuário para digitar uma senha. O programa deve verificar se a senha atende às seguintes regras:
# A senha deve ter exatamente 8 caracteres.
# Caso a senha esteja correta, exibir a mensagem: "Senha válida!".
# Caso a senha não esteja correta, exibir a mensagem: "Senha inválida! Deve conter exatamente 8 caracteres.".


# Requisitos do programa:
# Utilizar a função input() para ler a senha do usuário.
# Utilizar if e else para validar o tamanho da senha.
# Exibir a mensagem correta usando print() ou messagebox (se estiver usando Tkinter).

import tkinter as tk
from tkinter import messagebox

def verificar_senha():
    senha = entry_senha.get()  # Pega a senha digitada pelo usuário
    
    if len(senha) == 8:
        messagebox.showinfo("Resultado", "Senha válida!")
    else:
        messagebox.showerror("Erro", "Senha inválida! Deve conter exatamente 8 caracteres.")

# Criando a janela principal
root = tk.Tk()
root.title("Validador de Senha")
root.geometry("300x200")
root.configure(bg="#f0f0f0")

# Rótulo
tk.Label(root, text="Digite sua senha:", bg="#f0f0f0", font=("Arial", 14)).pack(pady=15)

# Campo de entrada
entry_senha = tk.Entry(root, show="*")  # 'show="*"' oculta a senha digitada
entry_senha.pack(pady=5)

# Botão de verificação
tk.Button(root, text="Verificar", command=verificar_senha, bg="blue", fg="white", font=("Arial", 12, "bold")).pack(pady=20)

# Inicia a interface
root.mainloop()
