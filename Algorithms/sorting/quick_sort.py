def quick_sort(arr):
    """ 
    Time Complexity: O(n log n). 
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for x in arr[1:]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)
    return sort(left) + [pivot] + sort(right)
