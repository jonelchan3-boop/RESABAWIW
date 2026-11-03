# 5. Doubly Linked List Implementation - Assessment 3.2
print("=== 5. DOUBLY LINKED LIST ===")

class DNode:
    def __init__(self, data):
        self.DATA = data
        self.PREV = None
        self.NEXT = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_end(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = self.tail = new_node
            return
        new_node.PREV = self.tail
        self.tail.NEXT = new_node
        self.tail = new_node

    def remove_last(self):
        if not self.head:
            return None
        val = self.tail.DATA
        if self.head == self.tail:
            self.head = self.tail = None
            return val
        self.tail = self.tail.PREV
        self.tail.NEXT = None
        return val

    def __str__(self):
        vals = []
        curr = self.head
        while curr:
            vals.append(curr.DATA)
            curr = curr.NEXT
        return " → ".join(vals) if vals else "EMPTY"

# Step 2: Add letters
dll = DoublyLinkedList()
for ch in ['R','E','S','A','B','A']:
    dll.add_end(ch)
    print(f"Add '{ch}' → {dll}")

# Step 3: Remove from end
while dll.head:
    removed = dll.remove_last()
    print(f"Removed last '{removed}' → {dll}")

print("=== End ===\n")
