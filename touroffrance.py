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
            mystring = line
            myString = re.sub(r"[\n\t\s]*", "", mystring)
            roadsList.append(myString.strip().split(','))
            
    return roadsList


def create_tree(node_list):
    
    df = pd.DataFrame(node_list, columns=['City1', 'City2', 'KM'])
    G = nx.from_pandas_edgelist(df, 'City1', 'City2')
    G = nx.from_pandas_edgelist(df, 'City1', 'City2', edge_attr='KM')
    
    return G



def get_children(G, the_node):
    children = nx.descendants(G, the_node)
    print(children)

    print(G[the_node])



if __name__ == "__main__":
    
    in_file = "./uscities.txt"

    StartCity = "Nantes"
    
    road_list = open_file(in_file)
    print(road_list)

    G = create_tree(road_list)
    
    pos = nx.spring_layout(G, seed=2)
    nx.draw(G, with_labels=True, pos=pos)
    plt.show()
    
    get_children(G, StartCity)
   