def sortedSquaredArray(array):
    sorted_square = [0 for _ in array]

    least_index = 0
    highest_index = len(array) - 1

    for i in reversed(range(len(array))):
        highest_value = array[highest_index]
        least_value = array[least_index]

        if abs(highest_value) < abs(least_value):
            sorted_square[i] = least_value * least_value
            least_index = least_index + 1
        else:
            sorted_square[i] = highest_value * highest_value
            highest_index = highest_index - 1

    return sorted_square


# bruteforce O(nlogn)
def sorted_square(array):
    return sorted([x * x for x in array])


# One liner o(nlogn)
sortedSquaredArray = lambda array: sorted([x**2 for x in array])
