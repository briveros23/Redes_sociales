import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def tallo_y_hoja(G):
    '''funcion para simular salida igraph'''
    for node in G.nodes():
        vecinos = list(G.neighbors(node))
        print(f'{node} -- {vecinos}')  

def grafico_ponderado(G,n=5, with_labels=True, node_color='skyblue', node_size=500, edge_color='black', linewidths=1, font_size=12,label=None):
    '''funcion para graficar las aristas del grafo con pesos'''
    # obtener pesos
    weights = [data['weight'] for _, _, data in G.edges(data=True)]
    # escalar pesos
    max_weight = max(weights)
    scaled_weights = [w / max_weight * n for w in weights]
    # Dibujar el grafo con el grosor de las aristas dependiendo del peso
    pos = nx.spring_layout(G)  # posición de los nodos
    nx.draw(G, pos, with_labels=with_labels, node_color=node_color, node_size=node_size, width=scaled_weights, edge_color=edge_color, linewidths=linewidths, font_size=font_size)
    plt.title(label)
    plt.show()

def definir_grafo_aleatorio(n_nodos,p):
    '''funcion para definir un grafo aleatorio con n_nodos y probabilidad p de que exista una arista entre dos nodos'''
    vertices = list(range(n_nodos))
    matriz_aristas = [(i,j) for i in range(n_nodos) for j in range(i+1,n_nodos) if np.random.rand() < p]
    G = nx.Graph()
    G.add_nodes_from(vertices)
    G.add_edges_from(matriz_aristas)
    return G

def reconstruir_matriz_adyacencia(matriz_aristas,vertices):
    '''funcion para reconstruir la matriz de adyacencia a partir de la matriz de aristas'''
    # definimos una matriz de adyacencia vacia 
    matriz_adyacencia = np.zeros((len(vertices),len(vertices)))
    indice_vertice = {vertice:indice for indice,vertice in enumerate(vertices)}

    # recuperamos la matriz
    for arista in matriz_aristas:
        i=indice_vertice[arista[0]]
        j=indice_vertice[arista[1]]
        matriz_adyacencia[i,j] = 1
        matriz_adyacencia[j,i] = 1
    
    # retornamos la matriz
    return matriz_adyacencia

def reconstruir_matriz_aristas_nodos(matriz_adyacencia):
    '''funcion para reconstruir la matriz de aristas a partir de la matriz de adyacencia'''
    # recuperamos los vertices 
    vertices = list(range(matriz_adyacencia.shape[0]))
    # definimos una matriz de aristas
    matriz_aristas = [(i,j) for i in range(matriz_adyacencia.shape[0]) for j in range(i+1,matriz_adyacencia.shape[0]) if matriz_adyacencia[i,j] == 1]
    # retornamos la matriz
    return matriz_aristas, vertices

