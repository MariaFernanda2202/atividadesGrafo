def criar_grafo():
    """
    Cria e retorna uma estrutura de grafo com lista de arestas e lista de vértices.

    Passos:
    1. Criar uma lista vazia chamada 'vertices'.
    2. Criar uma lista vazia chamada 'arestas', onde cada elemento será uma lista de tamanho 2 (origem, destino)
    3. Retornar vertices e arestas
    """
    vertices = []
    arestas = []
    return vertices, arestas


def inserir_vertice(vertices, vertice):
    """
    Adiciona um novo vértice no grafo.

    Passos:
    1. Verificar se o vértice já existe em 'vertices'.
    2. Se não existir, adicionar à lista 'vertices'.
    """

    if vertice in vertices: 
        print(f"A vértice {vertice}, já existe na lista de vértices")
        return
    vertices.append(vertice)
    return vertices

def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=False):
    """
    Adiciona uma aresta entre dois vértices.

    Passos:
    1. Garantir que 'origem' e 'destino' existam em 'vertices'.
       - Se não existirem, chamar 'inserir_vertice' para adicioná-los.
    2. Adicionar uma lista [origem, destino] na lista 'arestas'.
    3. Se nao_direcionado=True, adicionar também [destino, origem].
    """
    if origem not in vertices:
        print("Vértice origem não existe")
        print("Vou adicioná-la como uma vertice")
        inserir_vertice(vertices, origem)
    if destino not in vertices:
        print("Vértice destino não existe")
        print("Vou adicioná-la como uma vertice")
        inserir_vertice(vertices, destino)
        
        
    aresta = [origem, destino]
    arestas.append(aresta)
    if nao_direcionado == False:
        aresta2 = [destino, origem]
        arestas.append(aresta2)
        
    return arestas

def remover_aresta(arestas, origem, destino, nao_direcionado=False):
    """
    Remove uma aresta entre dois vértices.

    Passos:
    1. Percorrer a lista de Arestas procurando [origem, destino]
    2. Se encontrar, remover
    3. Se nao_direcionado=True, também procurar por [destino, origem]
    """
    aresta_excluir = [origem, destino] 
    aresta_excluir_invertida = [destino, origem]
    
    for aresta in arestas:
        if aresta == aresta_excluir or (nao_direcionado and aresta == aresta_excluir_invertida):
            arestas.remove(aresta)
            print("Aresta e sua inversão (caso haja) foram excluidas com sucesso!")
            return
        
    print("Aresta informada não existe!")
    return
            


def remover_vertice(vertices, arestas, vertice):
    """
    Remove um vértice e todas as arestas conectadas a ele.

    Passos:
    1. Verificar se o vértice existe na lista de vertices.
    2. Caso encontrado, remover o vértice da lista 'vertices'.
    3. Percorrer a lista de 'arestas' e remover todas onde o vértice aparece
       como origem ou destino.
    """
    if vertice in vertices:
        vertices.remove(vertice)
        for aresta in arestas[:]:
            if aresta[0] == vertice or aresta[1] == vertice:
                arestas.remove(aresta)
        print("Vértice e suas arestas removidas com sucesso")
        return
    print("Vértice não existe no grafo")
    return

def existe_aresta(arestas, origem, destino):
    """
    Verifica se existe uma aresta entre origem e destino.

    Passos:
    1. Percorrer a lista de aresta procurando [origem, destino]
    2. Retornar True se encontrar
    3. Caso não encontre na lista, retornar False no final.
    """
    
    for aresta in arestas:
        if aresta[0] == origem and aresta[1] == destino:
            print("Aresta existe")
            return True
    print("Aresta não encontrada")
    return False


def vizinhos(vertices, arestas, vertice):
    """
    Retorna a lista de vizinhos (vértices alcançáveis a partir de 'vertice').

    Passos:
    1. Criar uma lista vazia chamada 'vizinhos'.
    2. Percorrer todas as arestas [origem, destino].
    3. Se origem == vertice, adicionar destino na lista de vizinhos.
    4. Retornar a lista final.
    """
    
    vizinhos = []
    for aresta in arestas:
        if aresta[0] == vertice:
                vizinhos.append(aresta[1])
    return vizinhos


def grau_vertices(vertices, arestas, nao_direcionado=True):
    """
    Calcula o grau de entrada, saída e total de cada vértice.

    Passos:
    1. Criar um dicionário vazio 'graus'.
    2. Percorrer todas as arestas [origem, destino]:
        I. Se o grafo for não direcionado:
            - incrementar grau analisando apenas se origem ou destino equivale ao vértice analisado
        II. Se o grafo for direcionado
            - Se o vértice for origem Incrementar grau de saída do vértice origem
            - Se o vértice for destino incrementar grau de entrada do vértice destino.
            - Calcular o grau total (entrada + saída).
    4. Retornar o dicionário 'graus' para cada vértice.
    """
    graus = {}
    
    for vertice in vertices:
        graus[vertice] = {"entrada": 0, "saida": 0, "total": 0}
        
    for aresta in arestas:
        if nao_direcionado:
            if aresta[0] in graus:
                graus[aresta[0]]["total"] += 1
            if aresta[1] in graus:
                if aresta[0] != aresta[1]:
                    graus[aresta[1]]["total"] += 1
        else:
            if aresta[0] in graus:
                graus[aresta[0]]["saida"] += 1
            if aresta[1] in graus:
                graus[aresta[1]]["entrada"] += 1
                
    if not nao_direcionado:
        for vertice in graus:
            graus[vertice]["total"] = graus[vertice]["saida"] + graus[vertice]["entrada"]         

    return graus

def percurso_valido(arestas, caminho):
    """
    Verifica se um percurso é possível (seguindo as arestas na ordem dada).

    Passos:
    1. Percorrer o caminho de 0 até len(caminho) - 2.
    2. Para cada par consecutivo (u, v):
        - Verificar se (u, v) existe na lista de 'arestas' (funcao existe_aresta).
        - Se alguma não existir, retornar False.
    3. Se todas existirem, retornar True.
    """
    if isinstance(caminho, str):
        caminho = [v.strip() for v in caminho.split(",")]
        
    for i in range(len(caminho) - 2):
        origem = caminho[i]
        destino = caminho[i+1]
        
        if not existe_aresta(arestas, origem, destino):
            return False
    return True    


def listar_vizinhos(vertices, arestas, vertice):
    """
    Exibe os vizinhos de um vértice.

    Passos:
    1. Chamar a função vizinhos() para obter a lista.
    2. Exibir a lista formatada.
    """
    lista_vizinhos = vizinhos(vertices, arestas, vertice)
    for vizinho in lista_vizinhos:
        print(f"{vertice} vizinho de {vizinho}")
        return


def exibir_grafo(vertices, arestas):
    """
    Exibe todas as arestas do grafo.

    Passos:
    1. Exibir a lista de vértices.
    2. Exibir todas as arestas no formato (origem -> destino).
    """
    print(f"verices: {vertices}")
    print(f"arestas: {arestas}")
    for vertice in vertices:
        for aresta in arestas:
            if aresta[0] == vertice:
                print(f"{vertice}=>{aresta[1]}")
    pass

def grafo_modelo(vertices, arestas, nao_direcionado):
    if nao_direcionado: 
        vertices.extend(["v1", "v2", "v3"])
        arestas.extend([["v1", "v2"], ["v2", "v1"], ["v1", "v3"], ["v2", "v3"], ["v3", "v2"], ["v3", "v1"]])    
    else: 
        vertices.extend(["v1", "v2", "v3"])
        arestas.extend([["v1", "v2"], ["v2", "v3"], ["v3", "v1"]])  
    return vertices, arestas

def main():
    vertices = []
    arestas = []
    tipo = input("Grafo não direcionado?): ")
    nao_direcionado = tipo.lower() == "s" or tipo.lower() == "sim"
    
    while True:
        
            print("Escolha uma operação:")
            print("1 - criar grafo")
            print("2 - inserir vertice")
            print("3 - inserir aresta")
            print("4 - remover vertice")
            print("5 - remover aresta")
            print("6 - arestas existe no grafo")
            print("7 - grau dos vertices")
            print("8 - percurso existe")
            print("9 - listar vizinhos")
            print("10 - exibir grafo")
            print("11 - criar grafo base")
            opcao = int(input("Informe um numero: "))
            
            match opcao:
                case 1:
                    vertices, arestas = criar_grafo()
                    exibir_grafo(vertices, arestas)
                case 2:
                    vertice = input("Informe o vertice para adicionar: ")
                    inserir_vertice(vertices, vertice)
                    exibir_grafo(vertices, arestas)
                case 3:
                    origem = input("Vértice origem: ").strip()
                    destino = input("Vértice destino: ").strip()
                    inserir_aresta(vertices, arestas, origem, destino)
                    exibir_grafo(vertices, arestas)
                case 4:
                    vertice = input("Informe o vértice para excluir: ")
                    remover_vertice(vertices, arestas, vertice)
                    exibir_grafo(vertices, arestas)
                case 5:
                    origem = input("Vértice origem: ")
                    destino = input("Vértice destino: ")
                    remover_aresta(arestas, origem, destino, nao_direcionado)
                    exibir_grafo(vertices, arestas)
                case 6:
                    origem = input("Vértice origem: ")
                    destino = input("Vértice destino: ")
                    existe_aresta(arestas, origem, destino)   
                    exibir_grafo(vertices, arestas)
                case 7:  
                    graus = grau_vertices(vertices, arestas, nao_direcionado)
                    for vertice, grau in graus.items():
                        if nao_direcionado:
                            print(f"{vertice} tem grau de => {grau["total"]}")
                        else:
                            print(f"{vertice} tem os graus => Entrada: {grau['entrada']}; Saída: {grau['saida']}; Total: {grau['total']}.")
                    exibir_grafo(vertices, arestas)
                case 8: 
                    caminho = input("Informe o caminhos que deseja saber se existe: ")
                    percurso = percurso_valido(arestas, caminho)
                    if percurso:
                        print("Existe o caminho")
                    else: 
                        print("Perecurso não existe")
                    exibir_grafo(vertices, arestas)
                case 9:
                    vertice = input("Informe a vértice que deseja ver o vizinhos: ")
                    listar_vizinhos(vertices, arestas, vertice)
                    exibir_grafo(vertices, arestas)
                case 10: 
                    exibir_grafo(vertices, arestas)
                case 11: 
                    grafo_modelo(vertices, arestas, nao_direcionado)
                    exibir_grafo(vertices, arestas)
                case 0: 
                    print("Adeus")
                    break
        

if __name__ == "__main__":
    main()
