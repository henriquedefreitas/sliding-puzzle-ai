import os
import puzzle_ia as ia


#Verifica qual é o sistema operacional
if os.name == 'nt':
    clear_screen = 'cls'
else:
    clear_screen = 'clear'


#Limpa o terminal
os.system(clear_screen)


#Instruções iniciais
print("\n------------------INSTRUÇÕES------------------\n")
print("Informe a configuração inicial e final do jogo\nindicando a sequência de números na ordem da\nesquerda para a direita e de cima para baixo,\nutilizando o caracter X para representar o\nespaço em branco.")
print('\n---------------------------------------------')

input('\nPressione ENTER para ver um exemplo\n')
os.system(clear_screen)


#Exemplo
print("\n-------------------EXEMPLO-------------------\n")

ia.imprime_estado([1,2,3,4,' ',5,6,7,8])

print('\nEntrada: 1 2 3 4 X 5 6 7 8')
print('\n---------------------------------------------')

input('\nPressione ENTER para começar\n')
os.system(clear_screen)


#Entrada dos dados
print("\n-----------------ENTRADA--------------------")
print("\nInforme o número correspondente ao tipo de\nbusca que deseja fazer: ")
print("\n1 - Busca em largura")
print("2 - Busca em profundidade")
tipo_busca = input("\nEscolha: ") #1 = largura, 2 = profundidade

#Valida entrada
while tipo_busca != '1' and tipo_busca != '2':
    os.system(clear_screen)

    print("\n-----------------ENTRADA--------------------")
    print("\nValor inválido, tente novamente.")
    print("\nInforme o número correspondente ao tipo de\nbusca que deseja fazer: ")
    print("\n1 - Busca em largura")
    print("2 - Busca em profundidade")
    tipo_busca = input("\nEscolha: ") #1 = largura, 2 = profundidade

os.system(clear_screen)

print("\n-----------------ENTRADA--------------------")
estado_inicial = input("\nInforme o estado inicial do jogo: ")
estado_inicial = estado_inicial.split()

#Valida entrada
while len(estado_inicial) != 9 or 'X' not in estado_inicial or ' ' in estado_inicial:
    os.system(clear_screen)

    print("\n-----------------ENTRADA--------------------")
    print("\nEntrada inválida, tente novamente.")
    estado_inicial = input("\nInforme o estado inicial do jogo: ")
    estado_inicial = estado_inicial.split()

#Troca o X por um espaço
pos_vazio = estado_inicial.index('X')
estado_inicial[pos_vazio] = ' '

os.system(clear_screen)

print("\n-----------------ENTRADA--------------------")
estado_final = input("\nInforme o estado final do jogo: ")
estado_final = estado_final.split()

#Valida entrada
while len(estado_final) != 9 or 'X' not in estado_final or ' ' in estado_final:
    os.system(clear_screen)

    print("\n-----------------ENTRADA--------------------")
    print("\nEntrada inválida, tente novamente.")
    estado_final = input("\nInforme o estado final do jogo: ")
    estado_final = estado_final.split()

#Troca o X por um espaço
pos_vazio = estado_final.index('X')
estado_final[pos_vazio] = ' '

print("\nEncontrando solução...")


#Solução
if tipo_busca == '1':
    solucao = ia.busca_em_largura(estado_inicial, estado_final)
else:
    solucao = ia.busca_em_profundidade(estado_inicial, estado_final)
os.system(clear_screen)


#Resultados
print("\n-----------------SOLUÇÃO--------------------")

if solucao == None:
    print('\nNão foi encontrada uma solução para essa configuração!\n\nVerifique os valores de entrada e tente novamente.')
else:
    print(f"\nCusto da busca: foram percorridos {solucao.custo_busca} estado(s)")
    print(f"\nCusto da solução: a solução encontrada exige {solucao.custo_caminho} movimento(s)")
    print('\n---------------------------------------------')
    input('\nPressione ENTER para ver o passo a passo\n')
    

#Passo a passo para resolver (caminho)
    os.system(clear_screen)

    cont = 1
    for estado in solucao.caminho:
        print(f"\n-----------------ESTADO {cont}------------------\n")
        ia.imprime_estado(estado)
        print('\n---------------------------------------------')
        input('\nPressione ENTER para avançar\n')
        os.system(clear_screen)

        cont += 1

    print("\n-------------------FIM!---------------------\n")
    ia.imprime_estado(estado)

print('\n---------------------------------------------')
input('\nPressione ENTER para sair\n')
os.system(clear_screen)
exit()
