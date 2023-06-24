def sortedSquaredArray(array):
    init = [0 for _ in array]

    length = len(init)
    smaller_index = 0
    larger_index = length - 1

    for idx in reversed(range(length)):
        small_value = array[smaller_index]
        large_value = array[larger_index]

        if abs(small_value) > abs(large_value):
            init[idx] = small_value * small_value
            smaller_index += 1
        else:
            init[idx] = large_value * large_value
            larger_index -= 1
    return init
