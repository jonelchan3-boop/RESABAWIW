# 6. Circular Linked List Implementation - Assessment 3.2
print("=== 6. CIRCULAR LINKED LIST ===")

class CNode:
    def __init__(self, data):
        self.DATA = data
        self.NEXT = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add_end(self, data):
        new_node = CNode(data)
        if not self.head:
            self.head = new_node
            new_node.NEXT = self.head
            return
        curr = self.head
        while curr.NEXT != self.head:
            curr = curr.NEXT
        curr.NEXT = new_node
        new_node.NEXT = self.head

    def remove_last(self):
        if not self.head:
            return None
        if self.head.NEXT == self.head:
            val = self.head.DATA
            self.head = None
            return val
        prev = None
        curr = self.head
        while curr.NEXT != self.head:
            prev = curr
            curr = curr.NEXT
        prev.NEXT = self.head
        return curr.DATA

    def __str__(self):
        if not self.head:
            return "EMPTY"
        vals = []
        curr = self.head
        while True:
            vals.append(curr.DATA)
            curr = curr.NEXT
            if curr == self.head:
                break
        return " → ".join(vals) + " → (back to " + self.head.DATA + ")"

# Step 2: Add letters
cll = CircularLinkedList()
for ch in ['R','E','S','A','B','A']:
    cll.add_end(ch)
    print(f"Add '{ch}' → {cll}")

# Step 3: Remove from end
while cll.head:
    removed = cll.remove_last()
    print(f"Removed last '{removed}' → {cll}")

print("=== End ===\n")
