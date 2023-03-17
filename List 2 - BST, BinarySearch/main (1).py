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
    def pop(self):
        poppedItem = self.first
        self.first = self.first.next
        return poppedItem.value
        
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if not node:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)
        
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)
        if balance > 1:
            if value < node.left.value:
                node = self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                node = self.right_rotate(node)
        elif balance < -1:
            if value > node.right.value:
                node = self.left_rotate(node)
            else:
                node.right = self.right_rotate(node.right)
                node = self.left_rotate(node)
        return node

    def have_item(self, item):
        if not self.root:
            return False
        node = self.root
        while node:
            if node.value == item:
                return True
            elif item < node.value:
                node = node.left
            else:
                node = node.right
        return False

    def left_rotate(self, node):
        right_child = node.right
        node.right = right_child.left
        right_child.left = node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        right_child.height = 1 + max(self.get_height(right_child.left), self.get_height(right_child.right))
        return right_child

    def right_rotate(self, node):
        left_child = node.left
        node.left = left_child.right
        left_child.right = node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        left_child.height = 1 + max(self.get_height(left_child.left), self.get_height(left_child.right))
        return left_child

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)


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
            avl = BST()
        else:
            avl = None

        input_user = int(input())
        students_qnt = 0
        while input_user != '':
            if not find_caio_class or caio_class == avl :
                avl.insert(int(input_user))
                students_qnt += 1
            if int(input_user) == caio_regis:
                caio_class = avl
                find_caio_class = True
            input_user = input()


    try:
        input_user = input()
        while input_user != '':
            if caio_class.have_item(int(input_user)):
                caio_class_friends += 1
            input_user = input()
    except EOFError:
        pass
    print(caio_class_friends)

if __name__ == '__main__':
    main()