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

# 21/11/2025: Larissa: adição de funções para coloração de vértices, calcular
# graus dos vértices e verificar se o grafo é Euleriano

# 22/11/2025: Larissa: arrumado erros nas funções não compatíveis com dicionário

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
        self.n = 0  # Número de vértices


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
        self.n += 1
        print("\nVértice adicionado.")


    def addAresta(self, aresta):
        origem_existe = aresta.origem.nome in self.vertices
        destino_existe = aresta.destino.nome in self.vertices
        if not origem_existe or not destino_existe:
            msg = "\nErro: "
            if not origem_existe and not destino_existe:
                msg += f"vértices '{aresta.origem.nome}' e '{aresta.destino.nome}' não existem no grafo."
            elif not origem_existe:
                msg += f"vértice de origem '{aresta.origem.nome}' não existe no grafo."
            else:
                msg += f"vértice de destino '{aresta.destino.nome}' não existe no grafo."
            print(msg)
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
        # Remove o vértice do grafo (lista de adjacência e dicionário de vértices)
        del self.listaAdj[rotulo]
        del self.vertices[rotulo]
        self.n -= 1   # atualizar contador de vértices
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
    
    
    def listarHospitais(self, modo):
        hospitais = [v for v in self.vertices.values() if isinstance(v, Hospital)]
        lista = []
        for hosp in hospitais:
            tempos = [
                aresta.tempo
                for aresta in hosp.arestas
                if isinstance(aresta, Est_Hosp) and aresta.modo.lower() == modo.lower()
            ]
            if tempos:
                menor = min(tempos)
                lista.append((hosp.nome, menor))
            else:
                lista.append((hosp.nome, float('inf')))
        lista.sort(key=lambda x: x[1])
        print(f"\nHospitais ordenados pelo menor tempo ({modo}):")
        for nome, t in lista:
            if t < float('inf'):
                print(f"{nome}: {t} min")
            else:
                print(f"{nome}: não possui aresta do tipo '{modo}'")


    def modos(self):
        modos = set()
        for v in self.vertices.values():
            for aresta in v.arestas:
                if isinstance(aresta, Est_Hosp):
                    modos.add(aresta.modo.lower())
        return sorted(modos)

    
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
                visitados.append(atual)
                for vizinho in self.listaAdj[atual]:
                    if vizinho not in visitados:
                        pilha.append(vizinho)
    
        if len(visitados) == len(self.listaAdj):
            return True
        else:
            return False
        
    
    # -- GRAU DE VÉRTICES ---
    def degreeND(self, v):
        grau = len(self.listaAdj[v])           # Conta vizinhos de v
        if v in self.listaAdj[v]:              # Caso especial: laço em v
            grau += 1                          # Laço conta como 2
        return grau
    
    
    # Verifica se o grafo é Euleriano
    def euleriano(self):
        soma = 0
        impares = 0
        for v in self.listaAdj.keys():
            grau = self.degreeND(v)
            if self.degreeND(v) % 2 != 0:
                if impares > 2:
                    return False
                impares += 1
            soma += grau
        if impares % 2 != 0 or (soma != self.m * 2):
            return False
        return True
    
    
    # --- COLORAÇÃO DE VÉRTICES ---

    # Verificação de rótulos numéricos 
    @staticmethod
    def ehNumerico(x):
        if isinstance(x, int): return True
        if isinstance(x, str) and x.isdigit(): return True
        return False

    # Algoritmo de coloração sequencial (rótulos)
    def coloracao_seq(self, ordem_vertices):
        # ordem_vertices: lista de rótulos (strings) na ordem desejada
        classes = []
        cor = {}  # mapa rótulo -> cor
        # viz: mapa rótulo -> conjunto de vizinhos (rótulos)
        viz = {label: set(self.listaAdj[label]) for label in ordem_vertices}

        for vi in ordem_vertices:
            k = 1
            while True:
                if k > len(classes):
                    classes.append(set())
                ok = True
                for u in classes[k-1]:
                    if u in viz[vi] or vi in viz[u]:
                        ok = False
                        break
                if ok:
                    classes[k-1].add(vi)
                    cor[vi] = k
                    break
                k += 1
        return cor, classes

    # Rerrotulação (no caso de grafo com letras)
    def reRotulacao(self, labels):
        houve = any(not self.ehNumerico(x) for x in labels)
        if not houve:
            # retorna mesma lista de rótulos e sinaliza que não houve letras
            return labels[:], False

        # graus: (grau_do_rotulo, rótulo_str)
        graus = [(self.degreeND(labels[i]), str(labels[i])) for i in range(len(labels))]
        ordem_indices = sorted(range(len(labels)), key=lambda i: (-graus[i][0], graus[i][1]))
        ordem_labels = [labels[i] for i in ordem_indices]

        print("\n=======================================================")
        print("Rerrotulação por grau (número de vizinhos):")
        for rank, idx_label in enumerate(ordem_labels, start=1):
            print(f"{idx_label}: {rank}")
        return ordem_labels, True

    # Pipeline completo de coloração
    def colorir(self, labels):
        # 1) Chama re-rotulação se necessário
        ordem, houve_letras = self.reRotulacao(labels)
        if not houve_letras:
            ordem = labels[:]  # mantém ordem natural (rótulos)

        # 2) Coloração sequencial
        cores, classes = self.coloracao_seq(ordem)
        resultado = {str(label): cores.get(label, 0) for label in labels}
        rank_of_idx = {label: rank for rank, label in enumerate(ordem, start=1)}

        # 3) Impressão de resultados
        print("\n=======================================================")
        print("Coloração (rótulos originais -> classe de cor):")
        for lab in sorted(resultado.keys()):
            print(f"{lab}: {resultado[lab]}")
        print(f"\nNúmero de cores: {max(cores.values()) if cores else 0}")

        # Sempre imprime classes com números (usando ranks da ordem)
        print("\nClasses finais:")
        for k, Ck in enumerate(classes, start=1):
            nums = sorted(rank_of_idx[i] for i in Ck)
            print(f"C{k} = {{{', '.join(map(str, nums))}}}")

        # Imprime classes com LETRAS, somente se o grafo tiver letras
        if houve_letras:
            print("\nClasses com as letras originais:")
            for k, Ck in enumerate(classes, start=1):
                lets = sorted(Ck)
                print(f"C{k} = {{{', '.join(lets)}}}")

        print("=======================================================\n")
        return resultado



    def dijkstra(self, origem_nome, destino_nome):
        vertices = list(self.vertices.keys())
        n = len(vertices)
        # Cria mapeamento índice <-> nome
        nome_to_ind = {v: i for i, v in enumerate(vertices)}
        ind_to_nome = {i: v for i, v in enumerate(vertices)}
        dist = [float('inf')] * n
        pred = [None] * n
        visitado = [False] * n

        if origem_nome not in nome_to_ind or destino_nome not in nome_to_ind:
            return None, None

        origem = nome_to_ind[origem_nome]
        destino = nome_to_ind[destino_nome]
        dist[origem] = 0

        for _ in range(n):
            u = None
            melhor = float('inf')
            for v in range(n):
                if not visitado[v] and dist[v] < melhor:
                    melhor, u = dist[v], v
            if u is None:
                break
            visitado[u] = True
            for vizinho_nome in self.listaAdj[ind_to_nome[u]]:
                v = nome_to_ind[vizinho_nome]
                peso = None
                for aresta in self.vertices[ind_to_nome[u]].arestas:
                    outro = aresta.destino.nome if aresta.origem.nome == ind_to_nome[u] else aresta.origem.nome
                    if outro == vizinho_nome:
                        peso = aresta.tempo
                        break
                if peso is not None and peso >= 0:
                    if dist[u] + peso < dist[v]:
                        dist[v] = dist[u] + peso
                        pred[v] = u
        # Reconstruir caminho
        caminho = []
        v = destino
        if dist[destino] == float('inf'):
            return None, None
        while v is not None:
            caminho.append(ind_to_nome[v])
            v = pred[v]
        caminho.reverse()
        return caminho, dist[destino]

    
    

# --- LEITURA DE GRAFO A PARTIR DE ARQUIVO ---
def gArquivo(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        linhas = [l.strip() for l in f if l.strip()]

    tipo = int(linhas[0])  # Tipo do grafo
    n = int(linhas[1])     # Número de vértices

    grafo = TGrafo()
    rotulos = []

    for i in range(2, 2 + n):
        partes = linhas[i].split('"')
        nome = partes[1].strip()
        tipo_v = partes[3].strip().upper()
        atributo = partes[5].strip()
        grafo.addVert(nome, tipo_v, atributo)
        rotulos.append(nome)

    m = int(linhas[2 + n])  # Número de arestas

    for i in range(3 + n, 3 + n + m):
        partes = linhas[i].split('"')
        nome1 = partes[1].strip()
        nome2 = partes[3].strip()
        campos = linhas[i].split()
        # Se último campo é uma palavra (ex: CAMINHADA), use o penúltimo como peso
        if campos[-1].isalpha():
            peso = int(campos[-2])
            modo = campos[-1]
            v1 = grafo.vertices[nome1]
            v2 = grafo.vertices[nome2]
            aresta = Est_Hosp(v1, v2, peso, modo)
        else:
            # Caso padrão: estação-estação
            peso = int(campos[-1])
            v1 = grafo.vertices[nome1]
            v2 = grafo.vertices[nome2]
            if isinstance(v1, Estacao) and isinstance(v2, Estacao):
                aresta = Est_Est(v1, v2, peso)
            else:
                aresta = Aresta(v1, v2, peso)
        grafo.addAresta(aresta)
        
    return grafo