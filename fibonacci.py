"""Fibonacci Series - 0 1 1 2 3 5 8 ... nth term"""

n = int(input("Enter the term: "))
a, b = 0, 1
print("The Fibonacci series is : ", end=" ")
for i in range (1, n+1):
    c = a + b
    print(a, end=" ")
    a, b = b, c