class AVLTree:

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            self.height = 1

    def __init__(self):
        self.root = None

    def getHeight(self, node):
        return node.height if node else 0

    def getBalance(self, node):
        return self.getHeight(node.left) - self.getHeight(node.right) if node else 0

    def updateHeight(self, node):
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.updateHeight(y)
        self.updateHeight(x)

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.updateHeight(x)
        self.updateHeight(y)

        return y

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if not node:
            return self.Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            return node

        self.updateHeight(node)
        balance = self.getBalance(node)

        if balance > 1 and value < node.left.value:
            return self.rotate_right(node)

        if balance < -1 and value > node.right.value:
            return self.rotate_left(node)

        if balance > 1 and value > node.left.value:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1 and value < node.right.value:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if not node:
            return node

        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = self._minValueNode(node.right)
            node.value = temp.value
            node.right = self._delete(node.right, temp.value)

        self.updateHeight(node)
        balance = self.getBalance(node)

        if balance > 1 and self.getBalance(node.left) >= 0:
            return self.rotate_right(node)

        if balance > 1 and self.getBalance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1 and self.getBalance(node.right) <= 0:
            return self.rotate_left(node)

        if balance < -1 and self.getBalance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def _minValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        if not node:
            return []
        return self._inorder(node.left) + [node.value] + self._inorder(node.right)
    

#CASOS DE PRUEBA 

if __name__ == "__main__":
    avl = AVLTree()

    print("caso 1: Rotación RR")
    valores = [10, 20, 30]
    for v in valores:
        avl.insert(v)
    print("Inorden:", avl.inorder())
    print()

    avl = AVLTree()
    print("caso 2: Rotación LL")
    valores = [30, 20, 10]
    for v in valores:
        avl.insert(v)
    print("Inorden:", avl.inorder())
    print()

    avl = AVLTree()
    print("Caso 3: Rotación LR")
    valores = [30, 10, 20]
    for v in valores:
        avl.insert(v)
    print("Inorden:", avl.inorder())
    print()

    avl = AVLTree()
    print("Caso 4: Rotación RL")
    valores = [10, 30, 20]
    for v in valores:
        avl.insert(v)
    print("Inorden:", avl.inorder())
    print()

    avl = AVLTree()
    print("Caso5: Eliminación")
    valores = [10, 20, 30, 40, 50, 25]
    for v in valores:
        avl.insert(v)

    print("Antes de eliminar:", avl.inorder())
    avl.delete(50)
    print("Después de eliminar 50:", avl.inorder())
