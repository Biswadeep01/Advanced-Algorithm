"""s = 1 + x/1! + x^2/2! + x^3/3! + ... + x^n/n!"""

"""import math
def sin(x, n):
  sum = 0
  t = x
  for i in range(1, n+1):
    t = t / i
    sum += t
  return sum"""

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)
 

def sum(x, n):
    total = 1.0
    for i in range (1, n + 1, 1):
        total = total + (pow(x, i) / fact(i))
 
    return total

if __name__== '__main__':

    x = float(input("Enter the radian value of sin: "))
    n = int(input("Enter the term: "))
 
    # Print output
    print ("Sum is: {0:.4f}".format(sum(x, n)))
