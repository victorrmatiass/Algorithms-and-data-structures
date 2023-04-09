impressao = []

def particao(v, esq, dir):
    pivot = v[esq]
    i = esq
    j = dir+1
    while True:
        i += 1
        while v[i] < pivot:
            if i >= dir: break
            i += 1
        j -= 1
        while v[j] > pivot:

            if j <= esq:
                break
            j -= 1
        if i >= j:
            break
        impressao.append([v[i], v[j]])
        v[i], v[j] = v[j], v[i]
    if v[esq] != v[j]:
        impressao.append([v[esq], v[j]])
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


primeiro_print = False


def main():

    lista = []
    while True:
        try:
            entrada = str(input())
            lista.append(int(entrada.split()[0]))
        except EOFError:
            break
    quicksort(lista)
    for x in range(len(impressao)):
        if x == len(impressao)-1:
            print(impressao[x][0], impressao[x][1], end='')
            continue
        print(impressao[x][0], impressao[x][1])


if __name__ == '__main__':
    main()
