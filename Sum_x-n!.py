"""x - x^3/3! + x^5/5! - x^7/7! + ... - x^n/n!"""

"""import math
def calculate_series(x, n):
    result = 0
    sign = 1
    
    for i in range(1, n+1, 2):
        result += sign * (x ** i) / math.factorial(i)
        sign *= -1
    
    return result

# Example usage:
x = 2
n = 10
result = calculate_series(x, n)
print("Result of the series:", result)
"""
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)
    
def calc(x, n):
    s=0
    t=-1
    for j in range (1, n+1, 2):
        t=t*(-1)
        s=s+t*(x**j)/fact(j)
    return s

x = float(input("Enter the value of x: "))
n = int(input("Enter the term: "))


