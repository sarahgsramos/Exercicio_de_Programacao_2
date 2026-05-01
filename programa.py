from funcoes import *

cartela = {
    "regra_simples": {1:-1, 2:-1, 3:-1, 4:-1, 5:-1, 6:-1},
    "regra_avancada": {
        "sem_combinacao": -1,
        "quadra": -1,
        "full_house": -1,
        "sequencia_baixa": -1,
        "sequencia_alta": -1,
        "cinco_iguais": -1
    }
}

imprime_cartela(cartela)

for rodada in range(12):

    dados_rolados = rolar_dados(5)
    dados_guardados = []
    rerrolagens = 0

    while True:

        print(f'Dados rolados: {dados_rolados}')
        print(f'Dados guardados: {dados_guardados}')
        print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
        
        while True:
            opcao = input(">")
            if opcao not in ('0','1','2','3','4'):
                print("Opção inválida. Tente novamente.")
                continue
            break

        if opcao == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input(">"))

            if 0 <= indice < len(dados_rolados):
                dados_rolados, dados_guardados = guardar_dado(dados_rolados, dados_guardados, indice)


        elif opcao == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input(">"))

            if 0 <= indice < len(dados_guardados):
                dados_rolados, dados_guardados = remover_dado(dados_rolados, dados_guardados, indice)


        elif opcao == "3":
            if rerrolagens == 2:
                print("Você já usou todas as rerrolagens.")
                continue
            else:
                dados_rolados = rolar_dados(len(dados_rolados))
                rerrolagens += 1
                continue

        elif opcao == "4":
            imprime_cartela(cartela)
            continue

        elif opcao == "0":
            print("Digite a combinação desejada:")

            while True:
                combinacao = input(">")

                if combinacao in ["1","2","3","4","5","6"]:
                    numero = int(combinacao)

                    if cartela["regra_simples"][numero] != -1:
                        print("Essa combinação já foi utilizada.")
                        continue

                    break

                elif combinacao in cartela["regra_avancada"]:

                    if cartela["regra_avancada"][combinacao] != -1:
                        print("Essa combinação já foi utilizada.")
                        continue

                    break

                else:
                    print("Combinação inválida. Tente novamente.")
                    continue

            todos_dados = dados_guardados + dados_rolados
            cartela = faz_jogada(todos_dados, combinacao, cartela)

            break

imprime_cartela(cartela)

total = 0

soma_simples = 0
for valor in cartela["regra_simples"].values():
    if valor != -1:
        soma_simples += valor
total += soma_simples

if soma_simples >= 63:
    total += 35
    
for valor in cartela["regra_avancada"].values():
    if valor != -1:
        total += valor

print(f"Pontuação total: {total}")