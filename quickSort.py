
def partition(arr, low, high):
	i = (low-1)
	pivot = arr[high]
	for j in range(low, high):
		print(i,j,low,high)
		if arr[j] <= pivot:
			i = i+1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i+1], arr[high] = arr[high], arr[i+1]
	return (i+1)


def quickSort(arr, low, high):
	if len(arr) == 1:
		print("len 1", arr)
		return arr
	if low < high:
		print("in part: ", arr, low, high)
		part = partition(arr, low, high)
		#print(low, high, arr, part)
		quickSort(arr, low, part-1)
		quickSort(arr, part+1, high)



test = [7,2,1,8,6,3,5,4]
n = len(test)
quickSort(test, 0, n-1)
print("Sorted array is:", test)

"""
test1 = [7,2,1,8,6,3,5,4]
print(test1)
print(partition(test1, 0, len(test1)-1))
print(test1)
print(partition(test1, 0, 2))
print(test1)
print(partition(test1, 4, len(test1)-1))
print(test1)
"""