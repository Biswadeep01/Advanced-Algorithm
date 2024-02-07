x = float(input("Enter the radian value of cos: "))
n = int(input("Enter the term: "))
s=1
t=x
for i in range (1, n+1):
    t = -t + ((x*x)/((2*i-1)*2*i))
    s = s + t

print ("Sum is : ", s)
