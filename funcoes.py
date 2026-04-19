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


