'''
Class for do PadraoController
'''
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

# Lista para armazenar as tarefas
tarefas = []

tarefas = [{"ID":1,"Nome":'Mercado',"Descricao": 'Comprar itens de limpeza',"Prioridade": 'Média',"Categoria": 'Casa',"Concluida": False},
           {"ID":2,"Nome":'Farmacia',"Descricao": 'Comprar desloratadina',"Prioridade": 'Alta',"Categoria": 'Saúde',"Concluida": False},
           {"ID":3,"Nome":'Horti',"Descricao": 'Comprar legumes',"Prioridade": 'Alta',"Categoria": 'Casa',"Concluida": False},
           {"ID":4,"Nome":'Python',"Descricao": 'Concluir o Projeto',"Prioridade": 'Alta',"Categoria": 'Estudo',"Concluida": False},
           {"ID":5,"Nome":'Daily',"Descricao": 'Daily com o time geral',"Prioridade": 'Média',"Categoria": 'Trabalho',"Concluida": False},
           {"ID":6,"Nome":'Tiros',"Descricao": 'Ir ao clube de tiro para manter habitualizade',"Prioridade": 'Média',"Categoria": 'Lazer',"Concluida": False},
           {"ID":7,"Nome":'Resenha',"Descricao": 'resenha qualquer',"Prioridade": 'Baixa',"Categoria": 'Outros',"Concluida": False},
           ]

# Paramentros para cadastro
prioridades = ['Alta', 'Média', 'Baixa']
categorias = ['Trabalho', 'Estudo', 'Lazer', 'Casa', 'Saúde', 'Outros']

# Parametros para pesquisa
prioridades_p = ['Todas', 'Alta', 'Média', 'Baixa']

categorias_p = ['Todas', 'Trabalho', 'Estudo', 'Lazer', 'Casa', 'Saúde', 'Outros']

concluida_p =  ['Todas', 'Sim', 'Não']

