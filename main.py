import os
import puzzle_ia as ia


if os.name == 'nt':
    clear_screen = 'cls'
else:
    clear_screen = 'clear'

#Limpa o terminal
os.system(clear_screen)


#Instruções
print("\n-----------------INSTRUÇÕES-----------------\n")

print("Informe a configuração inicial e final do jogo indicando a sequência de\nnúmeros na ordem da esquerda para a direita e de cima para baixo,\nutilizando o caracter X para representar o espaço em branco.")
print('\n---------------------------------------------')
print("\nExemplo:")
ia.imprime_estado([1,2,3,4,'X',5,6,7,8])
print('\nA configuração acima é representada pela seguinte entrada: 1 2 3 4 X 5 6 7 8')


#Entradas
print("\n\n-----------------ENTRADA--------------------")

estado_inicial = input("\nInforme o estado inicial do jogo: ")
estado_inicial = estado_inicial.split()
pos_vazio = estado_inicial.index('X')
estado_inicial[pos_vazio] = ' '

estado_final = input("\nInforme o estado final do jogo: ")
estado_final = estado_final.split()
pos_vazio = estado_final.index('X')
estado_final[pos_vazio] = ' '


#Solução
solucao = ia.busca_em_largura(estado_inicial, estado_final)


#Resultados
print("\n\n-----------------SOLUÇÃO--------------------")

print(f"\nCusto da busca: foram percorridos {solucao.custo_busca} estado(s)")
print(f"\nCusto da solução: a solução encontrada exige {solucao.custo_caminho} movimento(s)")


input('\n\nPressione ENTER para ver o passo a passo\n')
os.system(clear_screen)

cont = 1
for estado in solucao.caminho:
    print(f'\nEstado {cont}')
    ia.imprime_estado(estado)
    input('\n\nPressione ENTER para avançar\n')
    os.system(clear_screen)

    cont += 1

print('\nFIM!')
ia.imprime_estado(estado)

input('\n\nPressione ENTER para sair\n')
os.system(clear_screen)
