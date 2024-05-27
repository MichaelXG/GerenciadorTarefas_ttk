from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from Controllers.PadraoController import *

def atualizar_treeview(tree):
    # Limpar todas as linhas da Treeview
    for item in tree.get_children():
        tree.delete(item)
    
    # Adicionar as linhas com os dados das tarefas não concluídas
    for tarefa in tarefas:
        if not tarefa["Concluida"]:
            tree.insert("", "end", text="", values=(
                tarefa["ID"], tarefa["Nome"], tarefa["Descricao"], tarefa["Prioridade"], tarefa["Categoria"],  "Sim" if tarefa["Concluida"] else "Não"))

def tela_concluir_tarefa():
    concluir_janela = Toplevel()
    concluir_janela.title("Concluir Tarefa")
    concluir_janela.geometry("700x500")
    
    # Obter os IDs das tarefas não concluídas
    tarefas_nao_concluidas = [tarefa["ID"] for tarefa in tarefas if not tarefa["Concluida"]]
    
    # Criar o combobox com os IDs das tarefas não concluídas
    Label(concluir_janela, text="ID Tarefa:").grid(row=0, column=0, padx=10, pady=5)
    tarefas_combo = Combobox(concluir_janela, width=50, values=tarefas_nao_concluidas)
    tarefas_combo.grid(row=0, column=1, padx=10, pady=5)
    
    # Criar o Frame para a Treeview de tarefas não concluídas
    tree_frame = Frame(concluir_janela)
    tree_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

    # Criar o Treeview para exibir as tarefas não concluídas
    tree = Treeview(tree_frame, columns=("ID", "Nome", "Descricao", "Prioridade", "Categoria", "Concluida"))
    
    # Definir as colunas
    tree.column("#0", width=0, stretch=NO)  # Coluna oculta
    tree.column("ID", width=50)
    tree.column("Nome", width=150)
    tree.column("Descricao", width=200)
    tree.column("Prioridade", width=100)
    tree.column("Categoria", width=100)
    tree.column("Concluida", width=100)

    # Definir os cabeçalhos das colunas
    tree.heading("#0", text="", anchor=W)
    tree.heading("ID", text="ID", anchor=W)
    tree.heading("Nome", text="Nome", anchor=W)
    tree.heading("Descricao", text="Descricao", anchor=W)
    tree.heading("Prioridade", text="Prioridade", anchor=W)
    tree.heading("Categoria", text="Categoria", anchor=W)
    tree.heading("Concluida", text="Concluida", anchor=W)

    # Adicionar as linhas com os dados das tarefas não concluídas
    atualizar_treeview(tree)

    # Adicionar um scrollbar
    scrollbar = Scrollbar(tree_frame, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Exibir o Treeview
    tree.pack(expand=YES, fill=BOTH)

    # Função para concluir a tarefa selecionada no combobox
    def concluir_tarefa(id_tarefa):
        id_tarefa = int(id_tarefa)
        for tarefa in tarefas:
            if tarefa["ID"] == id_tarefa:
                tarefa["Concluida"] = True
                messagebox.showinfo("Sucesso", f"Tarefa {id_tarefa} Concluída com sucesso!")
                # Trazer a janela de concluir tarefa para a frente novamente
                concluir_janela.lift()
                # Atualizar a lista de tarefas na tela de concluir tarefa
                tarefas_nao_concluidas.remove(id_tarefa)
                tarefas_combo["values"] = tarefas_nao_concluidas
                atualizar_treeview(tree)
                # Limpar o combobox
                tarefas_combo.set('')
                break
    
    concluir_button = Button(concluir_janela, text="Concluir", command=lambda: concluir_tarefa(tarefas_combo.get()))
    concluir_button.grid(row=0, column=2, padx=10, pady=5)
