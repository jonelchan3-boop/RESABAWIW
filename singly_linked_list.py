# 2. Singly Linked List Implementation - Assessment 3.2
print("=== 2. SINGLY LINKED LIST ===")

class Node:
    def __init__(self, data):
        self.DATA = data
        self.NEXT = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.NEXT:
            current = current.NEXT
        current.NEXT = new_node

    def remove_last(self):
        if not self.head:
            return None
        if not self.head.NEXT:
            val = self.head.DATA
            self.head = None
            return val
        prev = None
        current = self.head
        while current.NEXT:
            prev = current
            current = current.NEXT
        prev.NEXT = None
        return current.DATA

    def __str__(self):
        vals = []
        curr = self.head
        while curr:
            vals.append(curr.DATA)
            curr = curr.NEXT
        return " → ".join(vals) if vals else "EMPTY"

# Step 2: Add letters
sll = SinglyLinkedList()
for ch in ['R','E','S','A','B','A']:
    sll.add_end(ch)
    print(f"Add '{ch}' → {sll}")

# Step 3: Remove from end
while sll.head:
    removed = sll.remove_last()
    print(f"Removed last '{removed}' → {sll}")

print("=== End ===\n")
