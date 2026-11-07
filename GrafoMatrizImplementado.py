def criar_grafo():   
    matriz = []
    vertices = []
    return matriz, vertices


def inserir_vertice(matriz, vertices, vertice):
    if vertice in vertices:
        print("Essa vértice já existe.")
        return

    vertices.append(vertice)

    for linha in matriz:
        linha.append(0)

    linha_nova = []
    for lista in vertices:
        linha_nova.append(0)
    matriz.append(linha_nova)

def inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    if origem not in vertices:
        inserir_vertice(matriz, vertices, origem)
    if destino not in vertices:
        inserir_vertice(matriz, vertices, destino)

    i = vertices.index(origem)
    j = vertices.index(destino)
    matriz[i][j] = 1

    if nao_direcionado:
        matriz[j][i] = 1

def remover_vertice(matriz, vertices, vertice):
    if vertice not in vertices:
        print("Essa vértice não existe.")
        return

    indice = vertices.index(vertice)
    matriz.pop(indice)

    for linha in matriz:
        linha.pop(indice)

    vertices.remove(vertice)

def remover_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    if origem not in vertices or destino not in vertices:
        return

    i = vertices.index(origem)
    j = vertices.index(destino)
    matriz[i][j] = 0

    if nao_direcionado:
        matriz[j][i] = 0

def existe_aresta(matriz, vertices, origem, destino):

    if origem not in vertices or destino not in vertices:
        return False

    i = vertices.index(origem)
    j = vertices.index(destino)

    if matriz[i][j] == 1:
        print(f"Existe a aresta => [{i},{j}]")
        return True
    else:
        print(f"Não existe a aresta")
        return False

def vizinhos(matriz, vertices, vertice):
    """
    Retorna a lista de vizinhos (vértices alcançáveis a partir de 'vertice').

    Passos:
    1. Verificar se 'vertice' existe em 'vertices'.
    2. Obter o índice 'i' correspondente.
    3. Criar uma lista de vizinhos vazia
    4. Para cada item da linha matriz[i], verificar se == 1
        - Adicionar o vértice correspondente na lista de vizinhos
    5. Retornar essa lista.
    """
    if vertice not in vertices:
        return []

    i = vertices.index(vertice)
    lista_vizinhos = []

    for j in range(len(matriz[i])):
        if matriz[i][j] == 1:
            lista_vizinhos.append(vertices[j])

    return lista_vizinhos

def grau_vertices(matriz, vertices, nao_direcionado = False):
    graus = {}

    for i in range(len(vertices)):
        grau_saida = 0
        grau_entrada = 0

        for valor in matriz[i]:
            grau_saida = grau_saida + valor

        if nao_direcionado:
            
            graus[vertices[i]] = grau_saida
            print(f"Grau do vértice {vertices[i]} = {grau_saida}")
        else:
            for linha in matriz:
                grau_entrada = grau_entrada + linha[i]

            grau_total = grau_entrada + grau_saida
            graus[vertices[i]] = {"saida": grau_saida, "entrada": grau_entrada, "total": grau_total}
            print(f"Vértice {vertices[i]}, grau de saída: {grau_saida}, grau de entrada: {grau_entrada}, total de grau: {grau_total}")

    return graus

def percurso_valido(matriz, vertices, caminho):
    if isinstance(caminho, str):
        caminho = caminho.replace("[", "").replace("]", "").replace(" ", "").split(",")
    
    for i in range(len(caminho)-1):
        cidade1 = caminho[i]
        cidadeaolado = caminho[i+1]
        if not existe_aresta(matriz, vertices, cidade1, cidadeaolado):
            print("Caminho impossível")
            return False
    print("O caminho existe")
    return True


def listar_vizinhos(matriz, vertices, vertice):

    if vertice not in vertices:
        print("Essa vértice não existe.")
        return []

    lista = vizinhos(matriz, vertices, vertice)
    print("Vizinhos de", vertice, ":", lista)
    return lista

def exibir_grafo(matriz, vertices):
    cabecalho = "   "
    for vertice in vertices:
        cabecalho = cabecalho + vertice + " "
    print(cabecalho)

    for i in range(len(matriz)):
        linha_texto = vertices[i] + " "
        for valor in matriz[i]:
            linha_texto = linha_texto + str(valor) + "  "
        print(linha_texto)


def popular_grafo(matriz, vertices, nao_direcionado=False):
    inserir_vertice(matriz, vertices, "v1")
    inserir_vertice(matriz, vertices, "v2")
    inserir_vertice(matriz, vertices, "v3")
    inserir_vertice(matriz, vertices, "v4")

    inserir_aresta(matriz, vertices, "v1", "v2", nao_direcionado)
    inserir_aresta(matriz, vertices, "v1", "v3", nao_direcionado)
    inserir_aresta(matriz, vertices, "v2", "v4", nao_direcionado)
    inserir_aresta(matriz, vertices, "v3", "v4", nao_direcionado)

def main():

    matriz, vertices = criar_grafo()
    tipo = input("Grafo não direcionado?): ")
    nao_direcionado = tipo.lower() == "s" or tipo.lower() == "sim"

    while True:
        print("\n1 - Mostrar grafo")
        print("2 - Inserir vértice")
        print("3 - Remover vértice")
        print("4 - Inserir aresta")
        print("5 - Remover aresta")
        print("6 - Listar vizinhos")
        print("7 - Popular grafo")
        print("8 - Existe aresta")
        print("9 - Graus dos vértices")
        print("10 - Encontrar percurso")
        print("0 - Sair")
        opcao = int(input("Escolha: "))

        match opcao:
            case 1:
                exibir_grafo(matriz, vertices)
            case 2:
                vertice = input("Vértice: ")
                inserir_vertice(matriz, vertices, vertice)
            case 3:
                vertice = input("Vértice: ")
                remover_vertice(matriz, vertices, vertice)
            case 4:
                origem = input("Origem: ")
                destino = input("Destino: ")
                inserir_aresta(matriz, vertices, origem, destino, nao_direcionado)
            case 5:
                origem = input("Origem: ")
                destino = input("Destino: ")
                remover_aresta(matriz, vertices, origem, destino, nao_direcionado)
            case 6:
                vertice = input("Vértice: ")
                listar_vizinhos(matriz, vertices, vertice)
            case 7:
                popular_grafo(matriz, vertices, nao_direcionado)
                exibir_grafo(matriz, vertices)
            case 8:
                origem = input("Informe o lugar de origem: ")
                destino = input("Informe o lugar de destino: ")
                existe_aresta(matriz, vertices, origem, destino)
            case 9:
                grau_vertices(matriz, vertices, nao_direcionado)
            case 10:
                caminho = input("Informe um caminho que deseja saber se existe: ")
                percurso_valido(matriz, vertices, caminho)
            case 0:
                print("Adeus")
                break




if __name__ == "__main__":
    main()
