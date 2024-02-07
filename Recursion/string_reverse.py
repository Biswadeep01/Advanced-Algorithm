def str_reverse(str, l):
    if (l == 1):
        return str[0]
    else:    
        return str[l-1] + str_reverse(str, l-1)

str = input("Enter a string: ")
l = len(str)
print(str_reverse(str, l))