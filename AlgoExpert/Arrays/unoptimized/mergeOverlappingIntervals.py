def mergeOverlappingIntervals(intervals):
    array = sorted(intervals)
    result_array = []

    for start, end in array:
        if not result_array or start > result_array[-1][1]:
            result_array.append([start, end])
        else:
            result_array[-1][1] = max(result_array[-1][1], end)
    return result_array


print(
    mergeOverlappingIntervals(
        [[0, 1], [3, 4], [5, 6], [7, 19], [20, 21], [22, 24], [25, 27]]
    )
)
