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


def calcula_pontos_regra_simples(lista):
    dicionario = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    quant_1 = 0
    quant_2 = 0
    quant_3 = 0
    quant_4 = 0
    quant_5 = 0
    quant_6 = 0
    for elemento in lista:
        if elemento == 1:
            quant_1 += 1
            dicionario[1] = quant_1
        elif elemento == 2:
            quant_2 += 1
            dicionario[2] = quant_2*2
        elif elemento == 3:
            quant_3 += 1
            dicionario[3] = quant_3*3
        elif elemento == 4:
            quant_4 += 1
            dicionario[4] = quant_4*4
        elif elemento == 5:
            quant_5 += 1
            dicionario[5] = quant_5*5
        elif elemento == 6:
            quant_6 += 1
            dicionario[6] = quant_6*6
    return dicionario

def calcula_pontos_soma (lista):
    soma = 0 
    for elemento in lista:
        soma += elemento 
    return soma

def calcula_pontos_sequencia_baixa(lista):
    if (1 in lista and 2 in lista and 3 in lista and 4 in lista):
        return 15
    elif (2 in lista and 3 in lista and 4 in lista and 5 in lista):
        return 15
    elif (3 in lista and 4 in lista and 5 in lista and 6 in lista):
        return 15
    else:
        return 0

def calcula_pontos_sequencia_alta (lista):
    if (1 in lista and 2 in lista and 3 in lista and 4 in lista and 5 in lista):
        return 30 
    elif (2 in lista and 3 in lista and 4 in lista and 5 in lista and 6 in lista):
        return 30 
    else:
        return 0
    
def calcula_pontos_full_house(valores):

    contador1 = 0
    contador2 = 0

    soma = 0

    numero1 = valores[0]
    numero2 = numero1

    for n in valores:
        if n != numero1:
            numero2 = n
            break
    
    if numero2 == numero1:
        return 0

    for n in valores:
        if n == numero1:
            contador1 += 1
            soma += n
        elif n == numero2:
            contador2 += 1
            soma += n
        else:
            return 0

        if contador1 == 3 and contador2 == 2:
            return soma
        if contador1 == 2 and contador2 == 3:
            return soma
     
    return 0   
