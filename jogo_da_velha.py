import tkinter as tk
from tkinter import messagebox

# Função para iniciar o jogo
def iniciar_jogo():
    global player
    player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state=tk.NORMAL, bg="white")

# Função que controla os cliques nos botões
def click(row, col):
    global player
    if buttons[row][col]['text'] == "" and player:
        buttons[row][col].config(text=player, disabledforeground="black")
        if player == "X":
            buttons[row][col].config(bg="#FFDDC1")  # Cor de fundo para X
        else:
            buttons[row][col].config(bg="#BEE3DB")  # Cor de fundo para O

        if verificar_vencedor(player):
            messagebox.showinfo("Fim de Jogo", f"Jogador {player} venceu!")
            finalizar_jogo()
        elif verificar_empate():
            messagebox.showinfo("Fim de Jogo", "Empate!")
            finalizar_jogo()
        else:
            player = "O" if player == "X" else "X"

# Função para verificar se há um vencedor
def verificar_vencedor(p):
    # Verifica linhas
    for i in range(3):
        if all(buttons[i][j]['text'] == p for j in range(3)):
            return True
    # Verifica colunas
    for j in range(3):
        if all(buttons[i][j]['text'] == p for i in range(3)):
            return True
    # Verifica diagonais
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] == p:
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] == p:
        return True
    return False

# Função para verificar se há empate
def verificar_empate():
    return all(buttons[i][j]['text'] != "" for i in range(3) for j in range(3))

# Função para finalizar o jogo
def finalizar_jogo():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state=tk.DISABLED)

# Cria a janela principal
root = tk.Tk()
root.title("Jogo da Velha")
root.configure(bg="#2C3E50")  # Cor de fundo da janela principal

# Estilos globais
button_font = ('Helvetica', 24, 'bold')
button_bg = "#ECF0F1"
button_active_bg = "#95A5A6"
button_border_color = "#34495E"
button_border_width = 2

# Cria uma grade de botões
buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=button_font, width=5, height=2,
                                  bg=button_bg, activebackground=button_active_bg,
                                  borderwidth=button_border_width, relief="solid",
                                  highlightbackground=button_border_color,
                                  command=lambda i=i, j=j: click(i, j))
        buttons[i][j].grid(row=i, column=j, padx=5, pady=5)  # Espaçamento entre os botões

# Cria o botão para reiniciar o jogo
restart_button = tk.Button(root, text="Reiniciar", font=('Arial', 16), bg="#1ABC9C", fg="white",
                           activebackground="#16A085", width=15, command=iniciar_jogo)
restart_button.grid(row=3, column=0, columnspan=3, pady=10)  # Espaçamento vertical

# Inicia o jogo
iniciar_jogo()

# Inicia o loop da interface gráfica
root.mainloop()
