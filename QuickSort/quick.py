def quicksort(arr):
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quicksort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quicksort_recursive(low, pi - 1)
            quicksort_recursive(pi + 1, high)

    quicksort_recursive(0, len(arr) - 1)
    return arr

def quicksort_list(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivo = arr[0]
        menor_pivo = [x for x in arr[1:] if x <= pivo]
        maior_pivo = [x for x in arr[1:] if x > pivo]
        return quicksort_list(menor_pivo) + [pivo] + quicksort_list(maior_pivo) 

arr = [0,3,6,7,8,4,2,1,5]

arr = quicksort_list(arr)

print(arr)

test_array = [10, 7, 8, 9, 1, 5]
print("Unsorted array:", test_array)
sorted_array = quicksort(test_array)
print("Sorted array:", sorted_array)