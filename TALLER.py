import sys 

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1 


def getHeight(node):
    if not node:
        return 0
    return node.height

def getBalance(node):
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)

def updateHeight(node):
    if node:
        node.height = 1 + max(getHeight(node.left), getHeight(node.right))

def rotate_right(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    updateHeight(y)
    updateHeight(x)

    return x

def rotate_left(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    updateHeight(x)
    updateHeight(y)

    return y

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if not node:
            return Node(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        else:
            return node 
        
        updateHeight(node)

    def inorden(self, root):
        if root is None:
            return
        print(root.value)
        self.inorder(root.left)
        self.inorder(root.right)
    
    def eliminarnodo(self, node, value):
        if not node:
            return node
        if value < node.value:
            node.left = self.delete(node.left, value)
        elif value > Node.value:
            node.right = self.delete(node.right, value)
        else:
            #CASO 1 DONDE NO HAY HIJOS O SOLO 1
            if node.left is None:
                return node.rigth
            elif node.right is None:
                return node.left
                #CASO 2 DOS HIJOS
            temp = self.getMinimumValueNode(node.right)
            node.value = temp.value
            node.right = self.delete(temp.value, node.right)
            #ACTUALIZAR ALTURA
            updateHeight(node)
            
        balance = getBalance(node)

        #falta colocar el return de las rotaciones, si este no se encuentra, la raiz no cambia
        #Es decir 

        if balance > 1 and getBalance(node.left) >= 0:
             return rotate_right(node) 
        elif balance > 1 and getBalance(node.left) < 0:
            node.left = rotate_left(node.left)
            return rotate_right(node) 
        elif balance < -1 and getBalance(node.right) <= 0:
            return rotate_left(node)
        elif balance < -1 and getBalance(node.right) > 0:
            node.right = rotate_right(node.right)
            return rotate_left(node) 
        
        return node 
    


avl = AVLTree()
values_to_insert = [10, 20, 30, 40, 50, 25]

print("Insertando valores:", values_to_insert)
for val in values_to_insert:
    avl.insert(val)

print("\n--- Después de inserciones ---")

