from random import randint
def rolar_dados(n):
    dados = []
    i = 0
    while i < n:
        sorteio = randint(1,6)
        dados.append(sorteio)
        i += 1
    return dados

def guardar_dado (lista_dados_rolados, lista_dados_ja_guardados, indice):
    valor = lista_dados_rolados[indice]
    nova_lista = []
    for i in range(len(lista_dados_rolados)):
        if i != indice:
            dado = lista_dados_rolados[i]
            nova_lista.append(dado)
    lista_dados_ja_guardados.append(valor)
    saida = [nova_lista, lista_dados_ja_guardados]
    return saida

def remover_dado(dados_rolados,dados_no_estoque,dado_para_remover):
    rolados = dados_rolados
    armazenados = []

    rolados.append(dados_no_estoque[dado_para_remover])


    for i in range(len(dados_no_estoque)):
        numero = dados_no_estoque[i]
        if i != dado_para_remover:
            armazenados.append(numero)
    
    lista_final = [rolados,armazenados]
    return lista_final



