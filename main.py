
from graph import *
from utils import *
import sys

class main:
    def __init__(self):
        print('Trabalho Inteligência Artificial ESTGV 2019/2020')
    
    def menu(self):
        print("************MAIN MENU**************")
        print()

        choice = input("""
                      1: Custo Uniforme
                      2: Em profundidade limitada
                      3: Procura sôfrega
                      4: A*
                      0: Sair

                      Please enter your choice: """)

        if choice == "1":
            mainprogram.uniform_cost_search()
        elif choice == "2":
            mainprogram.depth_Limited_Search()
        elif choice == "3" :
            mainprogram.Greedy_Search()
        elif choice=="4":
            mainprogram.A_Star_Search()
        elif choice=="0":
            sys.exit
        else:
            print("You must only select either 1,2,3, or 4.")
            print("Please try again")

    def uniform_cost_search(self):
        graph = Graph()
        funcUtils = utils()
        funcUtils.read_file_first_space('Cidades_grafo.txt',graph)
        funcUtils.read_file_and_connect('Cidades_grafo.txt',graph)
        funcUtils.uniform_cost_search_util(graph,'Lisboa','Viseu',verbose=True)
    
    def depth_Limited_Search(self):
        graph = Graph()
        funcUtils = utils()
        funcUtils.read_file_first_space('Cidades_grafo.txt',graph)
        funcUtils.read_file_and_connect('Cidades_grafo.txt',graph)
        funcUtils.depth_Limited_Search_util(graph,'Lisboa','Viseu',10)

    def A_Star_Search(self):
        graph = Graph()
        funcUtils = utils()
        funcUtils.read_file_first_space('Cidades_grafo.txt',graph)
        funcUtils.read_file_and_connect('Cidades_grafo.txt',graph)
        heuristics = {}
        funcUtils.create_heuristics('Cidades_Faro.txt',heuristics)
        funcUtils.A_Star_Search_util(graph,heuristics,'Viseu','Faro')
    
    def Greedy_Search(self):
        graph = Graph()
        funcUtils = utils()
        funcUtils.read_file_first_space('Cidades_grafo.txt',graph)
        funcUtils.read_file_and_connect('Cidades_grafo.txt',graph)
        heuristics = {}
        funcUtils.create_heuristics('Cidades_Faro.txt',heuristics)
        funcUtils.Greedy_Search_util(graph,heuristics,'Viseu','Faro')
        
        
mainprogram = main()
mainprogram.menu()

