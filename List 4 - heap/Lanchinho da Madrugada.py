def distancia(coord):
    return (coord[0] ** 2 + coord[1] ** 2)**0.5


def main():
    n = int(input())
    m = int(input())
    restaurantes = []
    for i in range(m):
        x, y = map(int, input().split())
        restaurantes.append((x, y))

    restaurantes_ordenados = sorted(restaurantes, key=distancia)

    for i in range(n-1, -1, -1):
        print("{}, {}".format(
            restaurantes_ordenados[i][0], restaurantes_ordenados[i][1]))


if __name__ == "__main__":
    main()
