def mergesort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if (fim - inicio > 1):
        meio = (fim + inicio)//2
        mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)
        merge(lista, inicio, meio, fim)


def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0
    for k in range(inicio, fim):
        if top_left >= len(left):
            lista[k] = right[top_right]
            top_right = top_right + 1
        elif top_right >= len(right):
            lista[k] = left[top_left]
            top_left = top_left + 1
        elif left[top_left] < right[top_right]:
            lista[k] = left[top_left]
            top_left = top_left + 1
        else:
            lista[k] = right[top_right]
            top_right = top_right + 1


def main():
    lista = [1]
    # while True:
    #     try:
    #         entrada = str(input())
    #     except:
    #         break
    #     else:
    #         number = ""
    #         for i in range(len(entrada)):
    #             if entrada[i] != " ":
    #                 number = number + entrada[i]
    #             if i < len(entrada)-1:
    #                 if entrada[i+1] == " " and entrada[i] != " ":
    #                     lista.append(int(number))
    #                     number = ''
    #             else:
    #                 if number != '':
    #                     lista.append(int(number))
    #                     number = ''

    mergesort(lista)
    print(*lista, end='')


if __name__ == '__main__':
    main()
