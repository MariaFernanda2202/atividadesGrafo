lista_vertices = {
    'v1': ['v2','v3'],
    'v2': ['v3', 'v4'],
    'v3': ['v4', 'v5', 'v6'],
    'v4': ['v5', 'v6'],
    'v5': ['v5', 'v1'],
    'v6': ['v1', 'v2'],
}



def pega_vizinho(vertice, lista_vertices):
   return lista_vertices[vertice]

    
def buscar_em_profundidade(lista_vertices):
    
    visitados = []
    pilha_inicial = []   
        
    if len(pilha_inicial) == 0:
        primeiro_vertice = list(lista_vertices.keys())[0]
        pilha_inicial.insert(0, primeiro_vertice) 
                  
        print("Visitados", visitados)
        print("Pilha", pilha_inicial)
    
   
    while len(pilha_inicial) > 0:
        vertice_atual = pilha_inicial.pop(0)
            
        if vertice_atual not in visitados:
            visitados.insert(0, vertice_atual)
            vizinhos = pega_vizinho(vertice_atual, lista_vertices)
                
            for vizinho in vizinhos:
                if vizinho not in visitados and vizinho not in pilha_inicial:
                    pilha_inicial.insert(0, vizinho) 
            print("\nVisitados", visitados)
            print("Pilha\n", pilha_inicial)
    return visitados

def buscar_ciclo(lista_vertices):
    visitados = []
    pilha_inicial = [[],[]]   
        
    if len(pilha_inicial) == 0:
        primeiro_vertice = list(lista_vertices.keys())[0] #v1
        pilha_inicial[0].append(primeiro_vertice) 
        pilha_inicial[0].append(primeiro_vertice) 
                  
        print("Visitados", visitados)
        print("Pilha", pilha_inicial)
    
   
    visitados = buscar_em_profundidade(lista_vertices)
    pass


def main():
    while True:
        print("\n1 - busca em profundidade")
        print("2 - encontre o menor caminhos")
        print("0 - sair")
        opcao = int(input("Escolha: "))

        match opcao:
            case 1:
                buscar_em_profundidade(lista_vertices)
            case 2:
                origem = input("Origem: ")
                destino = input("Destino: ")
                buscar_menor_caminho(origem, destino, lista_vertices)
            case 0:
                print("Adeus")
                break


if __name__ == "__main__":
    main()