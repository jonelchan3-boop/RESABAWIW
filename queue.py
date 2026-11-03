# 4. Queue (FIFO) Implementation - Assessment 3.2
from collections import deque

print("=== 4. QUEUE (FIFO) ===")

NAME_QUEUE = deque()

# Step 2: Enqueue letters
for ch in ['R','E','S','A','B','A']:
    NAME_QUEUE.append(ch)
    print(f"Enqueue '{ch}' → Front: {NAME_QUEUE[0]} | {list(NAME_QUEUE)}")

# Step 3: Dequeue until empty
while NAME_QUEUE:
    removed = NAME_QUEUE.popleft()
    print(f"Dequeue '{removed}' → {list(NAME_QUEUE) if NAME_QUEUE else 'EMPTY'}")

print("=== End ===\n")
