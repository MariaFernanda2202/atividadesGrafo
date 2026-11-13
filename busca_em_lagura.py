lista_vertices = {
    'v1': ['v2','v3'],
    'v2': ['v3', 'v4'],
    'v8': ['v2'],
    'v3': ['v4', 'v5', 'v6'],
    'v4': ['v5', 'v6'],
    'v5': ['v5', 'v1'],
    'v6': ['v1', 'v2'],
}



def pega_vizinho(vertice, lista_vertices):
   return lista_vertices[vertice]

    
def buscar_em_largura(lista_vertices):
    
    visitados = []
    fila_inicial = []   
        
    if len(fila_inicial) == 0:
        primeiro_vertice = list(lista_vertices.keys())[0]
        fila_inicial.append(primeiro_vertice) 
                  
        print("Visitados", visitados)
        print("Fila", fila_inicial)
    
   
    while len(fila_inicial) > 0:
        vertice_atual = fila_inicial.pop(0)
            
        if vertice_atual not in visitados:
            visitados.append(vertice_atual)
            vizinhos = pega_vizinho(vertice_atual, lista_vertices)
                
            for vizinho in vizinhos:
                if vizinho not in visitados and vizinho not in fila_inicial:
                    fila_inicial.append(vizinho) 
            print("\nVisitados", visitados)
            print("Fila\n", fila_inicial)
    pass

def buscar_menor_caminho(
    origem, destino, lista_vertices
):
    visitados = []
        
    if origem not in lista_vertices:
        print("Origem não existem no grafo")
        return
    
    if destino not in lista_vertices:
        print("Destino não existem no grafo")
        return 
    
    fila_caminhos = [[origem, [origem]]]
    
    visitados.append(origem)
    
    while len(fila_caminhos) > 0:
        item_atual = fila_caminhos.pop(0)
        vertice_atual = item_atual[0]
        caminho_atual = item_atual[1]
        
        if vertice_atual == destino:
            print("Menor caminho encontrado")
            print(caminho_atual)
            return
        
        if vertice_atual in lista_vertices:
            vizinhos = pega_vizinho(vertice_atual, lista_vertices)
        
            for vizinho in vizinhos:
                if vizinho not in visitados:
                    visitados.append(vizinho)
                    
                    caminho_vertice = list(caminho_atual)
                    caminho_vertice.append(vizinho)
                    fila_caminhos.append([vizinho, caminho_vertice])            
            
    print('Caminho não existe')
    return        



def main():
    while True:
        print("\n1 - busca em largura")
        print("2 - encontre o menor caminhos")
        print("0 - sair")
        opcao = int(input("Escolha: "))

        match opcao:
            case 1:
                buscar_em_largura(lista_vertices)
            case 2:
                origem = input("Origem: ")
                destino = input("Destino: ")
                buscar_menor_caminho(origem, destino, lista_vertices)
            case 0:
                print("Adeus")
                break


if __name__ == "__main__":
    main()