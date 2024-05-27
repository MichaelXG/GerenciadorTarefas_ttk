from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from Controllers.PadraoController import *

def nova_tarefa(janela):
    
    def obter_proximo_id():
        if not tarefas:
            return 1
        return max(tarefa["ID"] for tarefa in tarefas) + 1
    
    def adicionar_tarefa(nome, descricao, prioridade, categoria):
        proximo_id = obter_proximo_id()
        
        tarefa = {
            "ID": proximo_id,
            "Nome": nome,
            "Descricao": descricao,
            "Prioridade": prioridade,
            "Categoria": categoria,
            "Concluida": False
        }
        tarefas.append(tarefa)
        messagebox.showinfo("Sucesso", "Tarefa adicionada com sucesso!")
        
        # Limpar os campos após adicionar a tarefa
        txt_nome.set("")
        txt_descricao.set("")
        txt_prioridade.set("")
        txt_categoria.set("")

    nova_janela = Toplevel(janela)
    nova_janela.title("Adicionar Tarefas")
    nova_janela.geometry("700x300")

    # Nome da tarefa
    txt_nome = StringVar()
    Label(nova_janela, text="Nome da tarefa:").grid(row=0, column=0, padx=10, pady=5)
    nome = Entry(nova_janela, width=30, textvariable=txt_nome)
    nome.grid(row=0, column=1, padx=10, pady=5)

    # Descricao da tarefa
    txt_descricao = StringVar()
    Label(nova_janela, text="Descricao da tarefa").grid(row=0, column=2, padx=10, pady=5)
    descricao = Entry(nova_janela, width=30, textvariable=txt_descricao)
    descricao.grid(row=0, column=3, padx=10, pady=5)

    # Prioridade
    txt_prioridade = StringVar()
    Label(nova_janela, text="Prioridade").grid(row=1, column=0, padx=10, pady=5)
    prioridade = Combobox(nova_janela, values=prioridades, textvariable=txt_prioridade)
    prioridade.grid(row=1, column=1, padx=10, pady=5)

    # Categoria
    txt_categoria = StringVar()
    Label(nova_janela, text="Categoria").grid(row=1, column=2, padx=10, pady=5)
    categoria = Combobox(nova_janela, values=categorias, textvariable=txt_categoria)
    categoria.grid(row=1, column=3, padx=10, pady=5)

    # Salvar tarefa
    btn_salvar = Button(nova_janela, text="Salvar", command=lambda: adicionar_tarefa(txt_nome.get(), txt_descricao.get(), txt_prioridade.get(), txt_categoria.get()))
    btn_salvar.grid(row=2, column=1, padx=10, pady=10, sticky=W)
