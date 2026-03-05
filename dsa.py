'''

Experiment – 2
class StaticArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.arr = [None]*capacity

    def append(self, x):
        if self.size == self.capacity:
            print("Array Full")
            return
        self.arr[self.size] = x
        self.size += 1

    def insert(self, i, x):
        if self.size == self.capacity:
            print("Array Full")
            return
        for j in range(self.size, i, -1):
            self.arr[j] = self.arr[j-1]
        self.arr[i] = x
        self.size += 1

    def get(self, i):
        return self.arr[i]

    def display(self):
        print(self.arr[:self.size])



# Test
a = StaticArray(5)
a.append(10)
a.append(20)
a.insert(1,15)
a.display()

class DynamicArray:
    def __init__(self, cap=2):
        self.cap = cap
        self.size = 0
        self.arr = [None]*cap

    def resize(self):
        self.cap *= 2
        new = [None]*self.cap
        for i in range(self.size):
            new[i] = self.arr[i]
        self.arr = new

    def append(self,x):
        if self.size == self.cap:
            self.resize()
        self.arr[self.size] = x
        self.size += 1

    def insert(self,i,x):
        if self.size == self.cap:
            self.resize()
        for j in range(self.size,i,-1):
            self.arr[j] = self.arr[j-1]
        self.arr[i] = x
        self.size += 1

    def pop(self):
        x = self.arr[self.size-1]
        self.size -= 1
        return x

    def display(self):
        print(self.arr[:self.size])


# Test
a = DynamicArray()
for i in range(6):
    a.append(i)

a.insert(2,99)
a.display()
a.pop()
a.display()









Experiment 3 – stack and queue
class Stack:
    def __init__(self,n):
        self.arr=[None]*n
        self.top=-1
        self.n=n

    def push(self,x):
        if self.top==self.n-1:
            print("Overflow")
        else:
            self.top+=1
            self.arr[self.top]=x

    def pop(self):
        if self.top==-1:
            print("Underflow")
        else:
            x=self.arr[self.top]
            self.top-=1
            return x

    def peek(self):
        return self.arr[self.top]

s=Stack(5)
s.push(10)
s.push(20)
print(s.pop())


class Queue:
    def __init__(self,n):
        self.q=[None]*n
        self.n=n
        self.front=self.rear=-1

    def enqueue(self,x):
        if (self.rear+1)%self.n==self.front:
            print("Overflow")
        else:
            if self.front==-1:
                self.front=0
            self.rear=(self.rear+1)%self.n
            self.q[self.rear]=x

    def dequeue(self):
        if self.front==-1:
            print("Underflow")
        else:
            x=self.q[self.front]
            if self.front==self.rear:
                self.front=self.rear=-1
            else:
                self.front=(self.front+1)%self.n
            return x

q=Queue(5)
q.enqueue(10)
q.enqueue(20)
print(q.dequeue())

# Infix → Postfix
def prec(x):
    if x in "+-": return 1
    if x in "*/": return 2
    return 0

def infix_to_postfix(exp):
    stack=[]
    out=""

    for c in exp:
        if c.isalnum():
            out+=c
        elif c=="(":
            stack.append(c)
        elif c==")":
            while stack and stack[-1]!="(":
                out+=stack.pop()
            stack.pop()
        else:
            while stack and prec(c)<=prec(stack[-1]):
                out+=stack.pop()
            stack.append(c)

    while stack:
        out+=stack.pop()

    return out

print(infix_to_postfix("A+B*C"))

Postfix Evaluation:
def eval_postfix(exp):
    stack=[]

    for c in exp:
        if c.isdigit():
            stack.append(int(c))
        else:
            b=stack.pop()
            a=stack.pop()

            if c=='+': stack.append(a+b)
            elif c=='-': stack.append(a-b)
            elif c=='*': stack.append(a*b)
            elif c=='/': stack.append(a//b)

    return stack.pop()

print(eval_postfix("23+"))









#Experiment 4 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None

    def insert_end(self,x):
        n=Node(x)
        if not self.head:
            self.head=n
        else:
            t=self.head
            while t.next:
                t=t.next
            t.next=n

    def delete_front(self):
        if self.head:
            self.head=self.head.next

    def display(self):
        t=self.head
        while t:
            print(t.data,end=" -> ")
            t=t.next
        print("None")

l=SLL()
l.insert_end(10)
l.insert_end(20)
l.insert_end(30)
l.display()

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DLL:
    def __init__(self):
        self.head=None

    def insert_end(self,x):
        n=Node(x)
        if not self.head:
            self.head=n
        else:
            t=self.head
            while t.next:
                t=t.next
            t.next=n
            n.prev=t

    def display(self):
        t=self.head
        while t:
            print(t.data,end=" <-> ")
            t=t.next
        print("None")

l=DLL()
l.insert_end(10)
l.insert_end(20)
l.insert_end(30)
l.display()	



#circular ll
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CLL:
    def __init__(self):
        self.tail=None

    def insert_end(self,x):
        n=Node(x)
        if not self.tail:
            self.tail=n
            n.next=n
        else:
            n.next=self.tail.next
            self.tail.next=n
            self.tail=n

    def display(self):
        if not self.tail:
            return
        t=self.tail.next
        while True:
            print(t.data,end=" -> ")
            t=t.next
            if t==self.tail.next:
                break
        print("(circular)")

l=CLL()
l.insert_end(10)
l.insert_end(20)
l.insert_end(30)
l.display()

#Experiment 5
Binary Tree Implementation
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)

root=Node('A')
root.left=Node('B')
root.right=Node('C')
root.left.left=Node('D')
root.left.right=Node('E')

inorder(root)




BST Insert + Search
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insert(root,x):
    if root is None:
        return Node(x)

    if x < root.data:
        root.left=insert(root.left,x)
    else:
        root.right=insert(root.right,x)

    return root

def search(root,x):
    if root is None:
        return False
    if root.data==x:
        return True
    if x < root.data:
        return search(root.left,x)
    return search(root.right,x)

root=None

for v in [50,30,70,20,40]:
    root=insert(root,v)

print(search(root,40))

BST Delete
def findmin(root):
    while root.left:
        root=root.left
    return root

def delete(root,x):
    if root is None:
        return root

    if x < root.data:
        root.left=delete(root.left,x)

    elif x > root.data:
        root.right=delete(root.right,x)

    else:
        if root.left is None:
            return root.right

        if root.right is None:
            return root.left

        temp=findmin(root.right)
        root.data=temp.data
        root.right=delete(root.right,temp.data)

    return root
4. Expression Tree
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def evaluate(root):

    if root.left is None and root.right is None:
        return int(root.data)

    l=evaluate(root.left)
    r=evaluate(root.right)

    if root.data=='+': return l+r
    if root.data=='-': return l-r
    if root.data=='*': return l*r

root=Node('*')
root.left=Node('+')
root.right=Node('2')

root.left.left=Node('5')
root.left.right=Node('3')

print(evaluate(root))

BST Dictionary (Word Count)
class Node:
    def __init__(self,word):
        self.word=word
        self.count=1
        self.left=None
        self.right=None

def insert(root,word):

    if root is None:
        return Node(word)

    if word==root.word:
        root.count+=1

    elif word < root.word:
        root.left=insert(root.left,word)

    else:
        root.right=insert(root.right,word)

    return root

words=["apple","banana","apple"]

root=None

for w in words:
    root=insert(root,w)

print("apple count:",root.count)



Lab 6
1. Min Heap
import heapq

heap=[3,9,2,1,4]

heapq.heapify(heap)

print(heap)

print(heapq.heappop(heap))

2. Max Heap
import heapq

arr=[3,9,2,1,4]

maxheap=[-x for x in arr]

heapq.heapify(maxheap)

print(-heapq.heappop(maxheap))

3. Heap Operations
import heapq

h=[]

heapq.heappush(h,5)
heapq.heappush(h,2)
heapq.heappush(h,8)

print(heapq.heappop(h))

4. Priority Queue
import heapq

pq=[]

heapq.heappush(pq,(3,"A"))
heapq.heappush(pq,(1,"Emergency"))
heapq.heappush(pq,(2,"B"))

while pq:
    print(heapq.heappop(pq))

5. Heap Sort
import heapq

arr=[3,9,2,1,4,5]

heapq.heapify(arr)

sorted_arr=[]

while arr:
    sorted_arr.append(heapq.heappop(arr))

print(sorted_arr)


'''