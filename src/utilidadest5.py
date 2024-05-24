import igraph as ig


# funcion para crear grafos bipartitos

def grafo_biparito_t5(nodos, aristas, dato_a_evitar):
    G = ig.Graph()
    for nodo in nodos:
        if nodo['id'] != dato_a_evitar:    
            G.add_vertex(name=str(nodo['id']), label=str(nodo['label']), tipo=str(nodo['type']))
    aristas = [ elem for elem in aristas if elem['source'] != dato_a_evitar]
    for arista in aristas:
        G.add_edge(str(arista['source']), str(arista['target']), weight=arista['value'])
    
    G.vs['type'] = [False if tipo == 'author' else True for tipo in G.vs['tipo']]
    return G

# generacion de grafos a partir de matriz de adyacencia

def grafo_matriz_adyacencia_t5(matriz_adyacencia, nombres_nodos):
    G = ig.Graph.Adjacency((matriz_adyacencia > 0).tolist(), mode = "undirected")
    G.es['weight'] = matriz_adyacencia[matriz_adyacencia.nonzero()]
    G.vs['label'] = nombres_nodos
    return G
