def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Read 8 numbers from keyboard
arr = []
print("Enter 8 numbers:")
for _ in range(8):
    num = int(input())
    arr.append(num)

# Sort the numbers using Bubble Sort
bubbleSort(arr)
print("Sorted numbers are:", arr)
