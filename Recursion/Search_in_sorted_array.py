def search_arr(arr, l, key):
    if(l==0):
        return -1
    if(arr[l-1]==key):
        return l-1
    else:
        return search_arr(arr, l-1, key)
    

arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
l = len(arr)
key = 20
print(search_arr(arr, l, key))