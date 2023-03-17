def buscabinaria(lista, chave):
	meio = len(lista) // 2
	if len(lista) == 0:
		return False
	if chave == lista[meio]:
		return True
	elif chave > lista[meio]:
		return buscabinaria(lista[meio+1:], chave)
	else:
		return buscabinaria(lista[:meio], chave)

def main():
	primeira_entrada = input().split()
	n_turmas = int(primeira_entrada[0])
	caio_matricula = int(primeira_entrada[1])
	input()

	turma_caio = []
	encontrou_caio = False

	for i in range(n_turmas):
		turma = []
		matricula = input()
		while matricula != "":
			if int(matricula) == caio_matricula:
				encontrou_caio = True
			turma.append(int(matricula))
			matricula = input()

		if encontrou_caio:
			turma_caio.append(turma)
			encontrou_caio = False

	qntd_amigos = 0

	'''
	try:
		matricula_amigo = 0
		while matricula_amigo != "":
			matricula_amigo = input()
			amigo = 0
			for i in range(len(turma_caio)):
				encontrou = buscabinaria(turma_caio[i], int(matricula_amigo))
				if encontrou: amigo = 1
			if amigo == 1: qntd_amigos += 1 
	except EOFError:
		pass
	'''
	
	while True:
		try:
			matricula_amigo = int((input()))
		except:
			break
		else:
			amigo = 0
			for i in range(len(turma_caio)):
				encontrou = buscabinaria(turma_caio[i], int(matricula_amigo))
				if encontrou: amigo = 1
			if amigo == 1: qntd_amigos += 1 

	print(qntd_amigos)

if __name__ == "__main__":
	main()