class Item:
    def __init__(self, value) -> None:
        self.next = None
        self.value = value

class List:
    def __init__(self) -> None:
        self.first = None
    def push(self, value):
        if not self.first:
            self.first = Item(value)
            return
        newItem = Item(value)
        newItem.next = self.first
        self.first = newItem
    
    def find(self, value):
        if not self.first:
            return False
        element = self.first
        while element:
            if element.value == value:
                return True
            element = element.next
        return False
        
        

def main():
    class_and_regis = input().split(' ')
    input()
    class_qnt = int(class_and_regis[0])
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