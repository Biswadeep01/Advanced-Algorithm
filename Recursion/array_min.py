def min_arr(a, l):
    if(l==1):
        return a[0]
    
    return min(a[l-1], min_arr(a, l-1))


a = [10, 20, 30, 5, 50, 60]
l = len(a)
print("Minimum of array is: ", min_arr(a, l))