class Node:
	def __init__(self, data) -> None:
		self.data = data
		self.left = None
		self.right = None
		self.height = 1

class BSTree:

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

		return root

	def get_height(self, root):
		if not root:
			return 0
		return root.height
		
def main():

	bst = BSTree()

	while True:
		try:
			number = input()
		except EOFError:
			break
		else:
			bst.insert(number)
			height = bst.get_height(bst.root)
			print(height)

if __name__ == "__main__":
	main()

def teste():
	bst = BSTree()
	lista = [0,2,1,6,4,5,3]
	lista2 = []
	for i in lista:
		bst.insert(i)
		height = bst.get_height(bst.root)
		lista2.append(height)
	print(lista2)


