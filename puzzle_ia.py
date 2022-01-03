from copy import copy
from queue import Queue


class No:
    def __init__(self, estado, custo_caminho, custo_busca, caminho):
        self.estado = estado
        self.custo_caminho = custo_caminho
        self.custo_busca = custo_busca
        self.caminho = copy(caminho)

def swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


def expande(no, custo_busca):
    pos_vazio = no.estado.index('X')

    CIMA = -3
    BAIXO = 3
    ESQUERDA = -1
    DIREITA = 1

    NUM_QUADROS = 9
    largura = 3

    nos_expandidos = []

    #se for possível mover para cima,
    if (pos_vazio + CIMA >= 0):
        novo_estado = copy(no.estado)
        swap(novo_estado, pos_vazio, pos_vazio + CIMA)

        novo_caminho = copy(no.caminho)
        novo_caminho.append(novo_estado)
        
        custo_busca += 1
        novo_no = No(novo_estado, no.custo_caminho + 1, custo_busca, novo_caminho)

        nos_expandidos.append(novo_no)

    #se for possível mover para baixo
    if (pos_vazio + BAIXO < NUM_QUADROS):
        novo_estado = copy(no.estado)
        swap(novo_estado, pos_vazio, pos_vazio + BAIXO)

        novo_caminho = copy(no.caminho)
        novo_caminho.append(novo_estado)
        
        custo_busca += 1
        novo_no = No(novo_estado, no.custo_caminho + 1, custo_busca, novo_caminho)

        nos_expandidos.append(novo_no)

    #se for possível mover para a esquerda
    if ((pos_vazio + ESQUERDA) % largura != largura - 1):
        novo_estado = copy(no.estado)
        swap(novo_estado, pos_vazio, pos_vazio + ESQUERDA)

        novo_caminho = copy(no.caminho)
        novo_caminho.append(novo_estado)
        
        custo_busca += 1
        novo_no = No(novo_estado, no.custo_caminho + 1, custo_busca, novo_caminho)

        nos_expandidos.append(novo_no)
        
    #se for possível mover para a direita
    if ((pos_vazio + DIREITA) % largura != 0):
        novo_estado = copy(no.estado)
        swap(novo_estado, pos_vazio, pos_vazio + DIREITA)

        novo_caminho = copy(no.caminho)
        novo_caminho.append(novo_estado)
        
        custo_busca += 1
        novo_no = No(novo_estado, no.custo_caminho + 1, custo_busca, novo_caminho)

        nos_expandidos.append(novo_no)

    return nos_expandidos


def busca_em_largura(estado_inicial, estado_final):
    no_inicial = No(estado_inicial, 0, 1, [estado_inicial])

    if (no_inicial.estado == estado_final):
        return no_inicial

    fila = Queue()
    fila.put(no_inicial)
    estados_percorridos = set()
    estados_percorridos.add(' '.join(no_inicial.estado))
    custo_busca = 1

    while not fila.empty():
        no_atual = fila.get()

        nos_expandidos = expande(no_atual, custo_busca)
        print(nos_expandidos)

        for no_expandido in nos_expandidos:
            custo_busca += 1

            print("Expansão:")
            print(f"Custo da busca: {no_expandido.custo_busca}")
            print(f"Custo da solução: {no_expandido.custo_caminho}")
            print(f"Caminho: {no_expandido.caminho}")

            if no_expandido.estado == estado_final:
                return no_expandido

            if ' '.join(no_expandido.estado) not in estados_percorridos:
                fila.put(no_expandido)
                estados_percorridos.add(' '.join(no_expandido.estado))

    return None


#LIXÃO:

'''
busca_em_largura(estado_inicial, estado_final):
    #constroi o no correspondente ao estado inicial
    no_inicial = no(estado_inicial, 0, 1, [estado_inicial])

    #verifica se o estado inicial é o estado final
    if (estado_inicial == estado_final):
        return no_inicial

    fila = fila()
    fila.push(no_inicial)
    set = {}
    set.add(no_inicial.estado)
    custo_busca = 1

    #enquanto a fila não estiver vazia
    while not fila.empty():
        no_atual = fila.pop()

        para todos os estados em expandir(no_atual, custo_busca):
            custo_busca += 1

            se o estado expandido for o estado final,
                retorne estado expandido
            
            se o estado não foi expandido antes,
                coloque o estado na fila
                coloque o estado no conjunto de já alcançados
    return false

expandir(no, custo_busca):
    pos_vazio = no.estado.find(' ')

    nos_expandidos = []
    
    #se for possível mover para cima,
    if (pos_vazio + CIMA >= 0):
        novo_estado = no.estado.swap(pos_vazio, pos_vazio + CIMA)
        
        novo_no = no(novo_estado, no.custo_caminho + 1, custo_busca, no.caminho + no.estado)

        nos_expandidos.append(novo_no)

    #se for possível mover para baixo
    if (pos_vazio + BAIXO < NUM_QUADROS):
        novo_estado = no.estado.swap(pos_vazio, pos_vazio + BAIXO)
        
        novo_no = no(novo_estado, no.custo_caminho + 1, custo_busca, no.caminho + no.estado)

        nos_expandidos.append(novo_no)

    #se for possível mover para a esquerda
    if ((pos_vazio + ESQUERDA) % largura != largura - 1):
        novo_estado = no.estado.swap(pos_vazio, pos_vazio + ESQUERDA)
        
        novo_no = no(novo_estado, no.custo_caminho + 1, custo_busca, no.caminho + no.estado)

        nos_expandidos.append(novo_no)
        
    #se for possível mover para a direita
    if ((pos_vazio + DIREITA) % largura != 0):
        novo_estado = no.estado.swap(pos_vazio, pos_vazio + DIREITA)
        
        novo_no = no(novo_estado, no.custo_caminho + 1, custo_busca, no.caminho + no.estado)

        nos_expandidos.append(novo_no)

    return nos_expandidos
'''