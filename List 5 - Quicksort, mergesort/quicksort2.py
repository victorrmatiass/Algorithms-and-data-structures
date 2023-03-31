def quicksort(arr, start, end):
    if start < end:
        # Particiona o array e retorna a posição do pivô
        pivot_index = partition(arr, start, end)

        # Aplica o quicksort recursivamente nas duas partes do array
        quicksort(arr, start, pivot_index-1)
        quicksort(arr, pivot_index+1, end)


def partition(arr, start, end):
    # Escolhe o primeiro elemento como pivô
    pivot = arr[start]

    # Define os índices para os elementos maiores e menores que o pivô
    i = start + 1
    j = end

    while i <= j:
        # Encontra o primeiro elemento maior que o pivô
        while i <= j and arr[i] <= pivot:
            i += 1

        # Encontra o último elemento menor que o pivô
        while i <= j and arr[j] > pivot:
            j -= 1

        if i < j:
            # Troca os elementos i e j
            print(arr[i], arr[j])
            arr[i], arr[j] = arr[j], arr[i]

    # Troca o pivô com o último elemento menor que ele
    if arr[start] != arr[j]:
        print(arr[start], arr[j])
    arr[start], arr[j] = arr[j], arr[start]

    return j


lista1 = [3234, 26435, 26459, 19288, 6089, 21378, 115,
          26860, 14362, 6695, 26292, 10251, 20579, 3403, 241]
lista2 = [5, 4, 7, 8, 1]

quicksort(lista1, 0, 14)
