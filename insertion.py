# Insertion sort algorithm
def insertion_sort(arr):
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return comparisons

# Test the function
numbers = [12, 11, 13, 5, 6]
comparisons = insertion_sort(numbers)
print("Sorted array is:", numbers)
print("Number of comparisons:", comparisons)
