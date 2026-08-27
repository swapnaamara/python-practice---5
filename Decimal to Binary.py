n = int(input("Enter number: "))

binary = ""

while n > 0:
    binary = str(n % 2) + binary
    n //= 2

print(binary)
