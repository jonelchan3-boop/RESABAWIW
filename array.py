# 1. Array Implementation - Assessment 3.2
print("=== 1. ARRAY ===")

# Step 1: Declare array with size = 6
NAME = [None] * 6

# Step 2: Add letters of RESABA
NAME[0] = 'R'
NAME[1] = 'E'
NAME[2] = 'S'
NAME[3] = 'A'
NAME[4] = 'B'
NAME[5] = 'A'
print("After adding:", NAME)

# Step 3: Remove elements one by one from the end
while NAME:
    removed = NAME.pop()
    print(f"Removed '{removed}' → {NAME if NAME else 'EMPTY'}")

print("=== End ===\n")
