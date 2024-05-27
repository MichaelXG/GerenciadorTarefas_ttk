from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from pages.Tarefas.FormTarefa import tarefas
from Controllers.PadraoController import *

def listar_tarefas():
    
    def aplicar_filtros():
        # Obter os valores dos filtros
        prioridade_filtro = prioridade_var.get()
        categoria_filtro  = categoria_var.get()
        concluida_filtro  = concluida_var.get()
        
        # Limpar a Treeview
        for item in tree.get_children():
            tree.delete(item)
        
        # Adicionar as linhas filtradas com os dados das tarefas
        for tarefa in tarefas:
            if (prioridade_filtro == "Todas" or tarefa["Prioridade"] == prioridade_filtro) and \
               (categoria_filtro == "Todas" or tarefa["Categoria"] == categoria_filtro) and \
               (concluida_filtro == "Todas" or ("Sim" if tarefa["Concluida"] else "Não") == concluida_filtro):
                tree.insert("", "end", text="", values=(
                    tarefa["ID"], tarefa["Nome"], tarefa["Descricao"], tarefa["Prioridade"], tarefa["Categoria"], 
                    "Sim" if tarefa["Concluida"] else "Não"))

    listar_janela = Toplevel()
    listar_janela.title("Lista de Tarefas")
    listar_janela.geometry("800x400")

    # Adicionar "Todas" às listas de opções
    prioridades_p.insert(0, "Todas")
    categorias_p.insert(0, "Todas")
    concluida_p.insert(0, "Todas")

    # Criar o Frame para os filtros
    filtros_frame = Frame(listar_janela)
    filtros_frame.pack(side=TOP, fill=X)

    # Filtros de Prioridade
    Label(filtros_frame, text="Prioridade:").pack(side=LEFT, padx=5)
    prioridade_var = StringVar(value="Todas")
    prioridade_menu = OptionMenu(filtros_frame, prioridade_var, *prioridades_p)
    prioridade_menu.pack(side=LEFT, padx=5)

    # Filtros de Categoria
    Label(filtros_frame, text="Categoria:").pack(side=LEFT, padx=5)
    categoria_var = StringVar(value="Todas")
    categoria_menu = OptionMenu(filtros_frame, categoria_var, *categorias_p)
    categoria_menu.pack(side=LEFT, padx=5)

    # Filtros de Concluída
    Label(filtros_frame, text="Concluída:").pack(side=LEFT, padx=5)
    concluida_var = StringVar(value="Todas")
    concluida_menu = OptionMenu(filtros_frame, concluida_var, *concluida_p)
    concluida_menu.pack(side=LEFT, padx=5)

    # Botão para aplicar filtros
    Button(filtros_frame, text="Aplicar Filtros", command=aplicar_filtros).pack(side=LEFT, padx=5)

    # Criar o Frame para a Treeview
    tree_frame = Frame(listar_janela)
    tree_frame.pack(expand=YES, fill=BOTH)

    # Criar o Treeview
    tree = Treeview(tree_frame, style="Custom.Treeview")

    # Estilo da Treeview
    style = Style()
    style.map("Custom.Treeview", background=[("selected", "#0080ff")])
    
   # Definir a cor para as tarefas concluídas
    tree.tag_configure("concluida", background="#c8e6c9")
    
    # Definir as colunas
    tree["columns"] = ("ID", "Nome", "Descricao", "Prioridade", "Categoria", "Concluida")

    # Formatar as colunas
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

    # Adicionar as linhas com os dados das tarefas
    for tarefa in tarefas:
        tree.insert("", "end", text="", values=(
            tarefa["ID"], tarefa["Nome"], tarefa["Descricao"], tarefa["Prioridade"], tarefa["Categoria"], 
            "Sim" if tarefa["Concluida"] else "Não"))

    # Adicionar um scrollbar
    scrollbar = Scrollbar(tree_frame, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Exibir o Treeview
    tree.pack(expand=YES, fill=BOTH)
