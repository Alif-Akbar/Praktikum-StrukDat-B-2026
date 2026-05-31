class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert_root(self, data):
        self.root = Node(data)
    
    def insert_left(self, parent_node, data):
        if parent_node.left is None:
            parent_node.left = Node(data)
        else:
            new_node = Node(data)
            new_node.left = parent_node.left
            parent_node.left = new_node
    
    def insert_right(self, parent_node, data):
        if parent_node.right is None:
            parent_node.right = Node(data)
        else:
            new_node = Node(data)
            new_node.right = parent_node.right
            parent_node.right = new_node

tree = BinaryTree()

tree.insert_root("A")
tree.insert_left(tree.root, "B")
tree.insert_right(tree.root, "C")
tree.insert_left(tree.root.left, "D")
tree.insert_right(tree.root.left, "E")
tree.insert_right(tree.root.right, "F")


def in_order(node):
        if node is not None:
            in_order(node.left)
            print(node.data, end=" ")
            in_order(node.right)


def pre_order(node):
        if node is not None:
            print(node.data, end=" ")
            pre_order(node.left)
            pre_order(node.right)


def post_order(node):
        if node is not None:
            post_order(node.left)
            post_order(node.right)
            print(node.data, end=" ")

print("Pre_Order: ")
pre_order(tree.root)

print("In_Order: ")
in_order(tree.root)

print("Post_Order: ")
post_order(tree.root)