
arr = [10,5,6,8,3,5,8]
def quicksort(arr):
    if len(arr) == 1:
        return arr
    else:
        pivot = arr[0]

        less = [i for i in arr[1:] if i < pivot]
        more = [i for i in arr[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(more)


print(quicksort(arr))