from copy import copy
from queue import Queue


class No:
    def __init__(self, estado, custo_caminho, custo_busca, caminho):
        self.estado = estado
        self.custo_caminho = custo_caminho
        self.custo_busca = custo_busca
        self.caminho = copy(caminho)


#Troca os valores de 2 posições em uma lista
def swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

#Aplica as ações possíveis ao no, gerando até 4 filhos
def expande(no):
    pos_vazio = no.estado.index(' ')

    #TODO: generalizar
    comprimento = 3
    altura = 3

    tamanho_puzzle = comprimento * altura

    CIMA = -comprimento
    BAIXO = comprimento
    ESQUERDA = -1
    DIREITA = 1

    nos_expandidos = []

    #Move pra cima, se possível
    if (pos_vazio + CIMA >= 0):
        novo_estado = copy(no.estado)
        swap(novo_estado, pos_vazio, pos_vazio + CIMA)

        novo_caminho = copy(no.caminho)
        novo_caminho.append(novo_estado)
        
        novo_no = No(novo_estado, no.custo_caminho + 1, -1, novo_caminho)

        nos_expandidos.append(novo_no)

    #Move pra direita, se possível
    if ((pos_vazio + DIREITA) % comprimento != 0):
        novo_estado = copy(no.estado)
        swap(novo_estado, pos_vazio, pos_vazio + DIREITA)

        novo_caminho = copy(no.caminho)
        novo_caminho.append(novo_estado)
        
        novo_no = No(novo_estado, no.custo_caminho + 1, -1, novo_caminho)

        nos_expandidos.append(novo_no)

    #Move pra baixo, se possível
    if (pos_vazio + BAIXO < tamanho_puzzle):
        novo_estado = copy(no.estado)
        swap(novo_estado, pos_vazio, pos_vazio + BAIXO)

        novo_caminho = copy(no.caminho)
        novo_caminho.append(novo_estado)
        
        novo_no = No(novo_estado, no.custo_caminho + 1, -1, novo_caminho)

        nos_expandidos.append(novo_no)

    #Move pra esquerda, se possível
    if ((pos_vazio + ESQUERDA) % comprimento != comprimento - 1):
        novo_estado = copy(no.estado)
        swap(novo_estado, pos_vazio, pos_vazio + ESQUERDA)

        novo_caminho = copy(no.caminho)
        novo_caminho.append(novo_estado)
        
        novo_no = No(novo_estado, no.custo_caminho + 1, -1, novo_caminho)

        nos_expandidos.append(novo_no)

    return nos_expandidos


def busca_em_comprimento(estado_inicial, estado_final):
    no_inicial = No(estado_inicial, 0, 1, [estado_inicial])

    if (no_inicial.estado == estado_final):
        return no_inicial

    fila = Queue()
    fila.put(no_inicial)
    estados_percorridos = set()
    estados_percorridos.add(''.join(no_inicial.estado))
    custo_busca = 1

    while not fila.empty():
        no_atual = fila.get()

        for no_expandido in expande(no_atual):
            custo_busca += 1

            if no_expandido.estado == estado_final:
                no_expandido.custo_busca = custo_busca
                return no_expandido

            if ''.join(no_expandido.estado) not in estados_percorridos:
                fila.put(no_expandido)
                estados_percorridos.add(''.join(no_expandido.estado))

    return None

#Versão iterativa
def busca_em_profundidade(estado_inicial, estado_final):
    pilha = []
    pilha.append([estado_inicial, 0]) #[estado, nivel]

    custo_busca = 0
    caminho = []
    alcancados = set()
    solucionado = False
    nivel = -1

    while len(pilha) != 0:
        topo = pilha.pop()
        estado_atual = topo[0]

        nivel_anterior = nivel
        nivel = topo[1]

        if nivel < nivel_anterior:
            caminho.pop()

        if ''.join(estado_atual) not in alcancados:
            custo_busca += 1
            caminho.append(estado_atual)

            if estado_atual == estado_final:
                solucionado = True
                break

            alcancados.add(''.join(estado_atual))
            pos_vazio = estado_atual.index(' ')
            comprimento = 3
            altura = 3
            tamanho_puzzle = comprimento * altura
            CIMA = -comprimento
            BAIXO = comprimento
            ESQUERDA = -1
            DIREITA = 1
            nivel_novo = nivel + 1

            #Move pra esquerda, se possível
            if ((pos_vazio + ESQUERDA) % comprimento != comprimento - 1):
                novo_estado = copy(estado_atual)
                swap(novo_estado, pos_vazio, pos_vazio + ESQUERDA)
                pilha.append([novo_estado, nivel_novo])

            #Move pra baixo, se possível
            if (pos_vazio + BAIXO < tamanho_puzzle):
                novo_estado = copy(estado_atual)
                swap(novo_estado, pos_vazio, pos_vazio + BAIXO)
                pilha.append([novo_estado, nivel_novo])

            #Move pra direita, se possível
            if ((pos_vazio + DIREITA) % comprimento != 0):
                novo_estado = copy(estado_atual)
                swap(novo_estado, pos_vazio, pos_vazio + DIREITA)
                pilha.append([novo_estado, nivel_novo])

            #Move pra cima, se possível
            if (pos_vazio + CIMA >= 0):
                novo_estado = copy(estado_atual)
                swap(novo_estado, pos_vazio, pos_vazio + CIMA)
                pilha.append([novo_estado, nivel_novo])

    if solucionado:
        return No(caminho[-1], len(caminho) - 1, custo_busca, caminho)
    else:
        return None


def imprime_estado(estado):
    print('        -------------------------')
    print('        |       |       |       |')
    print(f'        |   {estado[0]}   |   {estado[1]}   |   {estado[2]}   |')
    print('        |       |       |       |')
    print('        -------------------------')
    print('        |       |       |       |')
    print(f'        |   {estado[3]}   |   {estado[4]}   |   {estado[5]}   |')
    print('        |       |       |       |')
    print('        -------------------------')
    print('        |       |       |       |')
    print(f'        |   {estado[6]}   |   {estado[7]}   |   {estado[8]}   |')
    print('        |       |       |       |')
    print('        -------------------------')


#Versão recursiva
'''
def profundidade(estado):
    #Ve se encontrou o estado final
    if (estado == estado_final):
        caminho = []
        caminho.append(estado)

        global custo_busca
        custo_busca = len(alcancados)

        return caminho
    
    #Vê se o estado já foi alcançado antes
    if ''.join(estado) in alcancados:
        return None

    alcancados.add(''.join(estado))

    #setup
    pos_vazio = estado.index(' ')
    CIMA = -3
    BAIXO = 3
    ESQUERDA = -1
    DIREITA = 1
    tamanho_puzzle = 9
    comprimento = 3

    #Move pra cima, se possível
    if (pos_vazio + CIMA >= 0):
        novo_estado = copy(estado)
        swap(novo_estado, pos_vazio, pos_vazio + CIMA)
        caminho = profundidade(novo_estado)
        if caminho != None:
            caminho.insert(0, estado)
            return caminho

    #Move pra direita, se possível
    if ((pos_vazio + DIREITA) % comprimento != 0):
        novo_estado = copy(estado)
        swap(novo_estado, pos_vazio, pos_vazio + DIREITA)
        caminho = profundidade(novo_estado)
        if caminho != None:
            caminho.insert(0, estado)
            return caminho

    #Move pra baixo, se possível
    if (pos_vazio + BAIXO < tamanho_puzzle):
        novo_estado = copy(estado)
        swap(novo_estado, pos_vazio, pos_vazio + BAIXO)
        caminho = profundidade(novo_estado)
        if caminho != None:
            caminho.insert(0, estado)
            return caminho

    #Move pra esquerda, se possível
    if ((pos_vazio + ESQUERDA) % comprimento != comprimento - 1):
        novo_estado = copy(estado)
        swap(novo_estado, pos_vazio, pos_vazio + ESQUERDA)
        caminho = profundidade(novo_estado)
        if caminho != None:
            caminho.insert(0, estado)
            return caminho

    return None
    

def busca_em_profundidade(estado_inicial_, estado_final_):
    global estado_inicial
    estado_inicial = estado_inicial_
    
    global estado_final
    estado_inicial = estado_inicial_

    caminho = profundidade(estado_inicial_)

    if caminho != None:
        no = No(caminho[-1], len(caminho) - 1, custo_busca, caminho)

        return no
    else:
        return None
'''