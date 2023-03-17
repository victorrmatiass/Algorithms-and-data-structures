class Node:
	def __init__(self, data) -> None:
		self.data = data
		self.left = None
		self.right = None
		self.height = 1

class AVLTree:

	def __init__(self) -> None:
		self.root = None

	def insert(self, key):
		self.root = self._insert(self.root, key)

	def _insert(self, root, key):
	
		if not root:
			return Node(key)
		elif key < root.data:
			root.left = self._insert(root.left, key)
		else:
			root.right = self._insert(root.right, key)

		root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

		b = self.get_balance(root)

		if b > 1 and key < root.left.data:
			return self.right_rotate(root)

		if b < -1 and key > root.right.data:
			return self.left_rotate(root)

		if b > 1 and key > root.left.data:
			root.left = self.left_rotate(root.left)
			return self.right_rotate(root)

		if b < -1 and key < root.right.data:
			root.right = self.right_rotate(root.right)
			return self.left_rotate(root)

		return root

	def left_rotate(self, z):

		y = z.right
		T2 = y.left

		y.left = z
		z.right = T2

		z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
		y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

		return y

	def right_rotate(self, z):

		y = z.left
		T3 = y.right

		y.right = z
		z.left = T3

		z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
		y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

		return y

	def get_height(self, root):
		if not root:
			return 0
		return root.height

	def get_balance(self, root):
		if not root:
			return 0
		return self.get_height(root.left) - self.get_height(root.right)

	def search(self, key):
		pointer = self.root
		while pointer is not None:
			if key == pointer.data:
				return True
			elif key < pointer.data:
				pointer = pointer.left
			else:
				pointer = pointer.right
		return False

def main():
	primeira_entrada = str(input())
	num_turmas = int(primeira_entrada[0])
	str(input())
	matricula_caio = int(primeira_entrada[2])

	qntd_amigos = 0
	turma_caio = False

	for i in range(num_turmas):
		if not turma_caio:
			turma = AVLTree()
			turma_descartada = 1
		else: turma_descartada = None

		matricula = input()
		while matricula != "":
			if not turma_caio or turma_descartada == 1:
				if int(matricula) == matricula_caio:
					turma_caio = True
				turma.insert(int(matricula))
			else:
				pass
			matricula = input()
		
	try:
		matricula = (input())
		while matricula != "":
			encontrou = turma.search(int(matricula))
			if encontrou:
				qntd_amigos += 1
			matricula = (input())
	except EOFError:
		pass		

	print(qntd_amigos)
				
if __name__ == "__main__":
	main()