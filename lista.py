# Julia Santos Oliveira     RA: 10417672
# Larissa Yuri Sato         RA: 10418318

# O arquivo lista.py contém a implementação do grafo não direcionado rotulado
# utilizando dicionário de adjacência, além de funções para manipulação do grafo.


###################################################################################


# HISTÓRICO DE ALTERAÇÕES:

# 15/09/2025 - Larissa: modificação da classe TGrafo de grafo não
# direcionado para grafo não direcionado rotulado e mudando lista de adjacência
# para dicionário para facilitar a manipulação dos rótulos.

# 25/09/2025: Julia: atualização do código para incluir atributos
# linhas de metrô e especialidades nos vértices 

# 26/09/2025 - Larissa: adição de classes de vértice e arestas e modificação
# das funções de TGrafo para adaptar a essas classes

# 27/09/2025: Larissa: mudança das funções do grafo para
# diferenciar tipos de vértice e arestas


###################################################################################


class Vertice:
    def __init__(self, nome):
        self.nome = nome
        self.arestas = []


class Estacao(Vertice):
    def __init__(self, nome, linhas):
        super().__init__(nome)
        self.linhas = linhas


class Hospital(Vertice):
    def __init__(self, nome, especialidades):
        super().__init__(nome)
        self.especialidades = especialidades


class Aresta:
    def __init__(self, origem, destino, tempo):
        self.origem = origem
        self.destino = destino
        self.tempo = tempo

class Est_Est(Aresta):
    def __init__(self, origem, destino, tempo):
        super().__init__(origem, destino, tempo)


class Est_Hosp(Aresta):
    def __init__(self, origem, destino, tempo, modo):
        super().__init__(origem, destino, tempo)
        self.modo = modo

class TGrafo:
    def __init__(self):
        self.vertices = {} # vertices
        self.listaAdj = {}  # {rotulo: [vizinhos]}
        self.m = 0  # Número de arestas

    def addVert(self, nome, tipo, atributo):
        if nome in self.vertices:
            print(f"\nErro: vértice '{nome}' já existe.")
            return
        if tipo == 'E':
            vertice = Estacao(nome, atributo)
        elif tipo == 'H':
            vertice = Hospital(nome, atributo)
        else:
            print("Tipo de vértice inválido. Use 'E' para Estação ou 'H' para Hospital.")
            return
        self.vertices[nome] = vertice
        self.listaAdj[nome] = []
        print("\nVértice adicionado.")

    def addAresta(self, aresta):
        if aresta.origem.nome not in self.vertices or aresta.destino.nome not in self.vertices:
            print(f"\nErro: vértice '{aresta.origem.nome}' ou '{aresta.destino.nome}' não existe no grafo.")
            return
        # Adiciona vizinhos
        self.listaAdj[aresta.origem.nome].append(aresta.destino.nome)
        self.listaAdj[aresta.destino.nome].append(aresta.origem.nome)
        # Adiciona a aresta à lista de arestas dos vértices
        self.vertices[aresta.origem.nome].arestas.append(aresta)
        self.vertices[aresta.destino.nome].arestas.append(aresta)
        self.m += 1
        print("\nAresta inserida.")

    def remVert(self, rotulo):
        if rotulo not in self.vertices:
            print(f"\nErro: vértice '{rotulo}' não existe no grafo.")
            return
        # Remove o vértice das listas de adjacência dos vizinhos
        for vizinho in list(self.listaAdj[rotulo]):
            self.listaAdj[vizinho].remove(rotulo)
            self.m -= 1
        # Remove o vértice do grafo
        del self.listaAdj[rotulo]
        print("\nVértice removido.")

    def remAresta(self, rotulo1, rotulo2):
        if rotulo1 not in self.vertices or rotulo2 not in self.vertices:
            print(f"\nErro: vértice '{rotulo1}' ou '{rotulo2}' não existe no grafo.")
            return
        if rotulo2 not in self.listaAdj[rotulo1]:
            print("\nAresta não encontrada. Tente novamente.")
        else:
            self.listaAdj[rotulo1].remove(rotulo2)
            self.listaAdj[rotulo2].remove(rotulo1)
            self.m -= 1
            print("\nAresta removida.")

    def mostrar(self):
        print(f"\n n: {len(self.listaAdj):2d} m: {self.m:2d}")
        for rotulo, vizinhos in self.listaAdj.items():
            vizinhos_str = []
            for vizinho in vizinhos:
                # Procurar a aresta correspondente
                peso = None
                for aresta in self.vertices[rotulo].arestas:
                    if (aresta.origem.nome == rotulo and aresta.destino.nome == vizinho) or (aresta.origem.nome == vizinho and aresta.destino.nome == rotulo):
                        peso = aresta.tempo
                        break
                if peso is not None:
                    vizinhos_str.append(f"({vizinho}, {peso})")
                else:
                    vizinhos_str.append(f"({vizinho}, ?)")
            print(f"{rotulo}: {' '.join(vizinhos_str)}")
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
    rotulos = []

    # Adiciona vértices com nome, tipo e atributo (sem índice)
    for i in range(2, 2 + n):
        partes = linhas[i].split('"')
        # partes: ['', nome, ' ', tipo, ' ', atributo, '']
        nome = partes[1].strip()
        tipo_v = partes[3].strip().upper()
        atributo = partes[5].strip()
        grafo.addVert(nome, tipo_v, atributo)
        rotulos.append(nome)

    m = int(linhas[2 + n])  # Número de arestas

    # Adiciona arestas usando nomes
    for i in range(3 + n, 3 + n + m):
        partes = linhas[i].split('"')
        # partes: ['', nome1, ' ', nome2, ' ', peso, '']
        nome1 = partes[1].strip()
        nome2 = partes[3].strip()
        peso = int(linhas[i].split()[-1])
        aresta = Aresta(grafo.vertices[nome1], grafo.vertices[nome2], peso)
        grafo.addAresta(aresta)

    return grafo
