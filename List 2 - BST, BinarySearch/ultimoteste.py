def main():
    primeira_entrada = input().split()
    n_turmas = int(primeira_entrada[0])
    caio_matricula = int(primeira_entrada[1])
    input()

    qntd_amigos = 0
    turmas_caio = []

    for i in range(n_turmas):
        turma = []
        while True:
            entrada = input()
            if entrada == "": break
            else:
                turma.append(int(entrada))
        if caio_matricula in turma:
            turmas_caio.append(turma)

    while True:
        try:
            matricula = int(input())
            encontrou = False
        except:
            break
        else:
            for lista in turmas_caio:
                if matricula in lista: encontrou = True
            if encontrou: qntd_amigos += 1

    print(qntd_amigos)

if __name__ == "__main__":
    main()