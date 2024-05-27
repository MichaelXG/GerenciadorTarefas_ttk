from tkinter import *
from tkinter.ttk import *
from Controllers.PadraoController import *
from pages.Tarefas.FormTarefa import nova_tarefa
from pages.Tarefas.FormListarTarefa import listar_tarefas
from pages.Tarefas.FormConcluirTarefa import tela_concluir_tarefa

def sair():
    janela_main.destroy()

def sair_aplicacao():
    janela_main.quit()

def sobre():
    print("Sobre esta aplicação")

# Criar a janela principal
janela_main = Tk()
janela_main.geometry("800x400")
janela_main.title("Gerenciador de Tarefas")

# Criação do menu
menu_bar = Menu(janela_main)

# Menu tarefa
menu_tarefa = Menu(menu_bar, tearoff=0)
menu_tarefa.add_command(label="Novo", command=lambda: nova_tarefa(janela_main))
menu_tarefa.add_command(label="Listar", command= listar_tarefas)
menu_tarefa.add_command(label="Concluir", command= tela_concluir_tarefa)
menu_tarefa.add_separator()
menu_tarefa.add_command(label="Sair", command=sair)
menu_bar.add_cascade(label="Menu", menu=menu_tarefa)

# Menu Ajuda
menu_ajuda = Menu(menu_bar, tearoff=0)
menu_ajuda.add_command(label="Sobre", command=sobre)
menu_bar.add_cascade(label="Ajuda", menu=menu_ajuda)

# Adiciona o menu à janela
janela_main.config(menu=menu_bar)

janela_main.mainloop()
