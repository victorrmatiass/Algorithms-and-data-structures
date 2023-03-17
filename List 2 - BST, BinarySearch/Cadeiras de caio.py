teste = "3 0"
print(len(teste))

def search(self, key):
    pointer = self.head
    while pointer != None:
        if pointer.data == key:
            return True
        else:
            pointer = pointer.anterior
    return False