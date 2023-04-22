# Stack
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


# Queue
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


#linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head # type: ignore
        self.head = new_node

    def add_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node

    def delete_node(self, key):
        curr_node = self.head
        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return
        prev_node = None
        while curr_node and curr_node.data != key:
            prev_node = curr_node
            curr_node = curr_node.next
        if curr_node is None:
            return
        prev_node.next = curr_node.next
        curr_node = None

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next


# tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def add_node(self, val):
        new_node = TreeNode(val)
        if not self.root:
            self.root = new_node
            return
        queue = [self.root]
        while queue:
            curr_node = queue.pop(0)
            if curr_node.left is None:
                curr_node.left = new_node
                return
            else:
                queue.append(curr_node.left)
            if curr_node.right is None:
                curr_node.right = new_node
                return
            else:
                queue.append(curr_node.right)
    
    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.val)
            self.in_order_traversal(node.right)
