"""
@author: TMartin
"""

import pandas as pd
import re
import networkx as nx
import matplotlib.pyplot as plt
import sys
import math


def open_file(in_file):
    roadsList = []
    cityList = {}

    with open(in_file, 'r') as words:
        citiesStart=False
        roadsStart=False
        for line in words:
            if line.__eq__('%========================== Cities (name, latitude, longitude) ========================\n'):
                citiesStart=True
                continue
            if citiesStart and line != "\n":
                if line.__eq__("%====================================== Roads ========================================\n"):
                    citiesStart=False
                    roadsStart=True
                    continue  
                else:
                    mystring = line
                    myString = re.sub(r"[\n\t\s]*", "", mystring)
                    split = myString.strip().split(',')
                    cityList[split[0]] = [split[1],split[2]]
            if roadsStart==True and line != "\n":
                mystring = line
                myString = re.sub(r"[\n\t\s]*", "", mystring)
                roadsList.append(myString.strip().split(','))
                
           
            
    return roadsList,cityList


def create_tree(node_list,coordinate_list):
    
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
    
    def a_star(self, node, goalCity, G,cityList):
        self.visited.append(node)
        self.queue.append(node)
        self.node = str(node)
        self.neighborList = (G.adj[node])
        while self.queue:
            s = self.queue.pop(0)
            node_with_least_heuristic=''
            least_heuristic = -1
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
                        node_heuristic = self.calculate_heuristic(goalCity,neighbor,cityList)
                        if node_heuristic< least_heuristic or least_heuristic==-1:
                            least_heuristic=node_heuristic
                            node_with_least_heuristic = neighbor
                if node_with_least_heuristic not in self.visited:
                    self.visited.append(node_with_least_heuristic)            
                    self.queue.append(node_with_least_heuristic)
             
         
                        
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
                
    def calculate_heuristic(self,destination,node,cityList):
        lat2 =   float(cityList.get(destination)[0])
        long2 = float(cityList.get(destination)[1])
        lat1 = float(cityList.get(node)[0])
        long1 = float(cityList.get(node)[1])
        heuristic = math.sqrt((69.5 * (lat1 - lat2)) ** 2 + (69.5 * math.cos((lat1 + lat2)/360 * math.pi) * (long1 - long2)) ** 2)
        return heuristic
            



def callingSearch(startCity, goalCity, typeOfSearch, G,cityList):
    g = Search()
    if typeOfSearch == "bfs":
        g.bfs(startCity, goalCity, G)   
    elif typeOfSearch=='dfs':
        g.dfs(startCity, goalCity, G)    
    elif typeOfSearch=='A*':
        g.a_star(startCity, goalCity, G,cityList)        
        
## else if type of search = dfs 

if __name__ == "__main__":
    
    
    in_file = sys.argv[1]

    StartCity = sys.argv[2]
    GoalCity = sys.argv[3]
    type_of_search = "A*"

    road_list,city_list = open_file(in_file)
    G = create_tree(road_list,city_list)
    pos = nx.spring_layout(G, seed=2)
   # nx.draw(G,with_labels=True, pos=pos)
   # plt.show()
   
    print("Starting Node: " + StartCity)
    callingSearch(StartCity, GoalCity, type_of_search, G,city_list)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    