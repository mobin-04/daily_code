#for every ith element append the greater element to a new linkedlist by comparing two linked list.
def newlist(root1,root2):
    ptr1=root1
    ptr2=root2
    root=None
    while(ptr1!=None):
        temp=Node(0)
        temp.next=None
        if(ptr.data<ptr2.data):
            temp.data=ptr2.data
        else:
            temp.data=ptr1.data
        if root==None:
            root=temp
        else:
            ptr=root
            while(ptr.next!=None):
                ptr=ptr.next
        p1=p1.next
        p2=p2.next
def Node():
    def __init__(self,data):
        self.data=data
        self.next=next
        