# Julia Santos Oliveira     RA: 10417672
# Larissa Yuri Sato         RA: 10418318

# O arquivo main.py inclui a função principal do programa,
# mostrando ao usuário o menu de opções para manipulação
# do grafo


###################################################################################


# HISTÓRICO DE ALTERAÇÕES:

# 24/09/2025: Julia: adição da função de leitura,
# impressão e gravar dados no arquivo

# 25/09/2025: Larissa: alteração das chamadas de função do
# grafo para incluir os argumentos

# 28/09:2025: Julia: alteração das chamadas de função do grafo
# para incluir os argumentos


###################################################################################

from lista import TGrafo, Vertice, Aresta, Estacao, Hospital, gArquivo

def ler_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Entrada inválida. Informe um número inteiro.")

def ler_str(msg):
    while True:
        try:
            return (input(msg))
        except ValueError:
            print("Entrada inválida. Informe sequência de caracteres (string).")

def menuD(g: TGrafo):
    MENU = """
==================== MENU DO "METRÔSAÚDE": BEM-VINDO(A)! =====================
1) Leitura de arquivo (grafo.txt).
2) Gravar dados no arquivo (grafo.txt).
3) Inserir vértice (Estação ou Hospital).
4) Inserir aresta.
5) Remover vértice.
6) Remover aresta.
7) Mostrar conteúdo do arquivo.
8) Mostrar grafo (Lista de Adjacência).
9) Apresentar conexidade do grafo.
0) Sair
==========================================================================
"""
    while True:
        print(MENU)
        op = input("Selecione uma opção: ").strip()

        if op == "1":
            arq = input("\nNome do arquivo (ex.: 'grafo.txt'): ").strip()
            grafo = gArquivo(arq)
            print("\nLista de Adjacência resultante:\n")
            grafo.mostrar()

        elif op == "2":
            tipo_grafo = 3
            n = ler_int("Insira o número de vértices: ")
            vertices = []
            for i in range(n):
                nome = ler_str(f"Nome do vértice {i+1}: ")
                tipo_v = ler_str(f"Tipo do vértice {i+1} (E para Estação, H para Hospital): ").strip().upper()
                if tipo_v == 'E':
                    atributo = ler_str(f"Cor/linha da estação {nome}: ")
                elif tipo_v == 'H':
                    atributo = ler_str(f"Especialidade do hospital {nome}: ")
                else:
                    atributo = ""
                vertices.append((nome, tipo_v, atributo))
            m = ler_int("Insira o número de arestas: ")
            arestas = []
            for i in range(m):
                nome1 = ler_str(f"Nome do vértice de origem da aresta {i+1}: ")
                nome2 = ler_str(f"Nome do vértice de destino da aresta {i+1}: ")
                peso = ler_int(f"Peso da aresta {i+1}: ")
                arestas.append((nome1, nome2, peso))
            nome_arquivo = ler_str("Nome do arquivo para salvar o grafo: ")
            try:
                with open(nome_arquivo, 'w', encoding='utf-8') as f:
                    f.write(f"{tipo_grafo}\n")
                    f.write(f"{n}\n")
                    for nome, tipo_v, atributo in vertices:
                        f.write(f'"{nome}" "{tipo_v}" "{atributo}"\n')
                    f.write(f"{m}\n")
                    for nome1, nome2, peso in arestas:
                        f.write(f'"{nome1}" "{nome2}" {peso}\n')
                print(f"Grafo salvo em '{nome_arquivo}'.")
            except Exception as e:
                print(f"Erro ao salvar o arquivo: {e}")

        elif op == "3":
            tipo = ler_str("O vértice é Estação (E) ou Hospital (H)? ").strip().upper()
            nome = ler_str("Nome do vértice: ")
            if tipo == "E":
                atributo = ler_str("Cor/linha da estação: ")
            elif tipo == "H":
                atributo = ler_str("Especialidade do hospital: ")
            else:
                print("Tipo inválido. Use 'E' para Estação ou 'H' para Hospital.")
                continue
            g.addVert(nome, tipo, atributo)

        elif op == "4":
            origem = ler_str("Nome do vértice de origem: ")
            destino = ler_str("Nome do vértice de destino: ")
            tempo = ler_int("Peso/tempo da aresta: ")
            if origem not in g.vertices:
                print(f"Erro: vértice de origem '{origem}' não existe no grafo.")
                return
            if destino not in g.vertices:
                print(f"Erro: vértice de destino '{destino}' não existe no grafo.")
                return
            aresta = Aresta(g.vertices[origem], g.vertices[destino], tempo)
            g.addAresta(aresta)

        elif op == "5":
            nome = ler_str("Nome do vértice a remover: ")
            g.remVert(nome)

        elif op == "6":
            origem = ler_str("Nome do vértice de origem: ")
            destino = ler_str("Nome do vértice de destino: ")
            g.remAresta(origem, destino)

        elif op == "7":
            nome_arquivo = ler_str("Nome do arquivo para exibir: ")
            try:
                with open(nome_arquivo, 'r', encoding='utf-8') as f:
                    print(f"\n--- Conteúdo de '{nome_arquivo}' ---")
                    print(f.read())
                    print(f"--- Fim do arquivo ---\n")
            except FileNotFoundError:
                print(f"Arquivo '{nome_arquivo}' não encontrado.")

        elif op == "8":
            g.mostrar()

        elif op == "9":
            print("Conexidade:", g.conexidade())

        elif op == "0":
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    g = TGrafo()
    menuD(g)
