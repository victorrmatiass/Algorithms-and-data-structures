class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    def __init__(self) -> None:
        self.root = None
        self.result = ""

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):

        if not root:
            return Node(key)
        elif key < root.data:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

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

    def pre_order_search(self):
        self._pre_order_search(self.root)

    def post_order_search(self):
        self._post_order_search(self.root)

    def in_order_search(self):
        self._in_order_search(self.root)

    def _pre_order_search(self, node):
        if node is not None:
            self.result += " " + str(node.data)
            self._pre_order_search(node.left)
            self._pre_order_search(node.right)

    def _post_order_search(self, node):
        if node is not None:
            self._post_order_search(node.left)
            self._post_order_search(node.right)
            self.result += " " + str(node.data)

    def _in_order_search(self, node):
        if node is not None:
            self._in_order_search(node.left)
            self.result += " " + str(node.data)
            self._in_order_search(node.right)


def main():
    avlTree = AVLTree()

    while True:
        try:
            user_input = int(input())
        except EOFError:
            break
        else:
            avlTree.insert(user_input)

    avlTree.pre_order_search()
    print("preOrdem:",avlTree.result[1:])
    avlTree.result = ""

    avlTree.in_order_search()
    print("inOrdem:",avlTree.result[1:])
    avlTree.result = ""

    avlTree.post_order_search()
    print("posOrdem:",avlTree.result[1:])

if __name__ == "__main__":
    main()