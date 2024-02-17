import networkx as nx
import matplotlib.pyplot as plt


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