'''Insertion in a binary tree in level order
Algorithm:
Start
1. Create a queue and enqueue the root node.
2. While the queue is not empty,do the following:-
    a. Dequeue a node from the front of the queue
    b. if the left child of the dequeued node is empty,inset the new node as the left child.Otherwise enqueue the left child
    c. if the right child of the dequeued node is empty,insert the new node as the right child.Otherwise enqueue the right child
3. Repeat step 2 until new node is inserted into the binary tree.
END'''

from collections import deque
class treenode:
    def __init__(self,data):
        self.key=data
        self.left=None
        self.right=None
def Inorder(root):
     if root:
        Inorder(root.left)
        print(root.key,end=" ")
        Inorder(root.right)
def insert(root,key):
    if not root:
        return treenode(key)
    queue=deque([root])
    while queue:
        node=queue.popleft()
        if not node.left:
            node.left=treenode(key)
            break
        else:
            queue.append(node.left)
        if not node.right:
            node.right=treenode(key)
            break
        else:
            queue.append(node.right)
root=treenode(50)
root.left=treenode(30)
root.left.left=treenode(20)
root.left.right=treenode(40)
root.right=treenode(70)
root.right.right=treenode(80)
insert(root,118)