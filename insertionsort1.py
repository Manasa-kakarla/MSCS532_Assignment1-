def insertion_sort(arr):
    # Traverse the array from 1 to the end of the array
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1
        # shift elements of arr[0 to i-1], that are greater than
        # temp, to one position ahead of their current position
        while j >= 0 and arr[j] < temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

a = [34, 25, 82, 19, 3]
print("original array:", a)
insertion_sort(a)
print("sorted array in decreasing order:", a)