"""s = 1 + 2 + 3 + ... + n"""

n = int(input("Enter the term: "))
s=0
for i in range (1, n+1):
    s=s+i

print ("The sum of first",n," numbers is : ",s)