#two stacks using one stack
class twostacks:
    def __init__(self,n):
        self.size=n
        self.arr=[None]*n
        self.top1=-1
        self.top2=self.size
    def push1(self,x):
        if self.top1<self.top2-1:
            self.top1+=1
            self.arr[self.top1]=x
            print("pushed:",x)
        else:
            print("syack1 overflow")
    def push2(self,x):
        if self.top1<self.top2-1:
            self.top2-=1
            self.arr[self.top2]=x
            print("pushed:",x)
        else:
            print("syack2 overflow")
    def pop1(self):
        if self.top1>=0:
            self.top1-=1
            return x
        else:
            print("stack1 underflow")
    def pop2(self):
        if self.top2<self.size:
            x=self.arr[self.top2]
            self.top2+=1
            return x
        else:
            print("stack2 underflow")
st=twostacks(5)
st.push1(1)
st.push1(2)
st.push2(11)
st.push2(12)
st.push1(3)
st.push2(4)
st.push1(5)