saved_index = 0

def BinarySearch(array, term):
    global saved_index
    if len(array) == 1:
        if term == array[0]:
            return saved_index
        else:
            return -1    
    half = len(array) // 2
    if saved_index == 0:
        saved_index = half
    if term == array [half]:
        return half
    elif term < array [half]:
        saved_index = saved_index - half // 2
        sliced_array = array[slice(0,half)]
        print("sliced down", sliced_array)
    elif term > array [half]:
        saved_index = saved_index + half // 2
        sliced_array = array[slice(half, len(array))]
        print("sliced up", sliced_array)
    return BinarySearch(sliced_array, term)  



num_array = [1, 10, 20, 30, 40, 50, 60, 70, 80]
term = 80



print(BinarySearch(num_array, term))