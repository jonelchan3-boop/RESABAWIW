# 3. Stack (LIFO) Implementation - Assessment 3.2
print("=== 3. STACK (LIFO) ===")

NAME_STACK = []

# Step 2: Push letters
for ch in ['R','E','S','A','B','A']:
    NAME_STACK.append(ch)
    print(f"Push '{ch}' → {NAME_STACK}")

# Step 3: Pop until empty
while NAME_STACK:
    removed = NAME_STACK.pop()
    print(f"Pop '{removed}' → {NAME_STACK if NAME_STACK else 'EMPTY'}")

print("=== End ===\n")
