class Grafo:
    def __init__(self,qntd_vertices) -> None:
        self.vertices = {}
        self.qntd_vertices = qntd_vertices
        for i in range(qntd_vertices):
            self.vertices[i] = []

    def adicionar(self,v1,v2):
        if v1 != v2 and v1 not in self.vertices[v2]:
            self.vertices[v1].insert(0,v2)
            self.vertices[v2].insert(0,v1)

    def imprimir_listas(self):
        for vertice,lista in self.vertices.items():
            if len(lista) > 0:
                print(str(vertice)+":", *lista, "")
            else: print(str(vertice)+": Lista Vazia")

    def busca_profundidade(self):
        self.marcado = self.qntd_vertices*[False]
        self.visitados = []
        self.dfs(0)
        return self.visitados

    def dfs(self,v):
        self.marcado[v] = True
        self.visitados.append(v)
        for u in self.vertices[v]:
            if not self.marcado[u]:
                self.dfs(u)

def main():
    qntd_vertices_input = int(input())
    grafo = Grafo(qntd_vertices_input)

    entrada_str = str(input()).split()
    entrada_int = list(map(int,entrada_str))

    while entrada_int[2] != 0:
        grafo.adicionar(entrada_int[0],entrada_int[1])
        entrada_str = str(input()).split()
        entrada_int = list(map(int,entrada_str))
    else:
        grafo.adicionar(entrada_int[0],entrada_int[1])

    grafo.imprimir_listas()
    resultado = grafo.busca_profundidade()
    print()
    print(*resultado,end=' ')

if __name__=='__main__':
    main()