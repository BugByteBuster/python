def longestPeak(array):
    array_len = []
    for i in range(1, len(array) - 1):
        result_array = []
        if array[i] > array[i-1] and array[i] > array[i+1]:

            leftIndex = i - 2
            while leftIndex >= 0 and array[leftIndex] < array[leftIndex + 1]:
                result_array.append(array[leftIndex])
                leftIndex -= 1 
            
            rightIndex = i + 2
            while rightIndex < len(array) and array[rightIndex] < array[rightIndex - 1]:
                result_array.append(array[rightIndex])
                rightIndex += 1
            array_len.append(len(result_array))
    
    if len(array_len) > 0:
        return max(array_len) + 3
    else:
        return 0  