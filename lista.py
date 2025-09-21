# Julia Santos Oliveira     RA: 10417672
# Larissa Yuri Sato         RA: 10418318

# O arquivo lista.py contém a implementação do grafo não direcionado rotulado
# utilizando dicionário de adjacência, além de funções para manipulação do grafo.


###################################################################################


# HISTÓRICO DE ALTERAÇÕES:

# 15/09/2025 - Larissa: modificação da classe TGrafo de grafo não
# direcionado para grafo não direcionado rotulado e mudando lista de adjacência
# para dicionário para facilitar a manipulação dos rótulos.



###################################################################################



class TGrafo:
    def __init__(self):
        self.listaAdj = {}  # {rotulo: [vizinhos]}
        self.m = 0  # Número de arestas

    def addVert(self, rotulo):
        if rotulo in self.listaAdj:
            print(f"\nErro: vértice '{rotulo}' já existe.")
            return
        self.listaAdj[rotulo] = []
        print("\nVértice adicionado.")

    def addAresta(self, rotulo1, rotulo2):
        if rotulo1 not in self.listaAdj or rotulo2 not in self.listaAdj:
            print(f"\nErro: vértice '{rotulo1}' ou '{rotulo2}' não existe no grafo.")
            return
        if rotulo2 in self.listaAdj[rotulo1]:
            print("\nAresta já inserida. Tente novamente.")
        else:
            self.listaAdj[rotulo1].append(rotulo2)
            self.listaAdj[rotulo2].append(rotulo1)
            self.m += 1
            print("\nAresta inserida.")

    def remAresta(self, rotulo1, rotulo2):
        if rotulo1 not in self.listaAdj or rotulo2 not in self.listaAdj:
            print(f"\nErro: vértice '{rotulo1}' ou '{rotulo2}' não existe no grafo.")
            return
        if rotulo2 not in self.listaAdj[rotulo1]:
            print("\nAresta não encontrada. Tente novamente.")
        else:
            self.listaAdj[rotulo1].remove(rotulo2)
            self.listaAdj[rotulo2].remove(rotulo1)
            self.m -= 1
            print("\nAresta removida.")

    def remVert(self, rotulo):
        if rotulo not in self.listaAdj:
            print(f"\nErro: vértice '{rotulo}' não existe no grafo.")
            return
        # Remove o vértice das listas de adjacência dos vizinhos
        for vizinho in list(self.listaAdj[rotulo]):
            self.listaAdj[vizinho].remove(rotulo)
            self.m -= 1
        # Remove o vértice do grafo
        del self.listaAdj[rotulo]
        print("\nVértice removido.")

    def mostrar(self):
        print(f"\n n: {len(self.listaAdj):2d} m: {self.m:2d}")
        for rotulo, vizinhos in self.listaAdj.items():
            print(f"{rotulo}: {', '.join(str(v) for v in vizinhos)}")
        print("\nFim da impressão.")

    
    # Verifica se o grafo é conexo utilizando DFS
    def conexidade(self, rotuloInicio=None):
        if not self.listaAdj:
            print("Grafo vazio.")
            return False
        if rotuloInicio is None:
            rotuloInicio = next(iter(self.listaAdj))  # Pega qualquer vértice se não for passado
    
        visitados = []
        pilha = [rotuloInicio]
    
        while pilha:
            atual = pilha.pop()
            if atual not in visitados:
                print(f"Visitando: {atual}")
                visitados.append(atual)
                for vizinho in self.listaAdj[atual]:
                    if vizinho not in visitados:
                        pilha.append(vizinho)
    
        if len(visitados) == len(self.listaAdj):
            return True
        else:
            return False

# --- LEITURA DE GRAFO A PARTIR DE ARQUIVO ---
def gArquivo(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        linhas = [l.strip() for l in f if l.strip()]

    tipo = int(linhas[0])  # Tipo do grafo
    n = int(linhas[1])     # Número de vértices

    grafo = TGrafo()       # Inicializa grafo vazio

    # Adiciona vértices com rótulo
    for i in range(2, 2 + n):
        partes = linhas[i].split()
        rotulo = partes[1].strip('"')
        grafo.addVert(rotulo)

    m = int(linhas[2 + n])  # Número de arestas

    # Adiciona arestas
    for i in range(3 + n, 3 + n + m):
        partes = linhas[i].split()
        v1 = int(partes[0])
        v2 = int(partes[1])
        rotulos = list(grafo.listaAdj.keys())
        rotulo1 = rotulos[v1]
        rotulo2 = rotulos[v2]
        grafo.addAresta(rotulo1, rotulo2)

    return grafo