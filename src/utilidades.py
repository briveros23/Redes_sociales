import networkx as nx



def tallo_y_hoja(G):
    '''funcion para simular salida igraph'''
    for node in G.nodes():
        vecinos = list(G.neighbors(node))
        print(f'{node} -- {vecinos}')  