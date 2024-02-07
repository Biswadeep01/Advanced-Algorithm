def search_arr(arr, l, key):
    if(l==0):
        return -1
    if(arr[l-1]==key):
        return l-1
    else:
        return search_arr(arr, l-1, key)

arr = [20, 40, 55, 10, 12, 5]
l = len(arr)
key = 12
print(search_arr(arr, l, key))