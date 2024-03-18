def deci_binary(deci):
    if deci == 0:
        return 0
    else:
        return deci%2 + 10*deci_binary(deci//2)


deci = int(input("Enter a number: "))
print("Binary: ",deci_binary(deci))