class Pokemon:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.start = None
        self.size = 0

    def append(self,element):
        if self.start:
            self.start.next = element
            element.prev = self.start
            self.start = element
        else:
            self.start = element
        self.size += 1

    def search(self,name_elemt):
        pointer = self.start
        if pointer.name == name_elemt:
            return pointer
        else:
            while pointer.name != name_elemt and pointer.prev != None:
                pointer = pointer.prev
                if pointer.name == name_elemt:
                    return pointer
    
    def remove(self,name_element):
        objeto = self.search(name_element)
        if objeto:
            if objeto.prev != None:
                objeto.prev.next = objeto.next
            else:
                objeto.next.prev = None

            if objeto.next != None:
                objeto.next.prev = objeto.prev
            else:
                objeto.prev.next = None
            self.size -= 1

    def print(self):
        pointer = self.start
        for i in range(self.size):
            print(pointer.name)
            pointer = pointer.prev