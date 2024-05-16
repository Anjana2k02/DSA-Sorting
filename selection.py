def selection_sort(arr):
    n = len(arr)
    for j in range(n - 1):
        smallest = j
        for i in range(j + 1, n):
            if arr[i] < arr[smallest]:
                smallest = i
        # Swap the smallest element with the current element at index j
        arr[j], arr[smallest] = arr[smallest], arr[j]

# Test the function
numbers = [64, 25, 12, 22, 11]
selection_sort(numbers)
print("Sorted array is:", numbers)
