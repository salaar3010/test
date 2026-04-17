# EXPERIMENT 3 - Stack, Queue, BFS, Infix->Postfix, Postfix Evaluation

from collections import deque

# ---------------- STACK ----------------
class Stack:
    def __init__(self, n):
        self.a = [None]*n
        self.top = -1
        self.n = n

    def push(self, x):
        if self.top == self.n-1: return False
        self.top += 1
        self.a[self.top] = x
        return True

    def pop(self):
        if self.top == -1: return None
        x = self.a[self.top]
        self.top -= 1
        return x

    def peek(self):
        return None if self.top == -1 else self.a[self.top]

    def is_empty(self):
        return self.top == -1


# ---------------- CIRCULAR QUEUE ----------------
class Queue:
    def __init__(self, n):
        self.a = [None]*n
        self.n = n
        self.f = self.r = -1

    def enqueue(self, x):
        if (self.r+1)%self.n == self.f: return False
        if self.f == -1: self.f = 0
        self.r = (self.r+1)%self.n
        self.a[self.r] = x
        return True

    def dequeue(self):
        if self.f == -1: return None
        x = self.a[self.f]
        if self.f == self.r:
            self.f = self.r = -1
        else:
            self.f = (self.f+1)%self.n
        return x

    def is_empty(self):
        return self.f == -1


# ---------------- BFS (LATEST SIMPLE VERSION) ----------------
def bfs(graph, start):
    visited = set()
    q = deque([start])

    print("BFS Traversal:", end=" ")

    while q:
        node = q.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            q.extend(graph[node])


# ---------------- INFIX TO POSTFIX ----------------
def prec(op):
    if op in '+-': return 1
    if op in '*/': return 2
    return 0

def infix_to_postfix(s):
    st, out = [], []
    for ch in s:
        if ch.isalnum():
            out.append(ch)
        elif ch == '(':
            st.append(ch)
        elif ch == ')':
            while st[-1] != '(':
                out.append(st.pop())
            st.pop()
        else:
            while st and st[-1] != '(' and prec(ch) <= prec(st[-1]):
                out.append(st.pop())
            st.append(ch)

    while st:
        out.append(st.pop())

    return ''.join(out)


# ---------------- POSTFIX EVALUATION ----------------
def eval_postfix(s):
    st = []
    for ch in s:
        if ch.isdigit():
            st.append(int(ch))
        else:
            b = st.pop()
            a = st.pop()
            if ch == '+': st.append(a+b)
            elif ch == '-': st.append(a-b)
            elif ch == '*': st.append(a*b)
            elif ch == '/': st.append(a//b)
    return st.pop()


# ---------------- MAIN FUNCTION ----------------
if __name__ == "__main__":

    # Stack Demo
    s = Stack(5)
    s.push(10)
    s.push(20)
    print("Stack pop:", s.pop())

    # Queue Demo
    q = Queue(5)
    q.enqueue(100)
    q.enqueue(200)
    print("Queue dequeue:", q.dequeue())

    # BFS Demo
    graph = {
        1: [2, 3],
        2: [4],
        3: [5],
        4: [],
        5: []
    }
    bfs(graph, 1)
    print()

    # Infix to Postfix
    expr = "A+B*C"
    print("Postfix:", infix_to_postfix(expr))

    # Postfix Evaluation
    expr2 = "23+"
    print("Postfix Evaluation:", eval_postfix(expr2))
# EXPERIMENT 4 - Linked Lists and Applications

# ---------------- SINGLY LINKED LIST ----------------
class SNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new = SNode(data)
        new.next = self.head
        self.head = new

    def insert_end(self, data):
        new = SNode(data)
        if not self.head:
            self.head = new
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new

    def delete_front(self):
        if self.head:
            self.head = self.head.next

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")


# ---------------- DOUBLY LINKED LIST ----------------
class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = 

    # Insert at Start
    def insert_start(self, data):
        new = DNode(data)
        if not self.head:
            self.head = self.tail = new
            return
        new.next = self.head
        self.head.prev = new
        self.head = new

    # Insert at End
    def insert_end(self, data):
        new = DNode(data)
        if not self.head:
            self.head = self.tail = new
            return
        self.tail.next = new
        new.prev = self.tail
        self.tail = new

    #Insert After a Given Key (Middle)
    def insert_after(self, key, data):
        curr = self.head
        while curr:
            if curr.data == key:
                new = DNode(data)
                new.next = curr.next
                new.prev = curr

                if curr.next:
                    curr.next.prev = new
                else:
                    self.tail = new

                curr.next = new
                return
            curr = curr.next
        print("Key not found")

    # ---------------- DELETE ----------------

    # Delete from Start
    def delete_start(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = self.tail = None
            return
        self.head = self.head.next
        self.head.prev = None

    # Delete from End
    def delete_end(self):
        if not self.tail:
            return
        if self.head == self.tail:
            self.head = self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None

    # Delete by Key (Middle)
    def delete(self, key):
        curr = self.head
        while curr:
            if curr.data == key:

                # If first node
                if curr == self.head:
                    self.delete_start()
                    return

                # If last node
                if curr == self.tail:
                    self.delete_end()
                    return

                # Middle node
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                return
            curr = curr.next
        print("Key not found")

    # ---------------- PRINT ----------------

    def print_forward(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next
        print("None")


# ---------------- CIRCULAR LINKED LIST ----------------
class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.tail = None

    # ---------------- INSERT ----------------

    # 1️⃣ Insert at End (already given)
    def insert_end(self, data):
        new = CNode(data)
        if not self.tail:
            self.tail = new
            new.next = new
        else:
            new.next = self.tail.next
            self.tail.next = new
            self.tail = new

    # 2️⃣ Insert at Start
    def insert_start(self, data):
        new = CNode(data)
        if not self.tail:
            self.tail = new
            new.next = new
        else:
            new.next = self.tail.next
            self.tail.next = new

    # 3️⃣ Insert After a Given Key (Middle)
    def insert_after(self, key, data):
        if not self.tail:
            return

        curr = self.tail.next
        while True:
            if curr.data == key:
                new = CNode(data)
                new.next = curr.next
                curr.next = new

                if curr == self.tail:
                    self.tail = new
                return
            curr = curr.next
            if curr == self.tail.next:
                break
        print("Key not found")

    # ---------------- DELETE ----------------

    # 1️⃣ Delete Head (already given)
    def delete_head(self):
        if self.tail:
            if self.tail.next == self.tail:
                self.tail = None
            else:
                self.tail.next = self.tail.next.next

    # 2️⃣ Delete End
    def delete_end(self):
        if not self.tail:
            return

        if self.tail.next == self.tail:
            self.tail = None
            return

        curr = self.tail.next
        while curr.next != self.tail:
            curr = curr.next

        curr.next = self.tail.next
        self.tail = curr

    # 3️⃣ Delete by Key
    def delete(self, key):
        if not self.tail:
            return

        curr = self.tail.next
        prev = self.tail

        while True:
            if curr.data == key:

                # If only one node
                if curr == self.tail and curr.next == self.tail:
                    self.tail = None
                    return

                prev.next = curr.next

                if curr == self.tail:
                    self.tail = prev

                return

            prev = curr
            curr = curr.next

            if curr == self.tail.next:
                break

        print("Key not found")

    # ---------------- PRINT ----------------

    def print_list(self):
        if not self.tail:
            print("Empty")
            return

        curr = self.tail.next
        while True:
            print(curr.data, end=" -> ")
            curr = curr.next
            if curr == self.tail.next:
                break
        print("(circular)")


# ---------------- APPLICATION 1: DFS (Using SLL as Stack) ----------------
from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

def dfs(graph, start):
    visited = set()
    stack = [start]

    print("DFS Traversal:", end=" ")

    while stack:
        node = stack.pop()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            stack.extend(reversed(graph[node]))


dfs(graph, 'A')


# ---------------- APPLICATION 2: Polynomial Addition ----------------
def add_poly(p1, p2):
    result = {}
    for coeff, deg in p1 + p2:
        result[deg] = result.get(deg, 0) + coeff
    return [(result[d], d) for d in sorted(result, reverse=True)]


# ---------------- APPLICATION 3: Circular Queue ----------------
class CircularQueue(CircularLinkedList):
    def enqueue(self, data):
        self.insert_end(data)

    def dequeue(self):
        self.delete_head()


# ---------------- MAIN ----------------
if __name__ == "__main__":

    # Singly Linked List
    sll = SinglyLinkedList()
    sll.insert_end(1)
    sll.insert_end(2)
    sll.insert_front(0)
    sll.print_list()

    # Doubly Linked List
    dll = DoublyLinkedList()
    dll.insert_end(1)
    dll.insert_end(2)
    dll.insert_end(3)
    dll.delete(2)
    dll.print_forward()

    # Circular Linked List
    cll = CircularLinkedList()
    cll.insert_end(1)
    cll.insert_end(2)
    cll.insert_end(3)
    cll.print_list()

    # DFS
    g = Graph(5)
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,3)
    g.add_edge(2,4)
    print("DFS:", dfs(g,0))

    # Polynomial Addition
    p1 = [(2,3),(5,1),(1,0)]
    p2 = [(3,3),(2,1)]
    print("Poly Sum:", add_poly(p1,p2))

    # Circular Queue
    cq = CircularQueue()
    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    cq.dequeue()
    cq.print_list()
# EXPERIMENT 5 - Binary Tree and BST

# ---------------- TREE NODE ----------------
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# ---------------- 1. BINARY TREE ----------------
class BinaryTree:
    def __init__(self):
        self.root = None

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")


# ---------------- 2. BST (Insert + Search + Delete) ----------------
class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if not node:
            return Node(data)
        if data < node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)
        return node

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, node, data):
        if not node:
            return False
        if node.data == data:
            return True
        if data < node.data:
            return self._search(node.left, data)
        return self._search(node.right, data)

    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        if not node:
            return node
        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            # Case 1 & 2
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            # Case 3: Two children
            temp = self._find_min(node.right)
            node.data = temp.data
            node.right = self._delete(node.right, temp.data)
        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)


# ---------------- 3. EXPRESSION TREE ----------------
class ExpressionTree:
    def __init__(self):
        self.root = None

    def build_from_postfix(self, postfix):
        stack = []
        for ch in postfix:
            if ch.isdigit():
                stack.append(Node(ch))
            else:
                right = stack.pop()
                left = stack.pop()
                node = Node(ch)
                node.left = left
                node.right = right
                stack.append(node)
        self.root = stack.pop()

    def evaluate(self, root):
        if not root.left and not root.right:
            return int(root.data)
        l = self.evaluate(root.left)
        r = self.evaluate(root.right)
        if root.data == '+': return l + r
        if root.data == '-': return l - r
        if root.data == '*': return l * r
        if root.data == '/': return l // r


# ---------------- 4. BST DICTIONARY ----------------
class BSTDictionary:
    class DictNode:
        def __init__(self, word):
            self.word = word
            self.count = 1
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, word):
        self.root = self._insert(self.root, word)

    def _insert(self, node, word):
        if not node:
            return self.DictNode(word)
        if word < node.word:
            node.left = self._insert(node.left, word)
        elif word > node.word:
            node.right = self._insert(node.right, word)
        else:
            node.count += 1
        return node

    def search(self, word):
        node = self.root
        while node:
            if word == node.word:
                return node.count
            node = node.left if word < node.word else node.right
        return 0

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(f"{node.word}:{node.count}", end=" ")
            self.inorder(node.right)


# ---------------- MAIN ----------------
if __name__ == "__main__":

    # Binary Tree
    bt = BinaryTree()
    bt.root = Node('A')
    bt.root.left = Node('B')
    bt.root.right = Node('C')
    print("Binary Tree Inorder:", end=" ")
    bt.inorder(bt.root)
    print()

    # BST
    bst = BST()
    for v in [50,30,70,20,40,60,80]:
        bst.insert(v)
    print("BST Inorder:", end=" ")
    bst.inorder(bst.root)
    print("\nSearch 40:", bst.search(40))
    bst.delete(50)
    print("After delete 50:", end=" ")
    bst.inorder(bst.root)
    print()

    # Expression Tree
    et = ExpressionTree()
    et.build_from_postfix("23+4*")  # (2+3)*4
    print("Expression Result:", et.evaluate(et.root))

    # BST Dictionary
    d = BSTDictionary()
    words = ["apple","banana","apple","cherry"]
    for w in words:
        d.insert(w)
    print("Dictionary:", end=" ")
    d.inorder(d.root)
    print("\napple count:", d.search("apple"))


# EXPERIMENT 6 - Min Heap, Max Heap and Applications


class Heap:
    def __init__(self, is_min=True):
        self.heap = []
        self.is_min = is_min   # True → MinHeap, False → MaxHeap

    def parent(self, i): return (i - 1) // 2
    def left(self, i): return 2 * i + 1
    def right(self, i): return 2 * i + 2

    def compare(self, a, b):
        if self.is_min:
            return a < b
        return a > b

    # INSERT
    def insert(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1

        while i > 0 and self.compare(self.heap[i], self.heap[self.parent(i)]):
            p = self.parent(i)
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            i = p

    # EXTRACT (min or max)
    def extract(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0)
        return root

    # HEAPIFY
    def heapify(self, i):
        n = len(self.heap)
        l = self.left(i)
        r = self.right(i)
        target = i

        if l < n and self.compare(self.heap[l], self.heap[target]):
            target = l
        if r < n and self.compare(self.heap[r], self.heap[target]):
            target = r

        if target != i:
            self.heap[i], self.heap[target] = self.heap[target], self.heap[i]
            self.heapify(target)


# ---------------- PRIORITY QUEUE (Min Heap Based) ----------------
class SimplePriorityQueue:
    def __init__(self):
        self.data = []

    def enqueue(self, priority, value):
        self.data.append((priority, value))

    def dequeue(self):
        self.data.sort()
        return self.data.pop(0)

# ---------------- HEAP SORT ----------------
def heap_sort(arr):
    h = Heap(is_min=False)   # Max heap
    for x in arr:
        h.insert(x)

    result = []
    while h.heap:
        result.append(h.extract())
    return result


print(heap_sort([3, 9, 2, 1, 4, 5]))

# ---------------- MAIN ----------------
if __name__ == "__main__":

    # Min Heap
    mh = MinHeap()
    mh.build_heap([3,9,2,1,4,5])
    print("Min Heap:", mh.heap)
    print("Extract Min:", mh.extract_min())

    # Max Heap
    mx = MaxHeap()
    mx.build_heap([3,9,2,1,4,5])
    print("Max Heap:", mx.heap)
    print("Extract Max:", mx.extract_max())

    # Priority Queue
    pq = PriorityQueue()
    pq.enqueue(3,"Patient A")
    pq.enqueue(1,"Emergency B")
    pq.enqueue(2,"Patient C")
    print("Priority Queue:", [pq.dequeue() for _ in range(3)])

    # Heap Sort
    arr = [3,9,2,1,4,5]
    print("Heap Sort:", heap_sort(arr))
