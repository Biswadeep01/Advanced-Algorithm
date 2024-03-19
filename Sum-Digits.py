"""1234 = 1+ 2+ 3+ 4"""

n = int(input("Enter the number: "))
s=0
while(n!=0):
    r=n%10
    s=s+r
    n=n//10
print("The sum of digits is: ",s)