# 🚇🏥 MetrôSaúde: Acessibilidade a Hospitais Públicos via Rede Metropolitana de Transporte

---

## 👩‍💻 Equipe
- **Julia Santos Oliveira | 10417672**
- **Larissa Yuri Sato | 10418318**
  
---

## Descrição do Projeto

### O Problema 
A mobilidade urbana e o acesso equitativo aos serviços públicos de saúde continuam sendo desafios significativos nas grandes cidades brasileiras. Embora a rede metropolitana de transporte (metrô e CPTM) possua grande capacidade de transportar pessoas com rapidez e regularidade, ainda existem regiões onde a população enfrenta dificuldades para alcançar hospitais públicos de forma eficiente, especialmente em situações de urgência. Essa limitação contribui para desigualdades no atendimento, ampliando barreiras sociais e geográficas.

Esse cenário está diretamente associado a dois Objetivos de Desenvolvimento Sustentável:

- **Saúde e Bem-Estar (ODS 3)**, pois o acesso rápido e igualitário aos hospitais influencia a qualidade de vida, reduz mortalidade em emergências e garante atendimento ágil.
- **Cidades e Comunidades Sustentáveis (ODS 11)**, já que a integração entre transporte coletivo e infraestrutura de saúde é essencial para um planejamento urbano inclusivo, sustentável e capaz de reduzir desigualdades territoriais.

Assim, o problema central que buscamos enfrentar é: **como a rede metropolitana de transporte contribui, ou deixa de contribuir, para aproximar a população dos hospitais públicos e garantir um acesso mais justo aos serviços de saúde?**

### Nossa Proposta
Com base nesse contexto, o projeto **MetrôSaúde** foi desenvolvido para avaliar de forma sistemática a cobertura da rede metropolitana de transporte em relação aos hospitais públicos. Aproveitando tanto o caráter essencial do metrô para a população quanto nossa familiaridade com a malha metroviária de São Paulo e com ferramentas como o Google Maps, propomos um estudo que integra mobilidade urbana, saúde pública e análise computacional por meio de grafos.

O projeto analisa como o sistema atual influencia o acesso da população aos hospitais, identificando regiões potencialmente desassistidas ou com deslocamentos mais longos. A partir dessa abordagem, buscamos oferecer insumos para o planejamento urbano, indicando áreas que podem se beneficiar da criação de novas estações, da expansão da cobertura metroviária ou da melhoria das conexões já existentes.

Além de abordar desigualdades de mobilidade e saúde – temas ainda pouco discutidos, mas fundamentais —, o estudo reforça a importância da integração entre infraestrutura de transporte e serviços públicos de saúde para construir cidades mais acessíveis, inclusivas e sustentáveis.

---

## Coleta de Dados

A coleta de dados do projeto envolve a integração de diferentes fontes que permitem representar, de forma precisa, a relação entre a rede metropolitana de transporte de São Paulo e os hospitais públicos. Para compor a base hospitalar, utilizamos informações disponibilizadas pela Prefeitura de São Paulo, incluindo localização e especialidades médicas de cada unidade. Esses dados foram extraídos tanto do portal de hospitais municipais ([Hospitais Municipais - Secretaria Municipal da Saúde](https://prefeitura.sp.gov.br/web/saude/w/hospitais-municipais) quanto da relação completa de estabelecimentos de saúde publicada pela Secretaria Municipal da Saúde ([Relação de Hospitais Municipais - Prefeitura de São Paulo](https://drive.prefeitura.sp.gov.br/cidade/secretarias/upload/saude/arquivos/cis/2024-03-19_Relacao-Estabelecimentos-Completa.pdf)).

Paralelamente, a estrutura da rede metropolitana de transporte sobre trilhos foi obtida a partir do mapa oficial do Metrô de São Paulo ([Mapa do Transporte Metropolitano](https://www.metro.sp.gov.br/wp-content/uploads/2025/09/Mapa-de-rede.pdf)), que contém todas as estações, linhas e conexões atualmente em operação, de metrô e trens. Esses dados possibilitam reconstruir a malha metroviária no grafo de forma fiel e atualizada, representando corretamente tanto as interligações quanto a organização física do sistema.

Além das informações estruturais, o projeto também incorpora dados referentes a tempos de deslocamento, distâncias, rotas e alternativas de transporte, obtidos diretamente pelo Google Maps. Essa etapa inclui estimativas reais de trajeto entre estações e hospitais, considerando diferentes meios de transporte, como caminhada, carro ou integração com ônibus. Dessa forma, a coleta de dados reúne um conjunto robusto e interconectado de informações, permitindo análises consistentes sobre mobilidade urbana, acessibilidade e impacto da rede metropolitana de transporte no acesso aos serviços públicos de saúde.

---

## Estrutura

A estrutura do grafo adotado neste projeto é **ponderada**, dado que precisávamos atribuir pesos aos vértices e arestas, e **não-direcionada**, devido à possibilidade das rotas contempladas serem tanto de ida quanto de volta.

O grafo é composto por **200 vértices**, divididos em dois grupos principais:

- **Estações de metrô e trem**, abrangendo todas as linhas.
- **Hospitais públicos**, cada um com sua especialidade principal.

Cada estação armazena a cor referente à linha à qual pertence, enquanto os hospitais registram sua especialidade médica (ex.: cardiologia, pediatria).

As **209 arestas** se dividem em dois tipos:

1. **Estação de origem – estação de destino**: armazenam o tempo médio de percurso entre estações.
2. **Estação de destino – hospital**: registram o meio de transporte alternativo utilizado (caminhada, carro, ônibus) e o tempo estimado de deslocamento.

---

## Montagem

Para os vértices, primeiro replicamos cuidadosamente o **Mapa do Transporte Metropolitano de São Paulo**, com suas **172 estações** das linhas em operação. Em seguida, selecionamos **28 hospitais municipais**, escolhidos por proximidade em relação às estações.

Para as arestas:

- As conexões entre **estações** utilizaram tempos reais de deslocamento fornecidos pelo Google Maps.
- As conexões entre **estações e hospitais** usaram um meio alternativo de transporte escolhido (caminhada) e tempo igualmente calculado pela plataforma.

**Figura 1: Mapa do Transporte Metropolitano de São Paulo**
<img width="953" height="760" alt="image" src="https://github.com/user-attachments/assets/15c3a269-8670-47d0-b72c-3d00a1a928a7" />


**Figura 2: Grafo montado no Graph Online**
<img width="1281" height="572" alt="image" src="https://github.com/user-attachments/assets/dab55995-2a37-4c17-9b0d-aa9671bcf0d1" />

---

## Implementação

O projeto **MetrôSaúde** foi desenvolvido inteiramente em **Python**, linguagem escolhida pela clareza sintática, grande ecossistema de bibliotecas e facilidade no uso de estruturas como grafos. Optamos por utilizar **classes para vértices e arestas**, já que cada elemento possui atributos específicos e pesos distintos.

A representação do grafo é feita por **listas de adjacência**, mais eficientes e intuitivas que matrizes de adjacência, especialmente em grafos grandes e de baixa densidade. Para facilitar identificação, utilizamos **dicionários**, permitindo trabalhar diretamente com nomes de estações e hospitais (strings).

### Funções Disponíveis
Nossa aplicação oferece um conjunto de funcionalidades que permitem ao usuário manipular e analisar o grafo que representa a integração entre estações metroviárias e hospitais públicos. O sistema apresenta um menu interativo com diferentes operações, descritas a seguir.

- **Ler Arquivo de Dados**  
  Carrega o grafo a partir do arquivo “grafo.txt”.

- **Gravar Arquivo de Dados**  
  Salva toda a estrutura atual do grafo no arquivo “grafo.txt”.

- **Adicionar Vértice**  
  Permite inserir um novo vértice (Estação ou Hospital).

- **Adicionar Aresta**  
  Cria uma conexão entre dois vértices, com tempo de deslocamento.

- **Remover Vértice**  
  Exclui um vértice e todas as suas arestas associadas.

- **Remover Aresta**  
  Remove a conexão entre dois vértices.

- **Exibir Lista de Adjacência**  
  Mostra o grafo em forma de lista de adjacência.

- **Analisar Conexidade**  
  Verifica se o grafo é conexo.

- **Colorir Vértices**  
  Aplica o algoritmo sequencial de coloração aos vértices.

- **Calcular Grau dos Vértices**  
  Exibe o grau (quantidade de conexões) de cada vértice.

- **Verificar se o Grafo é Euleriano**  
  Avalia se o grafo atende às condições para ser considerado euleriano.

- **Encerrar Execução**  
  Finaliza a aplicação de forma segura.

### 🗺️ Interface Proposta
- **Protótipo no Figma:**  
  [Figma – Projeto IHC/Grafos](https://www.figma.com/design/KiJJ8dxm0PF48l1yWeD62W/Projeto---IHC---Grafos?node-id=31-911)

