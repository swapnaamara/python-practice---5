n = int(input("Enter size: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter value {i+1}: ")))

even = 0
odd = 0
for x in arr:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)