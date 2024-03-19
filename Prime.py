"""Prime Number check"""

n = int(input("Enter a number: "))
for i in range(2, n//2 + 1):
    if n % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")



"""Prime number in Range"""

for i in range(100, 999):
    for j in range(2, i//2 +1):
        if i % j == 0:
            break
    else:
        prime = i

print("Largest 3 digit prime number is: ", prime)