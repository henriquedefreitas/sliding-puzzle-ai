import puzzle_ia as ia

#Desenhar imagem de exemplo

#Entrada do estado inicial

estado_inicial = input("Informe o estado inicial do jogo: ")
estado_inicial = estado_inicial.split()

#Entrada do estado final

estado_final = input("Informe o estado final do jogo: ")
estado_final = estado_final.split()

solucao = ia.busca_em_largura(estado_inicial, estado_final)

print(f"Custo da busca: {solucao.custo_busca}")
print(f"Custo da solução: {solucao.custo_caminho}")
print(f"Caminho: {solucao.caminho}")
