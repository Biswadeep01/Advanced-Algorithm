"""s = 1! + 2! + 3! + ... + n!"""

n = int(input("Enter the term: "))
s=0
f=1
for i in range (1, n+1):
    for j in range (1, i+1):
        f=f*j
    s=s+f

print ("The sum of 1 ! + 2 ! + ... +",n,"! is : ",s)