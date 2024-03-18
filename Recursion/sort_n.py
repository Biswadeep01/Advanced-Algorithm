def sort(arr, n):
    if n == 1:
        return arr
    i=0
    while i < n:
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        i += 1
    return sort(arr, n-1)
    
arr = [45, 20, 100, 0, 70, 84, 95, 25, 52, 63, 36]
l = len(arr)
print(sort(arr, l-1))