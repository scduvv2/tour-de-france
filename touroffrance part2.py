"""
@author: TMartin
"""

import pandas as pd
import re
import networkx as nx
import matplotlib.pyplot as plt


def open_file(in_file):
    roadsList = []

    with open(in_file, 'r') as words:
        for line in words:
            if line.startswith('%'):
                continue
            
            mystring = line
            myString = re.sub(r"[\n\t\s]*", "", mystring)
            roadsList.append(myString.strip().split(','))
            
    return roadsList


def create_tree(node_list):
    
    df = pd.DataFrame(node_list, columns=['City1', 'City2', 'KM'])
    G = nx.from_pandas_edgelist(df, 'City1', 'City2')
    G = nx.from_pandas_edgelist(df, 'City1', 'City2', edge_attr='KM')
    
    return G


class Node(object):
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name


# write the thigns sto have dfs and bfs
class Search(Node):
    def __init__(self):
        self.visited = []
        self.queue = []
        self.weightedQueue = {} # may be needed for A*
        self.newNodes = []
        self.neighborL = []
        self.return_path = []
    def dfs(self, node, goalCity, G):
            self.visited.append(node)
            self.queue.append(node)
            self.node = str(node)
            self.neighborList = (G.adj[node])
            while self.queue:
                s = self.queue.pop(-1)
                nList = self.getNeighbor(s)
                if (s == goalCity):
                            print("These are visited nodes\n >>>", self.visited, "\n")
                            
                            print("Found:", goalCity,"")
                            self.return_path.append(goalCity)
                            self.find_path(goalCity)
                            break
                else:
                    for neighbor in nList:
                        if neighbor not in self.visited:
                            self.visited.append(neighbor)
                            self.queue.append(neighbor)
    def bfs(self, node, goalCity, G):
        self.visited.append(node)
        self.queue.append(node)
        self.node = str(node)
        self.neighborList = (G.adj[node])
        while self.queue:
            s = self.queue.pop(0)
            nList = self.getNeighbor(s)
            if (s == goalCity):
                        print("These are visited nodes\n >>>", self.visited, "\n")
                        
                        print("Found:", goalCity,"")
                        self.return_path.append(goalCity)
                        self.find_path(goalCity)
                        break
            else:
                for neighbor in nList:
                    if neighbor not in self.visited:
                        self.visited.append(neighbor)
                        self.queue.append(neighbor)
     
                        
    def getNeighbor(self, CurrNode):
        new_nodes = []
        inpt = str(CurrNode)
        neighbor = list(G.adj[inpt])
        for n in neighbor:
            if n not in self.queue:
                if n not in self.visited:
                    new_nodes.append(n)
                    
        newNeighbor = new_nodes
        self.neighborL.append(new_nodes)
        return newNeighbor    


    def find_path(self, goalCity):
        currNode = goalCity
        neighbor = list(G.adj[currNode])
        
        for n in neighbor:
            if n == self.visited[0]:
                self.return_path.insert(0, n)
                print("Here is the path to the goal")
                print(self.return_path)
                break
         
            if n in self.visited and n not in self.return_path:
                self.return_path.insert(0, n)
                self.find_path(n)
                if self.return_path[0] == self.visited[0]:
                    break
            



def callingSearch(startCity, goalCity, typeOfSearch, G):
    g = Search()
    if typeOfSearch == "bfs":
        g.bfs(startCity, goalCity, G)   
    elif typeOfSearch=='dfs':
        g.dfs(startCity, goalCity, G)    
        
## else if type of search = dfs 

if __name__ == "__main__":
    
    in_file = "./frenchcities.txt"

    StartCity = "Nantes"
    GoalCity = "Toulouse"
    type_of_search = "dfs"

    road_list = open_file(in_file)
    G = create_tree(road_list)
   
    print("Starting Node: " + StartCity)
    callingSearch(StartCity, GoalCity, type_of_search, G)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    