def particao(v, esq, dir):
    pivot = v[esq]
    i = esq
    j = dir+1
    while True:
        i += 1
        while v[i] < pivot:
            if i >= dir:
                break
            i += 1
        j -= 1
        while v[j] > pivot:

            if j <= esq:
                break
            j -= 1
        if i >= j:
            break
        print(v[i], v[j])
        v[i], v[j] = v[j], v[i]
    if v[esq] != v[j]:
        print(v[esq], v[j])
    v[esq], v[j] = v[j], v[esq]
    return j


def qs(v, esq, dir):
    if esq >= dir:
        return
    p = particao(v, esq, dir)
    qs(v, esq, p-1)
    qs(v, p+1, dir)


def quicksort(v):
    N = len(v) - 1
    qs(v, 0, N)


lista1 = [3234, 26435, 26459, 19288, 6089, 21378, 115,
          26860, 14362, 6695, 26292, 10251, 20579, 3403, 241]
lista2 = [5, 4, 7, 8, 1]
# quicksort(lista2)
# entrada = str(input())
# while entrada != "parar":
#     lista.append(int(entrada.split()[0]))
#     entrada = str(input())

quicksort(lista1)
print(lista1)
