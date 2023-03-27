def quicksort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)-1
    if inicio < fim:
        p = partition(lista, inicio, fim)
        # recursivamente na sublista à esquerda (menores)
        quicksort(lista, inicio, p-1)
        # recursivamente na sublista à direita (maiores)
        quicksort(lista, p+1, fim)


def partition2(lista, inicio, fim):
    pivot = lista[inicio]
    ultimoMenor = fim
    for j in range(fim, inicio, -1):
        if lista[j] > pivot:
            lista[j], lista[ultimoMenor] = lista[ultimoMenor], lista[j]
        ultimoMenor = j
    lista[inicio], lista[ultimoMenor] = lista[ultimoMenor], lista[inicio]
    return ultimoMenor


def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        # j sempre avança, pois representa o elementa em análise
        # e delimita os elementos maiores que o pivô
        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]
            # incrementa-se o limite dos elementos menores que o pivô
            i = i + 1
    lista[i], lista[fim] = lista[fim], lista[i]
    print(lista[fim], lista[i])
    return i


lista = []
# lista2 = [5, 4, 7, 8, 1]
# quicksort(lista2)
entrada = str(input())
while entrada != "parar":
    lista.append(int(entrada.split()[0]))
    entrada = str(input())

lista.reverse()
quicksort(lista)
