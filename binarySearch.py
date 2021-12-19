
def binarySearch(arr, low, high, x):
    if low >= high:
        if x == arr[low]:
            return low
        else:
            return False
    mid = int((low + high)/2)
    #print(arr, low, high, x, mid)

    if arr[mid] > x:
        return binarySearch(arr,low,mid-1,x)
    elif arr[mid] < x:
        return binarySearch(arr,mid+1,high,x)
    elif arr[mid] == x:
        #print("solution", mid)
        return mid
    else:
        return False

mySorted = [1, 2, 3, 4, 5, 6, 7]
res = binarySearch(mySorted,0,len(mySorted)-1,2)
print(res) # should be 1

mySorted = [1]
res = binarySearch(mySorted,0,len(mySorted)-1,2)
print(res) # should be false

mySorted = [1, 2, 3, 4, 5, 6, 7]
res = binarySearch(mySorted,0,len(mySorted)-1,1)
print(res) # should be 0

mySorted = [1, 2, 3, 4, 5, 6, 7]
res = binarySearch(mySorted,0,len(mySorted)-1,7)
print(res) # should by 6

mySorted = [1]
res = binarySearch(mySorted,0,len(mySorted)-1,1)
print(res) # should be 0

mySorted = [1, 2, 3, 4, 5, 6, 7]
res = binarySearch(mySorted,0,len(mySorted)-1,4)
print(res) # should be 3
