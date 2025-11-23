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

# 29/09/2025: Larissa: arrumar main para que possa manipular o grafo
# lido a partir do txt

# 20/11/2025: Larissa: inserir funções de coloração sequencial,
# cálculo de grau dos vértices e verificação de grafo euleriano

# 21/11/2025: Larissa: verificação de erros para grafo vazio ou não carregado


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

def menuD():
    g = TGrafo()  # Inicializa o grafo dentro da função
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
10) Aplicar Coloração Sequencial de Vértices.
11) Calcular grau dos vértices.
12) Verificar se o grafo é euleriano.
13) Listar hospitais por tempo.
 0) Sair
==========================================================================
"""
    while True:
        print(MENU)
        op = input("Selecione uma opção: ").strip()

        if op == "1":
            arq = input("\nNome do arquivo (ex.: 'grafo.txt'): ").strip()
            g = gArquivo(arq)
            print("\nLista de Adjacência resultante:\n")
            g.mostrar()

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
                continue
            if destino not in g.vertices:
                print(f"Erro: vértice de destino '{destino}' não existe no grafo.")
                continue
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
            if g is not None and len(g.vertices) > 0:
                g.mostrar()
            else:
                print("Grafo não carregado ou vazio. Use a opção 1 para carregar um grafo.")

        elif op == "9":
            if g is not None and len(g.vertices) > 0:
                print("Conexidade:", g.conexidade())
            else:
                print("Grafo não carregado ou vazio. Use a opção 1 para carregar um grafo.")
        
        elif op == "10":
            if g is not None and len(g.vertices) > 0:
                g.colorir(list(g.vertices.keys()))
            else:
                print("Grafo não carregado ou vazio. Use a opção 1 para carregar um grafo.")
                       
        elif op == "11":
            if g is not None and len(g.vertices) > 0:
                for vertice in g.vertices.values():
                    grau = g.degreeND(vertice.nome)
                    print(f"Grau do vértice '{vertice.nome}': {grau}")
            else:
                print("Grafo não carregado ou vazio. Use a opção 1 para carregar um grafo.")
        
        elif op == "12":
            if g is not None and len(g.vertices) > 0:
                print("O grafo é Euleriano." if g.euleriano() else "O grafo não é Euleriano.")
            else:
                print("Grafo não carregado ou vazio. Use a opção 1 para carregar um grafo.")
        
        elif op == "13":
            if g is not None and len(g.vertices) > 0:
                    modos = g.modos_existentes()
                    if not modos:
                        print("Não há modos de locomoção registrados no grafo (arestas Estação-Hospital).")
                        continue
                    print("Modos disponíveis:", ', '.join(modos))
                    modo = ler_str("Escolha o modo de locomoção exatamente como aparece acima: ").lower()
                    if modo not in modos:
                        print("Modo não encontrado. Tente novamente.")
                        continue
                    g.listar_hospitais_por_menor_aresta_modo(modo)
            else:
                print("Grafo não carregado ou vazio. Use a opção 1 para carregar um grafo.")

        elif op == "0":
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menuD()
