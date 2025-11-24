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
# cálculo de grau dos vértices e verificação de grafo euleriano no menu

# 21/11/2025: Larissa: verificação de erros para grafo vazio ou não carregado

# 23/11/2025: Larissa: atualização do menu para incluir as novas funcionalidades
# (listar hospitais por tempo e encontrar rota entre estação e hospital)

# 23//11/2025: Julia: atualização do menu para incluir função de visualização da imagem PNG do grafo, adição de comentários para melhor organização, atualização do README.md 

###################################################################################

from lista import Est_Est, Est_Hosp, TGrafo, Vertice, Aresta, Estacao, Hospital, gArquivo
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#--- FUNÇÕES DE LEITURA DE INTEIRO E STRING ---
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
14) Encontrar rota entre estação e hospital (Dijkstra).
15) Visualizar imagem PNG do arquivo (grafo.txt), montado na ferramenta Graph Online.
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
                vertices.append([nome, tipo_v, atributo])
            m = ler_int("Insira o número de arestas: ")
            arestas = []
            for i in range(m):
                nome1 = ler_str(f"Nome do vértice de origem da aresta {i+1}: ")
                nome2 = ler_str(f"Nome do vértice de destino da aresta {i+1}: ")
                peso = ler_int(f"Peso da aresta {i+1}: ")
                
                # Encontre o tipo de cada vértice (busca simples na lista)
                tipo1 = ""
                tipo2 = ""
                for vert in vertices:
                    if vert[0] == nome1:
                        tipo1 = vert[1]
                    if vert[0] == nome2:
                        tipo2 = vert[1]
                # Decide se precisa do modo de locomoção
                if (tipo1 == "E" and tipo2 == "H") or (tipo1 == "H" and tipo2 == "E"):
                    modo = ler_str(f"Modo de locomoção dessa ligação (ex: CAMINHADA, ONIBUS): ")
                    arestas.append([nome1, nome2, peso, modo])
                else:
                    arestas.append([nome1, nome2, peso, None])

            nome_arquivo = ler_str("Nome do arquivo para salvar o grafo: ")
            try:
                with open(nome_arquivo, 'w', encoding='utf-8') as f:
                    f.write(f"{tipo_grafo}\n")
                    f.write(f"{n}\n")
                    for v in vertices:
                        f.write(f'"{v[0]}" "{v[1]}" "{v[2]}"\n')
                    f.write(f"{m}\n")
                    for a in arestas:
                        if a[3] is not None:
                            f.write(f'"{a[0]}" "{a[1]}" {a[2]} {a[3]}\n')
                        else:
                            f.write(f'"{a[0]}" "{a[1]}" {a[2]}\n')
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

            v1 = g.vertices[origem]
            v2 = g.vertices[destino]

            if (isinstance(v1, Estacao) and isinstance(v2, Hospital)) or (isinstance(v2, Estacao) and isinstance(v1, Hospital)):
                modo = ler_str("Modo de locomoção (ex: CAMINHADA, ONIBUS): ")
                aresta = Est_Hosp(v1, v2, tempo, modo)
            elif isinstance(v1, Estacao) and isinstance(v2, Estacao):
                aresta = Est_Est(v1, v2, tempo)
            else:
                aresta = Aresta(v1, v2, tempo)
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
                    modos = g.modos()
                    if not modos:
                        print("Não há modos de locomoção registrados no grafo (arestas Estação-Hospital).")
                        continue
                    print("Modos disponíveis:", ', '.join(modos))
                    modo = ler_str("Escolha o modo de locomoção exatamente como aparece acima: ").lower()
                    if modo not in modos:
                        print("Modo não encontrado. Tente novamente.")
                        continue
                    g.listarHospitais(modo)
            else:
                print("Grafo não carregado ou vazio. Use a opção 1 para carregar um grafo.")
            
    
        elif op == "14":
            if g is not None and len(g.vertices) > 0:
                origem = ler_str("Nome da estação de origem: ")
                if origem not in g.vertices or not isinstance(g.vertices[origem], Estacao):
                    print("Origem inválida. Escolha uma estação existente.")
                    continue
                destino = ler_str("Nome do hospital desejado: ")
                if destino not in g.vertices or not isinstance(g.vertices[destino], Hospital):
                    print("Destino inválido. Escolha um hospital existente.")
                    continue
                caminho, tempo = g.dijkstra(origem, destino)
                if caminho is None:
                    print("Não existe caminho entre origem e hospital.")
                else:
                    print("Melhor caminho encontrado:")
                    print(" -> ".join(caminho))
                    print(f"Tempo total: {tempo} min")
            else:
                print("Grafo não carregado ou vazio. Use a opção 1 para carregar um grafo.")

        elif op == "15":
            try:
                img = mpimg.imread("grafo_mapa.png")
                plt.imshow(img)
                plt.axis("off")
                try:
                    plt.show(block=False)
                    plt.pause(0.1)
                except TypeError:
                    plt.show()
                print("Imagem visualizada com sucesso.")

            except Exception as e:

                print(f"Erro ao carregar a imagem: {e}")

        elif op == "0":
            print("Saindo do programa. Até mais!")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menuD()
