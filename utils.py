from graph  import *
from priority_queue import *
import time

class utils:
    
    def read_file_first_space(self,filename,graph):
        ficheiro = open(filename,'r')

        for linha in ficheiro:
            conteudo = linha.split(";",2)
            graph.addNode(conteudo[0])
            graph.addNode(conteudo[1])
        ficheiro.close()


    def read_file_and_connect(self,filename,graph):
        ficheiro = open(filename,'r')

        for linha in ficheiro:
            conteudo = linha.split(";")
            graph.connectNodes(conteudo[0],conteudo[1],int(conteudo[2]))
            graph.connectNodes(conteudo[1],conteudo[0],int(conteudo[2]))
        ficheiro.close()
    
    def create_heuristics(self,filename,heuristics):
        ficheiro = open(filename,'r')

        for linha in ficheiro:
            conteudo = linha.split(";")
            heuristics[conteudo[0]]= int(conteudo[2])
        ficheiro.close()
    
    # Check if a neighbor should be added to open list
    def add_to_open(self,open_list, neighbor):
        for node in open_list:
            if (neighbor == node and neighbor.f > node.f):
                return False
        return True
    
    def printList(self,open_list):
        i = len(open_list)-1
        for node in open_list:
            if i > 0:
                print(node.key,end =" -> ")
                i-=1
            else:
                print(node.key)




    def uniform_cost_search_util(self,graph,nodeStart,nodeGoal,verbose=False):
        #Check if both nodes exists
        if nodeStart not in graph.getNodes() or nodeGoal not in graph.getNodes():
            print('Error: Keys not exists!!')
            
        else:
            queue = PriorityQueue()

            keys_successors = graph.getSuccessors(nodeStart)

            for key_successor in keys_successors:
                weight = graph.getWeightEdge(nodeStart,key_successor)
                queue.insert((key_successor,weight),weight)
            
            goal , cost_goal = False,-1
            while not queue.is_empty():
                key_current_node, cost_node = queue.remove()
                if(key_current_node == nodeGoal):
                    goal,cost_goal=True,cost_node
                    break
                if verbose:
                    print('\nExpanding node \'%s\' with cost %s ...' % (key_current_node,cost_node))
                
                keys_successors = graph.getSuccessors(key_current_node)

                if keys_successors:
                    for key_successor in keys_successors:
                        cost_goal1 = graph.getWeightEdge(key_current_node,key_successor) + cost_node
                        queue.insert((key_successor,cost_goal1),cost_goal1)
            
            if(goal):
                print('\nGoal reached! Cost: %s' %cost_goal)
                print('Source: %s' %nodeStart)
                print('Goal: %s' %nodeGoal)
                #print(queue._queue)
                
            
            else:
                print('\n Unfulfilled goal.\n')
        

    def depth_Limited_Search_util(self,graph,nodeStart,nodeGoal,limit):
        #Check if both nodes exists
        if nodeStart not in graph.getNodes() or nodeGoal not in graph.getNodes():
            print('Error: Keys not exists!!')
        else:
            
            # Initialize mystack,visited and aux list
            myStack = []
            visitedList = []
            aux = []
            
            # Add the start node and initialize depth
            myStack.append(nodeStart)
            depth = 0

            # Loop until you find the end
            while len(myStack) > 0:

                #if depth <= limit requested by user
                if(depth <= int(limit)):

                    # Get the current node
                    current = myStack.pop()

                    #Check if node isn't in visitedList
                    if current not in visitedList:

                        #Found the goal
                        if current.__eq__(nodeGoal):
                            print("Goal Node found!!")
                            print("================== Visited List ================")
                            print(visitedList)
                            return

                        else:
                            #Add the current node
                            print("Depth = %s in limit of %s" %(depth,limit))
                            visitedList.append(current)
                            aux = graph.getSuccessors(current)
                            i = len(aux)-1
                        
                        while i > 0:
                            #Add the Successors of the current node
                            myStack.append(aux[i])
                            i-=1
                        depth +=1

                    else:
                        #If current already in the visitedList Jump for another node
                        #If this line is ignored it will make a infinite loop
                        print("Depth = %s in limit of %s" %(depth,limit))
                        myStack.pop()
                else:
                    #Goal node not found
                    print("Goal Node not found within depth limit")
                    return


    def A_Star_Search_util(self,graph,heuristics,nodeStart,nodeGoal):
        #Returns a list of tuples as a path from the given start to the given end in the given maze
        if nodeStart not in graph.getNodes() or nodeGoal not in graph.getNodes():
            print('Error: Keys not exists!!')
        
        else:

            # Initialize both open and closed list
            i=1
            open_list = []
            closed_list = []

            # Create a start and goal node
            start_node = Node(nodeStart)
            goal_node = Node(nodeGoal)

            # Add the start node
            open_list.append(start_node)
            

            # Loop until you find the end
            while len(open_list) > 0:

                
                # Get the current node
                open_list.sort(key=lambda Node: Node.f)
                current_node = open_list.pop(0)
                closed_list.append(current_node)

                if i > 1:
                    print('\nI will choose %s because has the lowest cost f= %s\n' % (current_node.key,current_node.f))
                
                # Found the goal
                if current_node.key.__eq__(goal_node.key):
                    print("Goal Node found!!")
                    print("================== Path List ================")
                    self.printList(closed_list)
                    return
            
                # Get neighbours
                neighbors = graph.getSuccessors(current_node.key)
                print ("============== Iteration nº %s ===============" %i)
                # Loop neighbors
                for key in neighbors:

                  
                    # Create a neighbor node
                    neighbor= Node(key)

                    # Check if the neighbor is in the closed list
                    if(neighbor in closed_list):
                        continue
                    
               
                    # Calculate full path cost
                    neighbor.g = graph.getWeightEdge(current_node.key,neighbor.key)
                    neighbor.h = heuristics.get(neighbor.key)
                    neighbor.f = neighbor.g + neighbor.h
                    print('\nNode:\'%s\' with g= %s  h= %s f= %s ' % (neighbor.key,neighbor.g,neighbor.h,neighbor.f))


                    # Check if neighbor is in open list and if it has a lower f value
                    if(self.add_to_open(open_list, neighbor) == True):
                        # Everything is green, add neighbor to open list
                        open_list.append(neighbor)
                i+=1
        
            print("No path Found")
    
    def Greedy_Search_util(self,graph,heuristics,nodeStart,nodeGoal):
         #Returns a list of tuples as a path from the given start to the given end in the given maze
        if nodeStart not in graph.getNodes() or nodeGoal not in graph.getNodes():
            print('Error: Keys not exists!!')
        
        else:

            # Initialize both open and closed list
            i=1
            open_list = []
            closed_list = []

            # Create a start and goal node
            start_node = Node(nodeStart)
            goal_node = Node(nodeGoal)

            # Add the start node
            open_list.append(start_node)
            

            # Loop until you find the end
            while len(open_list) > 0:


                # Get the current node
                open_list.sort(key=lambda Node: Node.f)
                current_node = open_list.pop(0)
                closed_list.append(current_node)
                if i > 1:
                    print('\nI will choose %s because has the lowest cost f= %s\n' % (current_node.key,current_node.f))
                
                # Found the goal
                if current_node.key.__eq__(goal_node.key):
                    print("Goal Node found!!")
                    print("================== Path List ================")
                    self.printList(closed_list)
                    return

            
                # Get neighbours
                neighbors = graph.getSuccessors(current_node.key)
                print ("============== Iteration nº %s ===============" %i)
                # Loop neighbors
                for key in neighbors:

                  
                    # Create a neighbor node
                    neighbor= Node(key)

                    # Check if the neighbor is in the closed list
                    if(neighbor in closed_list):
                        continue
                    
               
                    # Calculate full path cost
                    neighbor.h = heuristics.get(neighbor.key)
                    neighbor.f = neighbor.h
                    print('\nNode:\'%s\' with  h= %s f= %s ' % (neighbor.key,neighbor.h,neighbor.f))

                    # Check if neighbor is in open list and if it has a lower f value
                    if(self.add_to_open(open_list, neighbor) == True):
                        # Everything is green, add neighbor to open list
                        open_list.append(neighbor)
                i+=1
        
            print("No path Found")
   