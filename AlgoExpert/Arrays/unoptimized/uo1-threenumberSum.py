def threeNumberSum(array, targetSum):
    result = []
    i = 0
    array = sorted(array)
    while i < len(array):
        if array[i] < 0:
            start = array[i]
            end = abs(array[i])
        else:
            start = -array[i]
            end = array[i]
        current_element = array[i]
        for j in range(start, end + 1):
            if j in array and targetSum - (current_element + j) in array:
                print(j, array[i], targetSum - (current_element + j))
                element = sorted([j, array[i], targetSum - (current_element + j)])
                if element not in result and len(set(element)) == len(element):
                    result.append(element)
        i = i + 1
    return result
