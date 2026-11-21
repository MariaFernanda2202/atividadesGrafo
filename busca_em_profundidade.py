# lista_vertices = {
#     'v1': ['v2','v3'],
#     'v2': ['v3', 'v4'],
#     'v3': ['v4', 'v5', 'v6'],
#     'v4': ['v5', 'v6'],
#     'v5': ['v5', 'v1'],
#     'v6': ['v1', 'v2'],
# }

lista_vertices = { 
    'v1': ['v2', 'v3'],
    'v2': ['v1', 'v4'],
    'v3': ['v1', 'v5'],
    'v4': ['v2'],
    'v5': ['v3', 'v6'],
    'v6': ['v5']
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
    pilha_inicial = []   
    
    primeiro_vertice = list(lista_vertices.keys())[0] 

    pilha_inicial.append({
        'vertice': primeiro_vertice,
        'pai': None
    }) 
                  
    while pilha_inicial:
        vertice_atual = pilha_inicial.pop()

        vertice = vertice_atual['vertice']
        pai = vertice_atual['pai']

        if vertice not in visitados:

            visitados.append(vertice)

            vizinhos = pega_vizinho(vertice, lista_vertices)

            for vizinho in vizinhos:

                if vizinho not in visitados:

                    pilha_inicial.append({
                        'vertice': vizinho,
                        'pai': vertice
                    })

                elif vizinho != pai:
                    
                    return True
                    
    return False


def main():
    while True:
        print("\n1 - busca em profundidade")
        print("2 - verificar ciclo")
        print("0 - sair")
        opcao = int(input("Escolha: "))

        match opcao:
            case 1:
                buscar_em_profundidade(lista_vertices)
            case 2:
                if buscar_ciclo(lista_vertices):
                    print("O grafo tem um ciclo.")
                else:
                    print("O grafo não tem ciclos.")
            case 0:
                print("Adeus")
                break


if __name__ == "__main__":
    main()