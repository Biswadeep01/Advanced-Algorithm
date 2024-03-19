"""s = 1 + x^2 + x^3 + ... + x^n
for n =30, 60, 90, 120"""

def sum_calc(x, n):
    s=0
    for i in range (1, n+1):
        s=s+(x**i)
    
    return s

x = float(input("Enter the value of x: "))
print ("Sum is (n=30): ",sum_calc(x, 30))
print ("Sum is (n=60): ",sum_calc(x, 60))
print ("Sum is (n=90): ",sum_calc(x, 90))
print ("Sum is (n=120): ",sum_calc(x, 120))