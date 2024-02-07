def str_length(str):
    if(str==''):
        return 0
    return 1 + str_length(str[1:])


str = input("Enter a string: ")
print("Length of the string is: ", str_length(str))