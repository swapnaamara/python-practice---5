base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))

result = 1

for i in range(1, exp+1):
    result *= base

print(result)
