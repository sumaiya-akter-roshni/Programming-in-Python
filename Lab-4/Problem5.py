n = int(input("Enter N: "))

a = 0
b = 1
while a < n:
    print(a)
    temp = a + b
    a = b
    b = temp