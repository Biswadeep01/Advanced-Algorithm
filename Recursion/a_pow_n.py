"""calculating a^n using recursion"""

def sum(a, n):
    if (n>0):
        return a * sum (a, n-1)
    else:
        return 1

if __name__== '__main__':
    a = int(input("Enter the Base value: "))
    n = int(input("Enter the Power value: "))
    print(f"Value of {a}^{n} is : ",sum(a, n))