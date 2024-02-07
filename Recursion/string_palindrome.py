def str_reverse(str, l):
    if (l == 1):
        return str[0]
    else:    
        return str[l-1] + str_reverse(str, l-1)

def check(str):
    l = len(str)
    str_pal= str_reverse(str, l)
    if str == str_pal:
        return 1
    else:
        return 0


str = input("Enter a string: ")
print("Palindrome: ", check(str))