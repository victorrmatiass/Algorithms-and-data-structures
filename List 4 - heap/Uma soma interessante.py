def sum_with_cost(numbers):
    heap = numbers[:]
    heap.sort()
    cost = 0

    while len(heap) > 1:
        smallest1 = heap.pop(0)
        smallest2 = heap.pop(0)
        sum_cost = smallest1 + smallest2
        cost += sum_cost
        i = 0
        while i < len(heap) and heap[i] < sum_cost:
            i += 1
        heap.insert(i, sum_cost)

    return cost


def main():
    while True:
        n = int(input())
        if n == 0:
            break
        numbers = list(map(int, input().split()))
        print(sum_with_cost(numbers))


if __name__ == '__main__':
    main()
