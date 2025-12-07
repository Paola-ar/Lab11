import networkx as nx
from database.dao import DAO


class Model:
    def __init__(self):
        self.G = nx.Graph()

        self.id_map = {} # id rifugio
        self.rifugi = [] # lista completa rifugi
        self.connessioni = [] # connessioni filtrate per anno

        self.load_rifugi()

    def build_graph(self, year: int):
        """
        Costruisce il grafo (self.G) dei rifugi considerando solo le connessioni
        con campo `anno` <= year passato come argomento.
        Quindi il grafo avrà solo i nodi che appartengono almeno ad una connessione, non tutti quelli disponibili.
        :param year: anno limite fino al quale selezionare le connessioni da includere.
        """
        # TODO
        self.connessioni = DAO.readAllConnessione(year)
        edges = []
        for c in self.connessioni:
            if c.id_rifugio1 in self.id_map and c.id_rifugio2 in self.id_map:
                r1 = self.id_map[c.id_rifugio1]
                r2 = self.id_map[c.id_rifugio2]
                edges.append((r1,r2))
        self.G.add_edges_from(edges)

    def load_rifugi(self):
        """ Carica tutti i rifugi da databse e crea la mappa id:Rifugio"""
        self.rifugi = DAO.readAllRifugi()
        self.id_map = {r.id: r for r in self.rifugi}


    def get_nodes(self):
        """
        Restituisce la lista dei rifugi presenti nel grafo.
        :return: lista dei rifugi presenti nel grafo.
        """
        # TODO
        return list(self.G.nodes()) # lista degli id dei rifugi nel grafo


    def get_num_neighbors(self, node):
        """
        Restituisce il grado (numero di vicini diretti) del nodo rifugio.
        :param node: un rifugio (cioè un nodo del grafo)
        :return: numero di vicini diretti del nodo indicato
        """
        # TODO
        return len(list(self.G.neighbors(node)))


    def get_num_connected_components(self):
        """
        Restituisce il numero di componenti connesse del grafo.
        :return: numero di componenti connesse
        """
        # TODO
        return nx.number_connected_components(self.G)


    def get_reachable(self, start):
        """
        Deve eseguire almeno 2 delle 3 tecniche indicate nella traccia:
        * Metodi NetworkX: `dfs_tree()`, `bfs_tree()`
        * Algoritmo ricorsivo DFS
        * Algoritmo iterativo
        per ottenere l'elenco di rifugi raggiungibili da `start` e deve restituire uno degli elenchi calcolati.
        :param start: nodo di partenza, da non considerare nell'elenco da restituire.

        ESEMPIO
        a = self.get_reachable_bfs_tree(start)
        b = self.get_reachable_iterative(start)
        b = self.get_reachable_recursive(start)

        return a
        """

        # TODO
        # dfs_tree
        tree = nx.dfs_tree(self.G, start)
        reachable_dfs = list(tree.nodes)
        if start in reachable_dfs:
            reachable_dfs.remove(start)

        # DFS ricorsivo
        visitati = set()

        def dfs_ricorsivo(node):
            visitati.add(node)
            for neighbor in self.G.neighbors(node):
                if neighbor not in visitati:
                    dfs_ricorsivo(neighbor)

        dfs_ricorsivo(start)
        visitati.remove(start)
        return list(visitati)
