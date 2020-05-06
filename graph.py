
class Node:

    def __init__(self,key):
        self.key,self.successors,self.weight_successors = key,[],{}
        #for heuristic search purpose only (A*)
        self.g,self.h,self.f=0,0,0
    
    #return the key of a node
    def getKey(self):
        return self.key
    
    def getF(self):
        return self.f
    
    #return the successors of a node
    def getSuccessors(self):
        return self.successors
    
    #add a node successor
    def addSuccessor(self,node,weight):
        #only add if successor node not exists
        if node.getKey() not in self.weight_successors:
            self.successors.append(node)
            self.weight_successors[node.getKey()] = weight
    
    #return the weight of successors
    def getWeightSucessors(self):
        return self.weight_successors
    



class Graph:

    def __init__(self):
        self.nodes = {}
    
    def addNode(self,key_node):
        if key_node in self.nodes:
            #print('Error: key %s already exists!!' % key_node)
            return
        else:
                node = Node(key_node) #create a node
                self.nodes[key_node] = node

    #connect nodes
    def connectNodes(self,key_source,key_destination,weight):
        if key_source in self.nodes and key_destination in self.nodes:
            if key_source != key_destination: #check if the destination it's different of source 
                if weight > 0:                #cuz this graph not supports multiple edges with the same extremes
                    #connect nodes
                    self.nodes[key_source].addSuccessor(self.nodes[key_destination],weight)
                else:
                    print('Error: weight must be positive!!')
            else:
                print('Error: Same source and destination')
        else:
            print('Error: Key not exists!!')

    def getWeightEdge(self,key_source,key_successor):
        if key_source in self.nodes and key_successor in self.nodes: #check if the keys exists
            if key_source != key_successor:
                weight_successors = self.nodes[key_source].getWeightSucessors()
                if key_successor in weight_successors:
                    return weight_successors[key_successor]
                else:
                    print('Erros: Sucessor not exists!!')
            else:
                print('Erros: Same keys!!')
        else:
            print('Error: Key not exists!!')

    def getSuccessors(self,key_node):
        if key_node in self.nodes:
            nodes = self.nodes[key_node].getSuccessors()
            keys_sucessors = [node.getKey() for node in nodes]
            return keys_sucessors
        else:
            print('Error: Key not exists!!')
    
    def getNodes(self):
        return self.nodes