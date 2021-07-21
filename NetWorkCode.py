
# ==============================================
# Basic import of the networkx library.
import networkx
import matplotlib.pyplot as plt


# Static Directed Graph
# ==============================================
# Generate a simple fixed undirected graph.
# In this case we are adding in the nodes and
# edges to the graph manually to make a tree.
items = ['guda','champange', 'pino noir', 'merlot', 'mozzerrela', 'cheeze wiz', 'beer', 'cheddar',
         'chardnay', 'resling', 'pino', 'pepperjack', 'bre', 'cabenet']
NewGraph = networkx.Graph()
NewGraph.add_nodes_from(items)
NewGraph.add_edges_from([('guda', 'cabenet'), ('guda', 'mozzerrela'), ('champange', 'beer'), ('champange', 'cheeze wiz'), ('pino noir', 'mozzerrela'), ('merlot', 'mozzerrela'),
     ('cheeze wiz', 'beer'), ('beer', 'cheddar'), ('cheddar', 'chardnay'), ('cheddar',
                                                                            'pepperjack'), ('chardnay', 'resling'), ('resling', 'pino'),
     ('pino', 'pepperjack'), ('pino', 'bre'), ('pepperjack', 'bre'), ('bre', 'cabenet')])
# This code generates a basic plot for the graph and then
# shows the resulting graph value.
networkx.draw(NewGraph,
              with_labels=True,
              arrows=True)
plt.show()
