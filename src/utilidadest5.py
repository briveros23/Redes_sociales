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
    # diametro del grafo
    diametro = G.diameter()
    # nodo de mayor grado
    nodo_mayor_grado = G.vs.select(_degree = G.maxdegree())['label']
    mayor_grado = G.maxdegree()
    # nodo con mayor centralidad betweenness
    centralidad_intermediacion = G.betweenness()
    nodo_max_intermediacion = G.vs[centralidad_intermediacion.index(max(centralidad_intermediacion))]["label"]
    # nodo con mayor closeness
    centralidad_cercania = G.closeness()
    nodo_max_cercania = G.vs[centralidad_cercania.index(max(centralidad_cercania))]["label"]
    # nodo con mayor centralidad propia
    centralidad_eigen = G.eigenvector_centrality()
    nodo_max_eigen = G.vs[centralidad_eigen.index(max(centralidad_eigen))]["label"]
    # grado promedio
    grado_promedio = sum(G.degree())/len(G.degree())
    # clan mas grande
    clanes = G.largest_cliques()
    clan_mas_grande = max(clanes, key=len)
    clan_mas_grande = len(clan_mas_grande)
    # densidad de la red
    densidad_red = G.density()
    # transitividad global de la red
    transitividad_global = G.transitivity_undirected()
    return {"diametro": diametro, "nodo_mayor_grado": nodo_mayor_grado, "mayor_grado": mayor_grado, "nodo_max_intermediacion": nodo_max_intermediacion, "nodo_max_cercania": nodo_max_cercania, "nodo_max_eigen": nodo_max_eigen, "grado_promedio": grado_promedio, "clan_mas_grande": clan_mas_grande, "densidad_red": densidad_red, "transitividad_global": transitividad_global}