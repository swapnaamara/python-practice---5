n1 = int(input("Enter size of first array: "))
a = []

for i in range(n1):
    a.append(int(input(f"Enter value {i+1} for first array: ")))

n2 = int(input("Enter size of second array: "))
b = []

for i in range(n2):
    b.append(int(input(f"Enter value {i+1} for second array: ")))

print("Intersection:", end=" ")

for i in range(n1):
    for j in range(n2):
        if a[i] == b[j]:
            print(a[i], end=" ")
            break
