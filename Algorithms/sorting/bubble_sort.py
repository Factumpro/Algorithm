def swap(arr, i, j):
    arr[j], arr[i] = arr[i], arr[j]
    return arr

def bubble_sort(arr):
    """
    Time Complexity: O(n**2)
    """
    L = len(arr)
    for i in range(L):
        for j in range(1, L - i):
            if arr[j - 1] > arr[j]:
                arr = swap(arr, j, j - 1)
    return arr