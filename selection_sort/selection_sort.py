def selection_sort(arr):
    for i in range(0, len(arr)-1):
        current_minimum = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[current_minimum]:
                current_minimum = j

        arr[i], arr[current_minimum] = arr[current_minimum], arr[i]
    return arr
arr = [36,24,7,18,11,30,50,2]
print("Sorted List: ", selection_sort(arr))
