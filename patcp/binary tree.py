class Node:
    def __init__(self,key):
        self.leftchild=None
        self.rightchild=None
        self.data=key
def Inorder(root):
     if root:
        Inorder(root.leftchild)
        print(root.data,end=" ")
        Inorder(root.rightchild)
def preorder(root):
     if root:
        preorder(root.leftchild)
        print(root.data,end=" ")
        preorder(root.rightchild)
def postorder(root):
     if root:
        postorder(root.leftchild)
        print(root.data,end=" ")
        postorder(root.rightchild)
root=Node(1)
root.leftchild=Node(2)
root.rightchild=Node(3)
root.leftchild.leftchild=Node(4)
root.leftchild.rightchild=Node(5)
root.rightchild.leftchild=Node(6)

print("inorder traversal")
Inorder(root)
print("\npreorder traversal")
preorder(root)
print("\npost order traversal")
postorder(root)