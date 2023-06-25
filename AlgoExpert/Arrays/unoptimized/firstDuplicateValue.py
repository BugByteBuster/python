def firstDuplicateValue(array):
    dict = {}
    if len(array) == 0 or len(array) == len(set(array)):  # O(n) time complex
        return -1
    else:
        for i in range(len(array)):  # O(n) time complexity
            left_array = array[:i]
            count = left_array.count(array[i])
            if count >= 1 and count not in dict.keys():  # O(n) time complexity
                dict[count] = array[i]
    return list(dict.values())[0]  # O(n) time complexity
