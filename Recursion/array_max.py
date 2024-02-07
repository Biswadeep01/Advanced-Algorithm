def max_arr(arr, l, maxx):
    if(l==0):
        return maxx
    else:
        maxx = max(maxx, arr[l-1])
    
    return max_arr(arr, l-1, maxx)

arr = [1110, 20, 350, 40, 100, 60, 70, 80, 40]
l = len(arr)
maxx = arr[l-1]
print(max_arr(arr, l, maxx))