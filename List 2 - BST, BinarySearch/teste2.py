class NodeList:
	def __init__(self, data) -> None:
		self.data = data
		self.anterior = None

class LinkedList:
	def __init__(self) -> None:
		self.head = None

	def insert(self, key):
		if not self.head:
			self.head = NodeList(key)
			return

		node = NodeList(key)
		node.anterior = self.head
		self.head = node

	def search(self, key):
		pointer = self.head
		while pointer != None:
			if pointer.data == key:
				return True
			else:
				pointer = pointer.anterior
		return False

def main():
	primeira_entrada = str(input())
	num_turmas = int(primeira_entrada[0])
	matricula_caio = int(primeira_entrada[2])
	str(input())

	qntd_amigos = 0
	caio_class = None
	find_caio_class = False

	for i in range(num_turmas):
		if not find_caio_class:
			current_class = LinkedList()
		else:
			current_class = None

		input_user = int(input())
		while input_user != '':
			if not find_caio_class or caio_class == current_class:
				current_class.insert(int(input_user))
			if int(input_user) == matricula_caio:
				caio_class = current_class
				find_caio_class = True
			input_user = input()
		
	try:
		input_user = input()
		while input_user != '':
			if caio_class.search(int(input_user)):
				qntd_amigos += 1
			input_user = input()
	except EOFError:
		pass

	print(qntd_amigos)
				
if __name__ == "__main__":
	main()