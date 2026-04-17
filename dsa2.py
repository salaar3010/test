# import time
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)
# n = int(input("Enter the number of terms in the Fibonacci series: "))
# total = 0;start=time.time()
# print("Fibonacci series:")
# for i in range(n):
#     val = fibonacci(i)
#     print(val, end=" ")
#     total += val
# print("\nSum =", total);end=time.time()
# print("Time taken:", end - start, "seconds")
def traverse(graph, start, mode="bfs"):
    visited = set()
    ds = [start]   # common list (acts as queue/stack)
    result = []

    while ds:
        # 🔁 ONLY CHANGE
        if mode == "bfs":
            node = ds.pop(0)   # queue (FIFO)
        else:
            node = ds.pop()    # stack (LIFO)

        if node not in visited:
            visited.add(node)
            result.append(node)

            # add neighbors
            ds.extend(graph[node])

    return result


def main():
    g = {
        0:[1,2],
        1:[3],
        2:[4],
        3:[],
        4:[]
    }

    print("BFS:", traverse(g, 0, "bfs"))
    print("DFS:", traverse(g, 0, "dfs"))


if __name__ == "__main__":
    main()

def quick(a):
    if len(a)<=1: return a
    p=a[0]
    return quick([x for x in a[1:] if x<=p]) + [p] + quick([x for x in a[1:] if x>p])

def merge(a):
    if len(a)<=1: return a
    m=len(a)//2
    l,r=merge(a[:m]),merge(a[m:])
    res=[]
    while l and r:
        res.append(l.pop(0) if l[0]<r[0] else r.pop(0))
    return res + l + r

def main():
    arr=[5,1,3]
    print("Quick:", quick(arr))
    print("Merge:", merge(arr))

if __name__ == "__main__": main()

def bubble(a):
    for i in range(len(a)):
        for j in range(len(a)-1-i):
            if a[j] > a[j+1]: a[j],a[j+1]=a[j+1],a[j]
    return a

def insertion(a):
    for i in range(1,len(a)):
        key,j=a[i],i-1
        while j>=0 and a[j]>key:
            a[j+1]=a[j]; j-=1
        a[j+1]=key
    return a

def selection(a):
    for i in range(len(a)):
        m=i
        for j in range(i+1,len(a)):
            if a[j]<a[m]: m=j
        a[i],a[m]=a[m],a[i]
    return a

def main():
    arr=[5,2,4]
    print(bubble(arr.copy()), insertion(arr.copy()), selection(arr.copy()))

if __name__ == "__main__": main()

import heapq

def dijkstra(graph, src):
    dist = {i: float('inf') for i in graph}
    dist[src] = 0

    pq = [(0, src)]

    while pq:
        d, u = heapq.heappop(pq)

        for v, w in graph[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))

    return dist


def main():
    g = {
        0: [(1,4),(2,1)],
        1: [(3,1)],
        2: [(1,2),(3,5)],
        3: []
    }

    print("Shortest paths:", dijkstra(g, 0))


if __name__ == "__main__":
    main()

import time
n = int(input("Enter the number of terms in the Fibonacci series: "))
a, b = 0, 1;total = 0
start = time.time()
print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    total += a
    a, b = b, a + b
print("\nSum =", total)
end = time.time()
print("Time taken:", end - start, "seconds")

# import time
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n-1)
# n = int(input("Enter a number: "))
# start = time.time();result = factorial(n)
# end = time.time();print("Factorial =", result)
# print("Time taken:", end - start, "seconds")

import time
n = int(input("Enter a number: "))
start = time.time();fact = 1
for i in range(1, n + 1):
    fact *= i
end = time.time(); print("Factorial =", fact)
print("Time taken:", end - start, "seconds")

class DynamicArray:
    def __init__(self, initial_capacity=4):
        self.capacity = initial_capacity
        self.size = 0
        self.array = [None] * self.capacity
        print(f"Initial capacity: {self.capacity}")
    def __len__(self):
        return self.size
    def _resize(self, new_capacity):
        old_array = self.array
        self.array = [None] * new_capacity
        self.capacity = new_capacity
        for i in range(self.size):
            self.array[i] = old_array[i]
    def append(self, value):
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        self.array[self.size] = value
        self.size += 1
    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bound")
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.size += 1
    def pop(self):
        if self.size == 0:
            raise IndexError("Array is empty")
        value = self.array[self.size - 1]
        self.array[self.size - 1] = None
        self.size -= 1
        if self.size <= self.capacity // 4 and self.capacity > 4:
            self._resize(self.capacity // 2)
        return value
    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bound")
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None
        self.size -= 1
        if self.size <= self.capacity // 4 and self.capacity > 4:
            self._resize(self.capacity // 2)
    def reverse(self):
        left, right = 0, self.size - 1
        while left < right:
            self.array[left], 
            self.array[right] = self.array[right],
            self.array[left]
            left += 1
            right -= 1
    def find(self, value):
        for i in range(self.size):
            if self.array[i] == value:
                return i
        return -1
    def slice(self, start, end):
        if start < 0 or end > self.size or start > end:
            raise IndexError("Invalid range")
        new_array = DynamicArray(end - start)
        for i in range(start, end):
            new_array.append(self.array[i])
        return new_array
    def get(self, index):
        if 0 <= index < self.size:
            return self.array[index]
        raise IndexError("Index out of bound")
    def __str__(self):
        return str(self.array[:self.size])

if __name__ == "__main__":
    arr = DynamicArray()

    # Append elements
    print("\nTesting append:")
    for i in range(12):
        arr.append(i)
        print(arr)

    # Insert element
    print("\nTesting insert:")
    arr.insert(2, 99)
    print(arr)

    # Pop last element
    print("\nTesting pop:")
    arr.pop()
    print(arr)

    # Remove element
    print("\nArray:", arr)
    index = int(input("Enter index to remove: "))
    arr.remove(index)
    print("Array after remove:", arr)

    # Reverse array
    arr.reverse()
    print("\nArray after reverse:", arr)

    # Find value
    value = int(input("\nEnter value to find: "))
    pos = arr.find(value)
    if pos != -1:
        print(f"Value {value} found at index {pos}")
    else:
        print("Value not found")

    # Slice array
    start = int(input("\nEnter start index: "))
    end = int(input("Enter end index: "))
    sliced = arr.slice(start, end)
    print("Sliced array:", sliced)

class StaticArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity

    def __len__(self):
        return self.size

    def append(self, value):
        if self.size == self.capacity:
            raise IndexError("static array is full")
        self.array[self.size] = value
        self.size += 1

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("index out of bound")
        if self.size == self.capacity:
            raise IndexError("static array is full")

        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]

        self.array[index] = value
        self.size += 1

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("index out of bound")
    
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]

        self.array[self.size - 1] = None
        self.size -= 1

    def reverse(self):
        left = 0
        right = self.size - 1

        while left < right:
            self.array[left], 
            self.array[right] = self.array[right], 
            self.array[left]
            left += 1
            right -= 1

    def find(self, value):
        for i in range(self.size):
            if self.array[i] == value:
                return i
        return -1

    def slice(self, start, end):
        if start < 0 or end > self.size or start > end:
            raise IndexError("invalid range")

        new_array = StaticArray(end - start)
        for i in range(start, end):
            new_array.append(self.array[i])

        return new_array

    def get(self, index):
        if 0 <= index < self.size:
            return self.array[index]
        else:
            raise IndexError("index out of bound")
        
    def __str__(self):
        return str(self.array[:self.size])


if __name__ == "__main__":
    arr = StaticArray(5)

    # Append elements
    for i in range(5):
        arr.append(i)
        print(f"Appended {i}, size = {len(arr)}")

    # Remove element at index
    index = int(input("\nEnter index to remove: "))
    arr.remove(index)
    print("Array after remove:", arr)

    # Reverse array
    arr.reverse()
    print("\nArray after reverse:", arr)

    # Find value
    value = int(input("\nEnter value to find: "))
    pos = arr.find(value)
    if pos != -1:
        print(f"Value {value} found at index {pos}")
    else:
        print(f"Value {value} not found")

    # Slice array
    start = int(input("\nEnter start index: "))
    end = int(input("Enter end index: "))
    sliced_array = arr.slice(start, end)
    print("Sliced array:", sliced_array)

from collections import deque
# ---------------- STACK ----------------
class Stack:
    def __init__(self, n):
        self.arr = [None]*n
        self.top = -1
        self.n = n

    def push(self, x):
        if self.top == self.n-1:
            print("Overflow"); return
        self.top += 1
        self.arr[self.top] = x

    def pop(self):
        if self.top == -1:
            print("Underflow"); return None
        x = self.arr[self.top]
        self.top -= 1
        return x

    def peek(self):
        return None if self.top==-1 else self.arr[self.top]

    def is_empty(self):
        return self.top == -1

    def size(self):
        return self.top + 1


# ---------------- CIRCULAR QUEUE ----------------
class Queue:
    def __init__(self, n):
        self.q = [None]*n
        self.front = self.rear = -1
        self.n = n

    def enqueue(self, x):
        if (self.rear+1)%self.n == self.front:
            print("Overflow"); return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear+1)%self.n
        self.q[self.rear] = x

    def dequeue(self):
        if self.front == -1:
            print("Underflow"); return None
        x = self.q[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front+1)%self.n
        return x

    def is_empty(self):
        return self.front == -1

# ---------------- BFS MAZE (QUEUE APPLICATION) ----------------
def bfs_maze(grid, start, goal):

    r, c = len(grid), len(grid[0])
    q = deque([start])
    visited = set([start])
    parent = {}

    dirs = [(1,0),(-1,0),(0,1),(0,-1)]

    while q:
        x, y = q.popleft()

        if (x, y) == goal:
            path = []
            while (x, y) in parent:
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append(start)
            return path[::-1]

        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0<=nx<r and 0<=ny<c and grid[nx][ny]==0 and (nx,ny) not in visited:
                q.append((nx, ny))
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)

    return None

# ---------------- INFIX TO POSTFIX ----------------
def prec(op):
    return 1 if op in "+-" else 2 if op in "*/" else 0

def infix_to_postfix(exp):
    st = Stack(len(exp))
    res = []

    for ch in exp:
        if ch.isalnum():
            res.append(ch)
        elif ch == '(':
            st.push(ch)
        elif ch == ')':
            while st.peek() != '(':
                res.append(st.pop())
            st.pop()
        else:
            while not st.is_empty() and prec(ch) <= prec(st.peek()):
                res.append(st.pop())
            st.push(ch)

    while not st.is_empty():
        res.append(st.pop())

    return ''.join(res)


# ---------------- POSTFIX EVALUATION ----------------
def eval_postfix(exp):
    st = Stack(len(exp))

    for ch in exp:
        if ch.isdigit():
            st.push(int(ch))
        else:
            b = st.pop()
            a = st.pop()

            if ch == '+': st.push(a+b)
            elif ch == '-': st.push(a-b)
            elif ch == '*': st.push(a*b)
            elif ch == '/': st.push(a//b)

    return st.pop()

def traverse(graph, start, mode="bfs"):
    visited = set()
    ds = [start]
    result = []

    while ds:
        # 🔁 ONLY CHANGE
        if mode == "bfs":
            node = ds.pop(0)   # queue (FIFO)
        else:
            node = ds.pop()    # stack (LIFO)

        if node not in visited:
            visited.add(node)
            result.append(node)

            # add neighbors
            ds.extend(graph[node])

    return result


def main():
    g = {
        0:[1,2],
        1:[3],
        2:[4],
        3:[],
        4:[]
    }

    print("BFS:", traverse(g, 0, "bfs"))
    print("DFS:", traverse(g, 0, "dfs"))


if __name__ == "__main__":
    main()
# ---------------- MAIN ----------------
def main():
    print("---- STACK ----")
    s = Stack(5)
    s.push(10); s.push(20)
    print("Pop:", s.pop())
    print("Peek:", s.peek())

    print("\n---- QUEUE ----")
    q = Queue(5)
    q.enqueue(1); q.enqueue(2)
    print("Dequeue:", q.dequeue())

    print("\n---- BFS MAZE ----")
    maze = [
        [0,1,0],
        [0,0,0],
        [1,0,0]
    ]
    print("Path:", bfs_maze(maze,(0,0),(2,2)))

    print("\n---- INFIX TO POSTFIX ----")
    exp = "(A+B)*C"
    print(exp, "->", infix_to_postfix(exp))

    print("\n---- POSTFIX EVAL ----")
    print("23+ =", eval_postfix("23+"))

if __name__ == "__main__":
    main()
from collections import deque

# ===================== SLL =====================
class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def insert_front(self, x):
        n = Node(x)
        n.next = self.head
        self.head = n

    def insert_end(self, x):
        n = Node(x)
        if not self.head:
            self.head = n; return
        t = self.head
        while t.next:
            t = t.next
        t.next = n

    def insert_pos(self, x, pos):
        if pos == 0:
            self.insert_front(x); return
        t = self.head
        for _ in range(pos-1):
            if not t: return
            t = t.next
        n = Node(x)
        n.next = t.next
        t.next = n

    def delete_front(self):
        if self.head:
            self.head = self.head.next

    def delete_end(self):
        if not self.head: return
        if not self.head.next:
            self.head = None; return
        t = self.head
        while t.next.next:
            t = t.next
        t.next = None

    def delete_pos(self, pos):
        if pos == 0:
            self.delete_front(); return
        t = self.head
        for _ in range(pos-1):
            if not t: return
            t = t.next
        if t and t.next:
            t.next = t.next.next

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def search(self, key):
        t = self.head; pos = 0
        while t:
            if t.data == key:
                return pos
            t = t.next; pos += 1
        return -1

    def count(self):
        t = self.head; c = 0
        while t:
            c += 1
            t = t.next
        return c

    def display(self):
        t = self.head
        while t:
            print(t.data, end=" -> ")
            t = t.next
        print("None")


# ===================== DLL =====================
class DNode:
    def __init__(self, d):
        self.data = d
        self.prev = self.next = None

class DLL:
    def __init__(self):
        self.head = None

    def insert_front(self, x):
        n = DNode(x)
        if self.head:
            self.head.prev = n
            n.next = self.head
        self.head = n

    def insert_end(self, x):
        n = DNode(x)
        if not self.head:
            self.head = n; return
        t = self.head
        while t.next:
            t = t.next
        t.next = n
        n.prev = t

    def insert_pos(self, x, pos):
        if pos == 0:
            self.insert_front(x); return
        t = self.head
        for _ in range(pos-1):
            if not t: return
            t = t.next
        n = DNode(x)
        n.next = t.next
        if t.next:
            t.next.prev = n
        t.next = n
        n.prev = t

    def delete_front(self):
        if self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None

    def delete_end(self):
        if not self.head: return
        t = self.head
        while t.next:
            t = t.next
        if t.prev:
            t.prev.next = None
        else:
            self.head = None

    def delete_pos(self, pos):
        t = self.head
        for _ in range(pos):
            if not t: return
            t = t.next
        if not t: return
        if t.prev:
            t.prev.next = t.next
        else:
            self.head = t.next
        if t.next:
            t.next.prev = t.prev

    def display(self):
        t = self.head
        while t:
            print(t.data, end=" <-> ")
            t = t.next
        print("None")


# ===================== CLL =====================
class CNode:
    def __init__(self, d):
        self.data = d
        self.next = None

class CLL:
    def __init__(self):
        self.tail = None

    def insert_front(self, x):
        n = CNode(x)
        if not self.tail:
            self.tail = n
            n.next = n
        else:
            n.next = self.tail.next
            self.tail.next = n

    def insert_end(self, x):
        self.insert_front(x)
        self.tail = self.tail.next

    def insert_pos(self, x, pos):
        if pos == 0:
            self.insert_front(x); return
        t = self.tail.next
        for _ in range(pos-1):
            t = t.next
        n = CNode(x)
        n.next = t.next
        t.next = n
        if t == self.tail:
            self.tail = n

    def delete_front(self):
        if not self.tail: return
        if self.tail.next == self.tail:
            self.tail = None
        else:
            self.tail.next = self.tail.next.next

    def delete_end(self):
        if not self.tail: return
        if self.tail.next == self.tail:
            self.tail = None; return
        t = self.tail.next
        while t.next != self.tail:
            t = t.next
        t.next = self.tail.next
        self.tail = t

    def delete_pos(self, pos):
        if pos == 0:
            self.delete_front(); return
        t = self.tail.next
        for _ in range(pos-1):
            t = t.next
        t.next = t.next.next

    def display(self):
        if not self.tail:
            print("Empty"); return
        t = self.tail.next
        while True:
            print(t.data, end=" -> ")
            t = t.next
            if t == self.tail.next:
                break
        print("(circular)")


# ===================== STACK APP =====================
def is_balanced(exp):
    st = []
    pairs = {')':'(', '}':'{', ']':'['}
    for ch in exp:
        if ch in "({[":
            st.append(ch)
        elif ch in ")}]":
            if not st or st.pop() != pairs[ch]:
                return False
    return len(st) == 0


# ===================== POLYNOMIAL =====================
    # print(add_poly([(2,3),(5,1)], [(3,3)]))

def add_poly(p1, p2):
    res = {}
    for c,d in p1: res[d] = res.get(d,0) + c
    for c,d in p2: res[d] = res.get(d,0) + c
    return sorted([(res[d], d) for d in res], reverse=True)


# ===================== QUEUE =====================
class CircularQueue:
    def __init__(self):
        self.q = []

    def enqueue(self, x):
        self.q.append(x)

    def dequeue(self):
        if self.q:
            return self.q.pop(0)

    def display(self):
        print(self.q)


# ===================== DFS =====================
def dfs(graph, start):
    visited = set()
    stack = [start]
    res = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            res.append(node)
            stack.extend(reversed(graph[node]))

    return res


# ===================== MAIN =====================
def main():
    print("=== SLL ===")
    s = SLL()
    s.insert_front(2); s.insert_end(3); s.insert_front(1)
    s.display()
    print("Search 3:", s.search(3))
    print("Count:", s.count())
    s.reverse(); s.display()

    print("\n=== DLL ===")
    d = DLL()
    for i in [1,2,3]: 
        d.insert_end(i)
        d.display()
        d.delete_pos(1)
        d.display()

    print("\n=== CLL ===")
    c = CLL()
    for i in [1,2,3]: 
        c.insert_end(i)
        c.display()
        c.delete_front()
        c.display()

    print("\n=== Stack ===")
    print(is_balanced("{[()]}"))

    print("\n=== Polynomial ===")
    print(add_poly([(2,3),(5,1)], [(3,3)]))

    print("\n=== Queue ===")
    q = CircularQueue()
    for i in range(5): q.enqueue(i)
    q.display()

    print("\n=== DFS ===")
    g = {0:[1,2],1:[0,3],2:[0],3:[]}
    print(dfs(g,0))


if __name__ == "__main__":
    main()

class Heap:
    def __init__(self, type="min"):
        self.h = []
        self.type = type   # "min" or "max"

    # 🔁 Compare function (ONLY difference)
    def compare(self, a, b):
        if self.type == "min":
            return a < b   # Min Heap
        else:
            return a > b   # Max Heap

    # ➕ Insert
    def insert(self, x):
        self.h.append(x)
        i = len(self.h) - 1

        while i > 0 and self.compare(self.h[i], self.h[(i-1)//2]):
            self.h[i], self.h[(i-1)//2] = self.h[(i-1)//2], self.h[i]
            i = (i-1)//2

    # 🔽 Heapify (down)
    def heapify(self, i):
        l, r = 2*i+1, 2*i+2
        best = i

        if l < len(self.h) and self.compare(self.h[l], self.h[best]):
            best = l
        if r < len(self.h) and self.compare(self.h[r], self.h[best]):
            best = r

        if best != i:
            self.h[i], self.h[best] = self.h[best], self.h[i]
            self.heapify(best)

    # ❌ Extract (min or max depending on type)
    def extract(self):
        if not self.h:
            return None

        if len(self.h) == 1:
            return self.h.pop()

        root = self.h[0]
        self.h[0] = self.h.pop()
        self.heapify(0)

        return root

    # 👀 Peek
    def peek(self):
        return self.h[0] if self.h else None

    # 📦 Build Heap
    def build(self, arr):
        self.h = arr[:]
        for i in range(len(self.h)//2 - 1, -1, -1):
            self.heapify(i)
     # ❌ DELETE ROOT (important)
    def delete(self):
        if not self.h:
            return None

        if len(self.h) == 1:
            return self.h.pop()

        root = self.h[0]           # store min/max
        self.h[0] = self.h.pop()  # move last to root
        self.heapify(0)           # fix heap

        return root

# 🚀 MAIN
def main():
    print("---- MIN HEAP ----")
    minh = Heap("min")
    for i in [5,3,8,1,2]:
        minh.insert(i)
    print("Heap:", minh.h)
    print("Extract Min:", minh.extract())
    print("After:", minh.h)

    print("\n---- MAX HEAP ----")
    maxh = Heap("max")
    for i in [5,3,8,1,2]:
        maxh.insert(i)
    print("Heap:", maxh.h)
    print("Extract Max:", maxh.extract())
    print("After:", maxh.h)


if __name__ == "__main__":
    main()
#avl
class Node:
    def __init__(self, k):
        self.k = k
        self.l = self.r = None
        self.h = 1

def height(n):
    return n.h if n else 0

def get_balance(n):
    return height(n.l) - height(n.r) if n else 0


# 🔁 Rotations
# ---------------- RIGHT ROTATION (LL CASE) ----------------
def right_rotate(y):

#before
    #       y
    #      /
    #     x
    #      \
    #       T
#after
     #       x
    #         \
    #          y
    #         / 
    #        T   
    x = y.l
    T = x.r

    x.r = y
    y.l = T

    y.h = 1 + max(h(y.l), h(y.r))
    x.h = 1 + max(h(x.l), h(x.r))

    return x


# ---------------- LEFT ROTATION (RR CASE) ----------------
def left_rotate(x):
    #before
    #  x    
    #   \
    #    y
    #   /
    #  T

    #after
    #    y
    #   / 
    #  x   
    #   \
    #    T
    y = x.r
    T = y.l

    y.l = x
    x.r = T

    x.h = 1 + max(h(x.l), h(x.r))
    y.h = 1 + max(h(y.l), h(y.r))

    return y


# 🌳 Insert
def insert(root, key):
    if not root:
        return Node(key)

    if key < root.k:
        root.l = insert(root.l, key)
    else:
        root.r = insert(root.r, key)

    root.h = 1 + max(height(root.l), height(root.r))
    bf = get_balance(root)

    # LL
    if bf > 1 and key < root.l.k:
        return right_rotate(root)

    # RR
    if bf < -1 and key > root.r.k:
        return left_rotate(root)

    # LR
    if bf > 1 and key > root.l.k:
        root.l = left_rotate(root.l)
        return right_rotate(root)

    # RL
    if bf < -1 and key < root.r.k:
        root.r = right_rotate(root.r)
        return left_rotate(root)

    return root


# 🔍 Search
def search(root, key):
    if not root or root.k == key:
        return root
    return search(root.l, key) if key < root.k else search(root.r, key)


# 🔄 Inorder
def inorder(root):
    if root:
        inorder(root.l)
        print(root.k, end=" ")
        inorder(root.r)


# 🚀 Main
def main():
    root = None
    arr = [30, 20, 40, 10, 25, 35, 50]

    for x in arr:
        root = insert(root, x)

    print("Inorder:")
    inorder(root)

    print("\nSearch 25:", bool(search(root, 25)))


if __name__ == "__main__":
    main()

import heapq

def prim(graph, start=0):
    visited = set()
    pq = [(0, start)]
    cost = 0

    while pq:
        w, u = heapq.heappop(pq)

        if u in visited:
            continue

        visited.add(u)
        cost += w

        for v, wt in graph[u]:
            if v not in visited:
                heapq.heappush(pq, (wt, v))

    return cost


def main():
    g = {
        0: [(1,2),(3,6)],
        1: [(0,2),(2,3),(3,8)],
        2: [(1,3),(3,7)],
        3: [(0,6),(1,8),(2,7)]
    }

    print("Prim MST Cost:", prim(g))


if __name__ == "__main__":
    main()

def find(p, x):
    if p[x] != x:
        p[x] = find(p, p[x])
    return p[x]

def union(p, r, x, y):
    x = find(p, x)
    y = find(p, y)

    if x != y:
        if r[x] < r[y]:
            p[x] = y
        elif r[x] > r[y]:
            p[y] = x
        else:
            p[y] = x
            r[x] += 1
        return True
    return False


def kruskal(n, edges):
    edges.sort()
    p = list(range(n))
    r = [0]*n
    cost = 0

    for w,u,v in edges:
        if union(p, r, u, v):
            cost += w

    return cost


def main():
    edges = [
        (2,0,1),
        (6,0,3),
        (3,1,2),
        (8,1,3),
        (7,2,3)
    ]

    print("Kruskal MST Cost:", kruskal(4, edges))


if __name__ == "__main__":
    main()

import heapq

def dijkstra(graph, src):
    dist = {i: float('inf') for i in graph}
    dist[src] = 0

    pq = [(0, src)]

    while pq:
        d, u = heapq.heappop(pq)

        for v, w in graph[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))

    return dist


def main():
    g = {
        0: [(1,4),(2,1)],
        1: [(3,1)],
        2: [(1,2),(3,5)],
        3: []
    }

    print("Shortest paths:", dijkstra(g, 0))


if __name__ == "__main__":
    main()

class Node:
    def __init__(self, d):
        self.data = d
        self.left = self.right = None

def insert(r, x):
    if not r: return Node(x)
    if x < r.data: r.left = insert(r.left, x)
    else: r.right = insert(r.right, x)
    return r

def search(r, x):
    if not r or r.data == x: return r
    return search(r.left, x) if x < r.data else search(r.right, x)

def inorder(r):
    if r: inorder(r.left); print(r.data, end=" "); inorder(r.right)

def main():
    root = None
    for i in [50,30,70,20,40]:
        root = insert(root, i)

    inorder(root)
    print("\nSearch 40:", bool(search(root,40)))

if __name__ == "__main__": main()


class Node:
    def __init__(self, d):
        self.data = d
        self.left = self.right = None

def inorder(r):
    if r: inorder(r.left); print(r.data, end=" "); inorder(r.right)

def preorder(r):
    if r: print(r.data, end=" "); preorder(r.left); preorder(r.right)

def postorder(r):
    if r: postorder(r.left); postorder(r.right); print(r.data, end=" ")

def main():
    root = Node('A')
    root.left = Node('B')
    root.right = Node('C')
    root.left.left = Node('D')

    print("Inorder:"); inorder(root)
    print("\nPreorder:"); preorder(root)
    print("\nPostorder:"); postorder(root)

if __name__ == "__main__": main()


def find_min(r):
    while r.left: r = r.left
    return r

def delete(r, x):
    if not r: return r
    if x < r.data: r.left = delete(r.left, x)
    elif x > r.data: r.right = delete(r.right, x)
    else:
        if not r.left: return r.right
        if not r.right: return r.left
        temp = find_min(r.right)
        r.data = temp.data
        r.right = delete(r.right, temp.data)
    return r


def eval_postfix(exp):
    st = []
    for ch in exp:
        if ch.isdigit():
            st.append(int(ch))
        else:
            b = st.pop()
            a = st.pop()
            if ch=='+': st.append(a+b)
            elif ch=='-': st.append(a-b)
            elif ch=='*': st.append(a*b)
            elif ch=='/': st.append(a//b)
    return st[0]

def main():
    print("Result:", eval_postfix("23+5*"))  # (2+3)*5

if __name__ == "__main__": main()


class Node:
    def __init__(self, d):
        self.data = d
        self.count = 1
        self.left = self.right = None

def insert(r, x):
    if not r: return Node(x)
    if x < r.data: r.left = insert(r.left, x)
    elif x > r.data: r.right = insert(r.right, x)
    else: r.count += 1
    return r

def inorder(r):
    if r:
        inorder(r.left)
        print(r.data, ":", r.count)
        inorder(r.right)

def main():
    root = None
    words = ["a","b","a","c","b"]
    for w in words:
        root = insert(root, w)

    inorder(root)

if __name__ == "__main__": main()
