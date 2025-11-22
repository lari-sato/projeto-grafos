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
        for v in range(self.n):
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


    # Algoritmo de coloração sequencial
    def coloracao_seq(self, ordem_vertices):
        n = self.n
        classes = []
        cor = [0]*n
        viz = [set(self.listaAdj[i]) for i in range(n)]

        for vi in ordem_vertices:
            k = 1
            while True:
                if k > len(classes):
                    classes.append(set())
                ok = True
                for u in classes[k-1]:
                    if (u in viz[vi]) or (vi in viz[u]): 
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
            return list(range(self.n)), False

        graus = [(self.grau(i), str(labels[i])) for i in range(self.n)]
        ordem = sorted(range(self.n), key=lambda i: (-graus[i][0], graus[i][1]))

        print("\n=======================================================")
        print("Rerrotulação por grau (número de vizinhos):")
        for rank, idx in enumerate(ordem, start=1):
            print(f"{labels[idx]}: {rank}")
        return ordem, True


    # Pipeline completo de coloração
    def colorir(self, labels):
        # 1) Chama re-rotulação se necessário
        ordem, houve_letras = self.reRotulacao(labels)
        if not houve_letras:
            ordem = list(range(self.n))  # mantém ordem natural

        # 2) Coloração sequencial
        cores, classes = self.coloracao_seq(ordem)
        resultado = {str(labels[i]): cores[i] for i in range(self.n)}
        rank_of_idx = {idx: rank for rank, idx in enumerate(ordem, start=1)}

        # 3) Impressão de resultados
        print("\n=======================================================")
        print("Coloração (rótulos originais -> classe de cor):")
        for lab in sorted(resultado.keys()):
            print(f"{lab}: {resultado[lab]}")
        print(f"\nNúmero de cores: {max(cores) if cores else 0}")

        # Sempre imprime classes com números, independente de letras ou não
        print("\nClasses finais:")
        for k, Ck in enumerate(classes, start=1):
            nums = sorted(rank_of_idx[i] for i in Ck)
            print(f"C{k} = {{{', '.join(map(str, nums))}}}")

        # Imprime classes com LETRAS, somente se o grafo tiver letras
        if houve_letras:
            print("\nClasses com as letras originais:")
            for k, Ck in enumerate(classes, start=1):
                lets = sorted(labels[i] for i in Ck)
                print(f"C{k} = {{{', '.join(lets)}}}")

        print("=======================================================\n")
        return resultado
    
    

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
