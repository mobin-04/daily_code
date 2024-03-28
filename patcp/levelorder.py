class treenode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def level_order(root):
    if root is None:
        return
    queue=[root]
    while queue:
        current_level=[]
        level_size=len(queue)
        for i in range(level_size):
            node=queue.pop(0)
            current_level.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print(*current_level,sep=" ",end=" ")
root=treenode(1)
root.left=treenode(2)
root.right=treenode(3)
root.left.left=treenode(4)
root.left.right=treenode(5)
root.right.left=treenode(6)
root.right.right=treenode(7)
print("level order traversal:")
level_order(root)