def criar_grafo():
    return {"vertices": [], "arestas": []}


def inserir_vertice(grafo, vertice):
    if vertice in grafo["vertices"]:
        print("Essa vértice já existe.")
        return
    grafo["vertices"].append(vertice)


def inserir_aresta(grafo, origem, destino, nao_direcionado=False):
    if origem not in grafo["vertices"]:
        inserir_vertice(grafo, origem)
    if destino not in grafo["vertices"]:
        inserir_vertice(grafo, destino)

    aresta = [origem, destino]
    if aresta not in grafo["arestas"]:
        grafo["arestas"].append(aresta)

    if nao_direcionado:
        inversa = [destino, origem]
        if inversa not in grafo["arestas"]:
            grafo["arestas"].append(inversa)


def remover_aresta(grafo, origem, destino, nao_direcionado=False):
    aresta = [origem, destino]
    if aresta in grafo["arestas"]:
        grafo["arestas"].remove(aresta)

    if nao_direcionado:
        inversa = [destino, origem]
        if inversa in grafo["arestas"]:
            grafo["arestas"].remove(inversa)


def remover_vertice(grafo, vertice, nao_direcionado=True):
    if vertice not in grafo["vertices"]:
        print("Essa vértice não existe.")
        return

    restantes = []
    for aresta in grafo["arestas"]:
        if aresta[0] != vertice and aresta[1] != vertice:
            restantes.append(aresta)

    grafo["arestas"] = restantes
    grafo["vertices"].remove(vertice)


def vizinhos(grafo, vertice):
    resultado = []
    for aresta in grafo["arestas"]:
        if aresta[0] == vertice:
            if aresta[1] not in resultado:
                resultado.append(aresta[1])
    return resultado


def listar_vizinhos(grafo, vertice):
    if vertice not in grafo["vertices"]:
        print("Essa vértice não existe.")
        return []
    resultado = vizinhos(grafo, vertice)
    print("Vizinhos de", vertice, ":", resultado)
    return resultado


def exibir_grafo(grafo):
    print("Vértices:", grafo["vertices"])
    print("Arestas:", grafo["arestas"])


def existe_aresta(grafo, origem, destino):
    aresta = [origem, destino]
    if aresta in grafo["arestas"]:
        print(f"A aresta [{origem},{destino}] existe no grafo")
        return True
    else:
        print(f"A aresta [{origem},{destino}] não foi encontrada no grafo")
        return False


def grau_vertices(grafo):
    grau = {}
    for v in grafo["vertices"]:
        grau[v] = { "out": 0, "in": 0, "total": 0}
        
        for a in grafo["arestas"]:
            if a[0] == v:
                grau[v]["out"] += 1
            if a[1] == v:
                grau[v]["in"] += 1
                 
        grau[v]["total"] = (grau[v]["in"]+grau[v]["out"])
        print(f"Grau do vértice {v} = {grau[v]}")
    pass


def percurso_valido(grafo, caminho):
    if isinstance(caminho, str):
        caminho = caminho.replace("[", "").replace("]", "").replace(" ", "").split(",")
        
    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i+1]
        if not existe_aresta(grafo, origem, destino):
            print(f"Caminho impossível, não existem arestas que ligem esse caminho")
            return False
        
    print("O caminho existe")
    return True


# fiz um direto pra n ter q ficar preenchendo toda vez q for usar o grafo
def carregar_exemplo(grafo, nao_direcionado=False):
    for vertice in ["v1", "v2", "v3", "v4", "v5"]:
        if vertice not in grafo["vertices"]:
            inserir_vertice(grafo, vertice)

    inserir_aresta(grafo, "v1", "v2", nao_direcionado)
    inserir_aresta(grafo, "v3", "v4", nao_direcionado)
    inserir_aresta(grafo, "v5", "v1", nao_direcionado)
    inserir_aresta(grafo, "v4", "v2", nao_direcionado)
    inserir_aresta(grafo, "v3", "v1", nao_direcionado)


def main():
    grafo = criar_grafo()
    tipo = input("Grafo não direcionado? (s/n): ")
    nao_direcionado = tipo.lower() == "s"
    while True:
        print("\n1 - Mostrar grafo")
        print("2 - Inserir vértice")
        print("3 - Remover vértice")
        print("4 - Inserir aresta")
        print("5 - Remover aresta")
        print("6 - Listar vizinhos")
        print("7 - Carregar exemplo de teste")
        print("8 - Exibir aresta")
        print("9 - Encontrar uma aresta")
        print("10 - Grau dos vértices")
        print("11 - Percurso válido")
        print("0 - Sair")
        opcao = int(input("Escolha: "))

        match opcao:
            case 1:
                exibir_grafo(grafo)
            case 2:
                vertice = input("Vértice: ")
                inserir_vertice(grafo, vertice)
            case 3:
                vertice = input("Vértice: ")
                remover_vertice(grafo, vertice)
            case 4:
                origem = input("Origem: ")
                destino = input("Destino: ")
                inserir_aresta(grafo, origem, destino, nao_direcionado)
            case 5:
                origem = input("Origem: ")
                destino = input("Destino: ")
                remover_aresta(grafo, origem, destino, nao_direcionado)
            case 6:
                vertice = input("Vértice: ")
                listar_vizinhos(grafo, vertice)
            case 7:
                carregar_exemplo(grafo, nao_direcionado)
                exibir_grafo(grafo)
            case 8:
                exibir_grafo(grafo)
            case 9:
                origem = input('Informe a vértice origem: ')
                destino = input('Informe a vértive destino: ')
                existe_aresta(grafo, origem, destino)
            case 10:
                grau_vertices(grafo)
            case 11:
                caminho = input("informe o ponto de saída e de chegada: (Ex: [v1,v2]): ")
                percurso_valido(grafo, caminho)
            case 0:
                print("Adeus")
                break


if __name__ == "__main__":
    main()
