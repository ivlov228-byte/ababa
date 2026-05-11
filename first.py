n = int(input("n = "))

if n >= 1:
    print(0)
if n >= 2:
    print(1)

a, b = 0, 1
for i in range(3, n + 1):
    c = a + b
    print(c)
    a, b = b, c
    