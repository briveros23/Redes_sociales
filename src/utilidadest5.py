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

# funcion para obtener estadisticas descriptivas de un grafo

def estadisticas_descriptivas_t5(G):
    return {
        # caratizar vertices del grafo
        # diametro del grafo
        'diametro': G.diameter(),
        # nodo de mayor grado
        'nodo_mayor_grado': G.vs.select(_degree = G.maxdegree())['label'],
        # nodo con mayo centralidad closeness
        'nodo_centralidad_closeness': G.vs.select(closeness = G.closeness())[0]['label'],
        # nodo con mayor centralidad betweenness
        'nodo_centralidad_betweenness': G.vs.select(betweenness = G.betweenness())[0]['label'],
        # nodo con mayor centralidad propia
        'nodo_centralidad_eigen': G.vs.select(_eigen = G.eigenvector_centrality())[0]['label'],
        #caracterizar conectividad del grafo
        # grado promedio
        'grado_promedio': sum(G.degree())/len(G.degree()),
        # clan mas grande
        'clan_mas_grande': G.clusters().giant().vcount(),
        # densidad de la red
        'densidad_red': G.density(),
        # transitividad global de la red 
        'transitividad_global': G.transitivity_undirected(),
    }