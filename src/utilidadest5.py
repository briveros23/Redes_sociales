import igraph as ig


# funcion para crear grafos bipartitos

def grafo_bipartito(primer_grupo, segundo_grupo, aristas):
    # nodos 
    nodos = primer_grupo + segundo_grupo
    # lista de True por ley
    primer_tipo = [True] * len(primer_grupo)
    # lista de false por partido politico 
    segundo_tipo = [False] * len(segundo_grupo)
    # sumamos ambas listas 
    tipo = primer_tipo + segundo_tipo  
    # creamos el grafo bipartito

    conexiones_indices = [(nodos.index(nodo1), nodos.index(nodo2)) for nodo1,nodo2  in aristas]
    
    g = ig.Graph.Bipartite(types=tipo, edges=conexiones_indices)
    g.vs['nombre'] = nodos

    return g