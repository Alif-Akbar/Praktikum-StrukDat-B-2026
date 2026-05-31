
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