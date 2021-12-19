myList = [9, 2, 4, 5, 6, 8, 3, 7]


def merge(arr1, arr2):
    arr3 = []
    while len(arr1) > 0 and len(arr2) > 0:
        if arr1[0] > arr2[0]:
            arr3.append(arr2.pop(0))
        else:
            arr3.append(arr1.pop(0))
    """
    #print(arr1, arr2)
    while len(arr1) > 0:
         arr3.append(arr1.pop(0))

    while len(arr2) > 0:
         arr3.append(arr2.pop(0))
    """

    while len(arr1) > 0:
    arr3.append(arr1.pop(0))

     while len(arr2) > 0:
         arr3.append(arr2.pop(0))

    return arr3


def mergeSort(arr):
    if len(arr) == 1:
        return arr

    arr1 = arr[:int(len(arr)/2)]
    arr2 = arr[int(len(arr)/2):]
    
    arr1 = mergeSort(arr1)
    arr2 = mergeSort(arr2)

    return merge(arr1, arr2)


#print(merge([1,9], [3,5,7]))
print("Original List : \n", myList, "\n New Sorted List : ")
print(mergeSort(myList))