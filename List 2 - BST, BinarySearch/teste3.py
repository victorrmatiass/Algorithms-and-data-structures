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
    entrada = input().split(' ')
    input()
    class_qnt = int(entrada[0])
    caio_regis = int(class_and_regis[1])

    caio_class = None
    caio_class_friends = 0
    find_caio_class = False
    for i in range(class_qnt):
        if not find_caio_class:
            current_class = List()
        else:
            current_class = None

        input_user = int(input())
        while input_user != '':
            if not find_caio_class or caio_class == current_class:
                current_class.push(int(input_user))
            if int(input_user) == caio_regis:
                caio_class = current_class
                find_caio_class = True
            input_user = input()


    try:
        input_user = input()
        while input_user != '':
            if caio_class.find(int(input_user)):
                caio_class_friends += 1
            input_user = input()
    except EOFError:
        pass
    print(caio_class_friends)

if __name__ == '__main__':
    main()