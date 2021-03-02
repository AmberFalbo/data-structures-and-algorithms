#   InsertionSort(int[] arr)

#     FOR i = 1 to arr.length
    
#       int j <-- i - 1
#       int temp <-- arr[i]

#       WHILE j >= 0 AND temp < arr[j]
#         arr[j + 1] <-- arr[j]
#         j <-- j - 1
        
#       arr[j + 1] <-- temp

def insertion_sort(array):
    for i in range(1, len(array)):
        previous_index = i - 1
        current_shorts = array[i]

        while previous_index >= 0 and current_shorts < array[previous_index]:
            array[previous_index + 1] = array[previous_index]
            previous_index = previous_index - 1

        array[previous_index + 1] = current_shorts
    return array
