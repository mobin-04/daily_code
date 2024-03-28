class Stacks:
    def __init__(self,arr):
        self.arr=arr
    def isempty(self):
        return len(self.arr)==0
    def push(self,ele):
        self.arr.append(ele)
    def pop(self):
        self.arr.pop()
    
n=5
arr=[]
s1=Stacks(arr)
for i in range(n):
    s1.push(i)
print(arr)
for i in range(5):
    a=arr.pop()
    print(a)
print(s1.isempty())
print(arr)