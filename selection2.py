def partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

def read_numbers():
    numbers = []
    num_count = int(input("Enter the number of elements: "))
    print("Enter the numbers:")
    for _ in range(num_count):
        num = int(input())
        numbers.append(num)
    return numbers

# Main program
if __name__ == "__main__":
    # Read numbers and store them in an array
    arr = read_numbers()
    print("Array before partitioning:", arr)

    # Call partition function
    p = 0
    r = len(arr) - 1
    partition_index = partition(arr, p, r)

    # Display the array after partitioning
    print("Array after partitioning:", arr)
    print("Partition index:", partition_index)
