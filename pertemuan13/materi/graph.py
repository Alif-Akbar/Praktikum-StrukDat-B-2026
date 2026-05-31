'''
Graph adalah struktur data yang terdiri dari simpul (nodes) dan sisi (edges)
yang menghubungkan simpul-simpul tersebut. Graph dapat digunakan untuk merepresentasikan
berbagai jenis hubungan, seperti jaringan sosial, peta jalan, atau hubungan antar objek.

Graph dapat dibagi menjadi dua jenis utama: graph berarah (directed graph) dan
graph tidak berarah (undirected graph).
'''

class graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def display(self):
        for node in self.graph:
            print(f"Node {node}: {self.graph[node]}")

# Contoh penggunaan
g = graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.display()
