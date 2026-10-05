# Part C - List Report

items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

# 2. Numbered list
number = 1
for item in items:
    print(str(number) + ". " + item)
    number += 1

# 3. Count names with more than 4 letters
count = 0
for item in items:
    if len(item) > 4:
        count += 1
print("Items with more than 4 letters:", count)

# 4. Longest name using a loop comparison (no max())
longest = items[0]
for item in items:
    if len(item) > len(longest):
        longest = item
print("Longest item name:", longest)
